from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Project, Skill, Experience, ContactLink
from .serializers import (
    ProjectSerializer, SkillSerializer,
    ExperienceSerializer, ContactLinkSerializer,
)


class ProjectListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        projects = Project.objects.prefetch_related('tags').order_by('order', '-created_at')
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, slug):
        try:
            project = Project.objects.prefetch_related('tags').get(slug=slug)
        except Project.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


class SkillListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        skills = Skill.objects.filter(is_active=True)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)


class ExperienceListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        experiences = Experience.objects.filter(is_active=True)
        serializer = ExperienceSerializer(experiences, many=True)
        return Response(serializer.data)


class ContactLinkListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        links = ContactLink.objects.filter(is_active=True)
        serializer = ContactLinkSerializer(links, many=True)
        return Response(serializer.data)


class PortfolioDataAPIView(APIView):
    """Single endpoint returning all portfolio data — used by the template view."""
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'projects': ProjectSerializer(
                Project.objects.prefetch_related('tags').order_by('order', '-created_at'),
                many=True
            ).data,
            'skills': SkillSerializer(
                Skill.objects.filter(is_active=True),
                many=True
            ).data,
            'experience': ExperienceSerializer(
                Experience.objects.filter(is_active=True),
                many=True
            ).data,
            'contact_links': ContactLinkSerializer(
                ContactLink.objects.filter(is_active=True),
                many=True
            ).data,
        })
