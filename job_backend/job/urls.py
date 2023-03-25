from django.urls import path

from .views import *

app_name = 'job'

urlpatterns = [
    path('newest/', NewestJobsView.as_view()),
    path('<int:pk>/', JobsDetailView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('', BrowseJobsView.as_view()),
    path('my/', MyJobsView.as_view()),
    path('create/', CreateJobView.as_view()),
    path('<int:pk>/delete/', CreateJobView.as_view()),
    path('<int:pk>/edit/', CreateJobView.as_view()),
]