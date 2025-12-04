from rest_framework import serializers
from api.models.projects import Project, Category, ProjectImage
from api.models.skills import Skill


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["id", "image"]


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    categories = CategorySerializer(many=True, read_only=True)
    categories_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    tech_stack = serializers.StringRelatedField(many=True, read_only=True)
    tech_stack_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Project
        fields = [
            "id", "title", "subtitle", "description",
            "live_link", "live_demo", "github_link",
            "tags", "categories", "categories_ids",
            "tech_stack", "tech_stack_ids",
            "images"
        ]

    def create(self, validated_data):
        categories_ids = validated_data.pop("categories_ids", [])
        tech_ids = validated_data.pop("tech_stack_ids", [])

        project = Project.objects.create(**validated_data)
        project.categories.set(categories_ids)
        project.tech_stack.set(tech_ids)

        return project

    def update(self, instance, validated_data):
        categories_ids = validated_data.pop("categories_ids", None)
        tech_ids = validated_data.pop("tech_stack_ids", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if categories_ids is not None:
            instance.categories.set(categories_ids)

        if tech_ids is not None:
            instance.tech_stack.set(tech_ids)

        return instance
