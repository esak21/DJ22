from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from .models import Project, Tag, Review, ProjecDetails

# msg = "Hello we are on the Projects Page -- May22"
# number = 11
# tech = ['Python', 'scala', 'aws', 'snowflake']
# projectlist = [
#     {
#         "id": 1001,
#         "Profile": "dev",
#         "skills": ['Python', 'scala', 'aws', 'snowflake']
#     },
#             {
#         "id": 1002,
#         "Profile": "qa",
#         "skills": ['Python', 'Testing', 'aws', 'selenium']
#     },
#             {
#         "id": 1001,
#         "Profile": "dba",
#         "skills": ['Python', 'rds', 'aws', 'snowflake']
#     }
# ]

# context =  { 'msg': msg , 
#                 'number': number ,
#                 'projectlist': projectlist
#             }


# creating Model Views 

from .forms import ProjectForm

@login_required(login_url='login')
def deleteProject(request,pk):
    proj_obj = Project.objects.get(id=pk)
    if request.method =="POST":
        proj_obj.delete()
        return redirect('projects')
    context ={'object': proj_obj}
    return render(request, 'projects/delete_template.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    proj_obj = Project.objects.get(id=pk)

    #we are creating a Form using the project Object 
    form = ProjectForm(instance=proj_obj)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=proj_obj)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render ( request, 'projects/project_form.html', context)
# if the user tries to navigate to add projects Page and of they are not logged in , website redirects them to the login page 
@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, request.FILES)
        # request.FILES we can get the uploaded Files 
        if form.is_valid():
            form.save() # it will save the form data in Database
            return redirect('projects') 
    return render (request, 'projects/project_form.html', context)
                

def projects(request):
    #return HttpResponse('Here are our Products')
    # return the HTML response 
    # get all the Projects from DB 
    projects = Project.objects.all()
    context = {'projects': projects}
    print(context)

    return render(request, 'projects/projects.html', context )

def project(request, pk):
    #return HttpResponse(f'single Project -- {pk}')
    project_object = Project.objects.get(id=pk)
    tags = project_object.tags.all()
    return render(request, 'projects/single_project.html', {'project': project_object, 'tags': tags })


def diagram(request):
    qs = ProjecDetails.objects.all()
    project_data = [
        {
            'project': x.name,
            "start": x.start_date,
            "finish": x.end_date,
            "responsible": x.responsible
        } for x in qs
    ]

    df = pd.DataFrame(project_data)
    fig = px.timeline(
        df,
        x_start="start",
        x_end="finish",
        y="project",
        color="responsible"
    )

    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")

    context ={'plot_div': gantt_plot}
    return render(request, 'projects/projectdetails.html', context)