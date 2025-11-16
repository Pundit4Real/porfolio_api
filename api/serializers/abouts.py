from rest_framework import serializers
from api.models.abouts import About, Expertise
from api.models.skills import Skill


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = "__all__"


class AboutSerializer(serializers.ModelSerializer):
    expertise = ExpertiseSerializer(many=True, read_only=True)
    expertise_ids = serializers.PrimaryKeyRelatedField(
        queryset=Expertise.objects.all(),
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

    image = serializers.ImageField(read_only=True)

    class Meta:
        model = About
        fields = [
            "id", "bio", "image",
            "expertise", "expertise_ids",
            "tech_stack", "tech_stack_ids"
        ]

    def create(self, validated_data):
        expertise_ids = validated_data.pop("expertise_ids", [])
        tech_stack_ids = validated_data.pop("tech_stack_ids", [])

        about = About.objects.create(**validated_data)
        about.expertise.set(expertise_ids)
        about.tech_stack.set(tech_stack_ids)
        return about

    def update(self, instance, validated_data):
        expertise_ids = validated_data.pop("expertise_ids", None)
        tech_stack_ids = validated_data.pop("tech_stack_ids", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if expertise_ids is not None:
            instance.expertise.set(expertise_ids)

        if tech_stack_ids is not None:
            instance.tech_stack.set(tech_stack_ids)

        return instance
