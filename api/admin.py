from time import timezone
from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin
from django.shortcuts import redirect
from api.models.abouts import About, Expertise
from api.models.contact import ContactMessage, ContactInfo
from api.models.experience import Experience
from api.models.hero import Home, HeroSection
from api.models.projects import Project, Category, ProjectImage
from api.models.services import Service
from api.models.skills import Skill
from api.models.testimonials import Testimonial
from api.utils.contact_email import send_contact_reply_email
from django.contrib import messages
from django.utils import timezone


@admin.register(Expertise)
class ExpertiseAdmin(admin.ModelAdmin):
    list_display = ['title', 'proficiency_level', 'years_of_experience']
    search_fields = ['title']
    list_filter = ['proficiency_level', 'title']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'bio']
    filter_horizontal = ['expertise', 'tech_stack']


# ---------------------------
# CONTACT
# ---------------------------
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'status_label', 'created_at', 'responded_at']
    list_filter = ['responded', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at', 'responded_at']
    change_form_template = "admin/change_form.html"

    def status_label(self, obj):
        """Styled status badge for admin list."""
        if obj.responded:
            return format_html(
                '<span style="padding:4px 8px; background:#10B981; color:white; '
                'border-radius:4px; font-size:12px;">Responded</span>'
            )
        return format_html(
            '<span style="padding:4px 8px; background:#EF4444; color:white; '
            'border-radius:4px; font-size:12px;">Pending</span>'
        )
    status_label.short_description = "Status"

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_send_reply'] = True
        return super().changeform_view(request, object_id, form_url, extra_context)

    def response_change(self, request, obj):
        """Handles the Send Reply button."""
        if "send_reply" in request.POST:
            if not obj.response_message:
                messages.error(request, "Please type a response message before sending.")
                return redirect("admin:api_contactmessage_change", obj.id)

            send_contact_reply_email(obj)
            obj.responded = True
            obj.responded_at = timezone.now()
            obj.save()

            messages.success(request, "Reply email has been sent successfully.")
            return redirect("admin:api_contactmessage_change", obj.id)

        return super().response_change(request, obj)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['address','phone', 'email', 'linkedin', 'github', 'twitter', 'telegram']
    search_fields = ['phone', 'email', 'linkedin', 'github', 'twitter', 'telegram']


# ---------------------------
# EXPERIENCE
# ---------------------------
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'end_date']
    search_fields = ['role', 'company', 'subtitle', 'description']
    filter_horizontal = ['skills_used']
    list_filter = ['start_date', 'end_date']


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    search_fields = ['name', 'title', 'keywords']


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['page', 'headline', 'subheadline']
    search_fields = ['headline', 'subheadline']


# ---------------------------
# PROJECT + IMAGES
# ---------------------------
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']
    search_fields = ['title', 'subtitle', 'description', 'tags']
    filter_horizontal = ['category', 'tech_stack']
    inlines = [ProjectImageInline]


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ['project', 'image_preview']
    readonly_fields = ['image_preview']
    search_fields = ['project__title']

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
    image_preview.short_description = "Preview"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# ---------------------------
# SERVICES + SKILLS
# ---------------------------
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'highlight', 'price','is_active']
    search_fields = ['title', 'description', 'icon', 'price']
    list_filter = ['highlight',"is_active"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level']
    search_fields = ['name', 'level']


# ---------------------------
# TESTIMONIALS
# ---------------------------
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'date', 'rating', 'average_rating_display']
    search_fields = ['name', 'role', 'company', 'feedback']
    list_filter = ['date']

    def average_rating_display(self, obj):
        stats = Testimonial.get_stats()
        return stats.get("average_rating", 0)

    average_rating_display.short_description = "Average Rating"
