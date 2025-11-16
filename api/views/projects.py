from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.projects import Project, Category, ProjectImage
from api.serializers.projects import (
    ProjectSerializer,
    CategorySerializer,
    ProjectImageSerializer
)
from api.utils.hero_mixin import HeroPageMixin

class CategoryViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    hero_page = "projects"



class ProjectViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    hero_page = "projects"

    # Custom endpoint to upload multiple images
    @action(detail=True, methods=["post"])
    def upload_images(self, request, pk=None):
        project = self.get_object()

        images = request.FILES.getlist("images")

        for img in images:
            ProjectImage.objects.create(project=project, image=img)

        return Response({"status": "images uploaded"})


class ProjectImageViewSet(HeroPageMixin,viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    serializer_class = ProjectImageSerializer
    hero_page = "projects"

