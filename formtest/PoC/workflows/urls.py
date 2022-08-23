from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), #homepage
    path('workflows/', views.workflows, name="workflows"),
    path('workflow/<str:pk>', views.workflow, name="workflow"),
    path('create-workflow/', views.createView, name="create-workflow"),
    path('update-workflow/<str:pk>', views.updateView, name="update-workflow"),
    path('delete-workflow/<str:pk>', views.deleteView, name="delete-workflow"),





    
]