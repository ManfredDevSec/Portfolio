from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.request import Request as DRFRequest

from .api_views import PortfolioDataAPIView, ProjectDetailAPIView
from .models import Project


def _call_api(view_class, request, **kwargs):
    """
    Call a DRF APIView internally and return its .data dict.
    No HTTP round-trip — direct Python call.
    """
    drf_request = DRFRequest(request)
    view = view_class()
    view.request = drf_request
    view.kwargs = kwargs
    response = view.get(drf_request, **kwargs)
    return response.data


def index(request):
    data = _call_api(PortfolioDataAPIView, request)

    # Group skills by category for the template
    skills_by_category = {}
    for skill in data.get('skills', []):
        cat = skill['category']
        skills_by_category.setdefault(cat, []).append(skill)

    context = {
        'projects': data.get('projects', []),
        'skills': data.get('skills', []),
        'skills_by_category': skills_by_category,
        'experience': data.get('experience', []),
        'contact_links': data.get('contact_links', []),
    }
    return render(request, 'core/index.html', context)


def project_detail(request, slug):
    data = _call_api(ProjectDetailAPIView, request, slug=slug)
    if 'detail' in data:
        raise Http404
    return render(request, 'core/project_detail.html', {'project': data})
