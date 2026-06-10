from django.urls import path
from .api_views import (
    ProjectListAPIView, ProjectDetailAPIView,
    SkillListAPIView, ExperienceListAPIView,
    ContactLinkListAPIView, PortfolioDataAPIView,
)

urlpatterns = [
    path('portfolio/', PortfolioDataAPIView.as_view(), name='api-portfolio'),
    path('projects/', ProjectListAPIView.as_view(), name='api-projects'),
    path('projects/<slug:slug>/', ProjectDetailAPIView.as_view(), name='api-project-detail'),
    path('skills/', SkillListAPIView.as_view(), name='api-skills'),
    path('experience/', ExperienceListAPIView.as_view(), name='api-experience'),
    path('contact/', ContactLinkListAPIView.as_view(), name='api-contact'),
]
