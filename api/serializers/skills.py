from rest_framework import serializers
from api.models.skills import Skill


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        ref_name = "TechStackSkill"

