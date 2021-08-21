from django.shortcuts import render
from .models import Project
# Create your views here.
def blog(request):
    projects = Project.objects.all()
    return render(request, "blog/blog.html", {'projects':projects})
