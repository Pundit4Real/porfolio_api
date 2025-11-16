from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.abouts import AboutViewSet, ExpertiseViewSet
from api.views.contact import ContactMessageViewSet, ContactInfoViewSet
from api.views.experience import ExperienceViewSet
from api.views.hero import HomeViewSet, HeroSectionViewSet
from api.views.projects import ProjectViewSet, CategoryViewSet, ProjectImageViewSet
from api.views.services import ServiceViewSet
from api.views.skills import SkillViewSet
from api.views.testimonials import TestimonialViewSet


router = DefaultRouter()

router.register("about", AboutViewSet)
router.register("expertise", ExpertiseViewSet)

router.register("contact-messages", ContactMessageViewSet)
router.register("contact-info", ContactInfoViewSet)

router.register("experience", ExperienceViewSet)

router.register("home", HomeViewSet)
router.register("hero", HeroSectionViewSet)

router.register("projects", ProjectViewSet)
router.register("project-categories", CategoryViewSet)
router.register("project-images", ProjectImageViewSet)

router.register("services", ServiceViewSet)
router.register("skills", SkillViewSet)

router.register("testimonials", TestimonialViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
