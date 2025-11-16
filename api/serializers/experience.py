from rest_framework import serializers
from api.models.experience import Experience
from api.models.skills import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        ref_name = "ExperienceSkill"



class ExperienceSerializer(serializers.ModelSerializer):
    skills_used = SkillSerializer(many=True, read_only=True)
    skills_used_ids = serializers.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Experience
        fields = [
            "id", "role", "company", "subtitle",
            "description", "start_date", "end_date",
            "skills_used", "skills_used_ids"
        ]

    def create(self, validated_data):
        skills_ids = validated_data.pop("skills_used_ids", [])
        exp = Experience.objects.create(**validated_data)
        exp.skills_used.set(skills_ids)
        return exp

    def update(self, instance, validated_data):
        skills_ids = validated_data.pop("skills_used_ids", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if skills_ids is not None:
            instance.skills_used.set(skills_ids)

        return instance
