from django.shortcuts import render, redirect
from . models import Workflow, Profile
from django.http import HttpResponseRedirect
from django.urls import reverse
from . forms import WorkflowForm


# Create your views here.
def index(request):
  return render(request, 'workflows/index.html', {
    
})
    

    
def workflows(request):
    workflows = Workflow.objects.all()
    context = {'workflows': workflows}
    return render(request, 'workflows/workflows.html', context)
    # 'workflows': Workflow.objects.all()

def workflow(request,pk):
    workflowObj = Workflow.objects.get(id=pk)
    profiles = Profile.objects.all()
    return render(request, 'workflows/single-workflow.html', {'workflow': workflowObj,'profiles': profiles})
  
def createView(request):
    form = WorkflowForm()
    if request.method == 'POST':
        form = WorkflowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workflows') # change this if you want them to be redirected elsehwere
    context ={'form': form}
    return render(request, 'workflows/workflow_form.html', context)


def updateView(request, pk):
    workflow = Workflow.objects.get(id=pk)
    form = WorkflowForm(instance=workflow)
    
    if request.method == 'POST':
        form = WorkflowForm(request.POST, instance=workflow)
        if form.is_valid():
            form.save()
            return redirect('workflows') # change this if you want them to be redirected elsehwere
    context ={'form': form}
    return render(request, 'workflows/workflow_form.html', context)



def deleteView(request, pk):
    if request.method == 'POST':
        workflow = Workflow.objects.get(id=pk)
        workflow.delete()
    return HttpResponseRedirect(reverse('workflows'))