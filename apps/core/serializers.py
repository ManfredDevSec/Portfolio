from rest_framework import serializers
from .models import Project, Skill, Experience, ContactLink


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'label', 'order']


class ProjectSerializer(serializers.ModelSerializer):
    all_tags = serializers.SerializerMethodField()
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'slug', 'tagline', 'description',
            'status', 'status_display', 'all_tags',
            'github_url', 'live_url', 'order', 'is_featured',
            'created_at',
        ]

    def get_all_tags(self, obj):
        return obj.get_all_tags()


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'role', 'company', 'year_range', 'description', 'order']


class ContactLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactLink
        fields = ['id', 'label', 'value', 'url', 'icon', 'order']
