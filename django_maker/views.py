from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from .models import Play_Project
import json
import os
import subprocess
from django.utils.crypto import get_random_string
from proxy.views import proxy_view


# Path settings
# {{
dir_path = os.path.dirname(os.path.realpath(__file__))
bin_string = dir_path + "/bin/"
command_run_make_cont = "/bin/bash {bin_string}make_cont.sh {project_id}"
command_run_del_cont = "/bin/bash {bin_string}del_cont.sh {project_id}"
my_env = os.environ.copy()
my_env["DJANGO_SETTINGS_MODULE"] = "user_project.settings"
# }}

def index(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    context_dict = {'con_001': proj.con_001,
                    'id': proj.id,
                    'project_id': project_id,
                    }
    return render(request, 'django_maker/index.html', context=context_dict)

def new_project(request):
    proj = Play_Project()
    def_id = get_random_string(length=32)
    proj.unique_id = def_id
    proj.save()
    return HttpResponseRedirect('/index/{}/'.format(def_id))

def save(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    saved = False
    if request.method == 'POST':
        str_request = request.body.decode('utf-8')
        json_data = json.loads(str_request)
        proj.con_001 = json_data['con_001']
        proj.save()
        saved = True
    return JsonResponse({'saved': saved})

def make(request, project_id):
#    subprocess.run(command_run_make_cont.format(bin_string=bin_string, project_id=project_id).split(), env=my_env)
    return JsonResponse({'ran': True})

def view(request, project_id):
    proj = Play_Project.objects.get(unique_id=project_id)
    remoteurl = project_id + ".app:8000"
    return proxy_view(request, remoteurl)

def kill(request, project_id):
    proj = Play_Project.objects.get(usique_id=project_id)
#    subprocess.run(command_run_del_cont.format(bin_string=bin_string, project_id=project_id).split(), env=my_env)
