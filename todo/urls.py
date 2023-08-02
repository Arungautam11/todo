from django.urls import path
from . import views


urlpatterns = [

    #Add the task features
    path('addTask/', views.addTask, name='addTask'),

    # Task the mark as done features
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),

    #Task the mark as undone features
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),

    #Task the edit features
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),

    #Task the delete features
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]