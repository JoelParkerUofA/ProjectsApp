from django.shortcuts import render
from projects.models import Project

# Create your views here.

# create index view
def project_index(request):
    projects = Project.objects.all() # reteive all instances in projects table
    context = {
        "projects": projects # create a dictionary with project information
    }
    return render(request, "projects/project_index.html", context) # renders index.html with the information from the projects


# Create detail veiw which utilizes a key to make sure the correct project is rendered. 
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)