from django.urls import path, include

from . import views

urlpatterns = [
    path('labs', views.LabExperimentList.as_view()),
    path('labs/sem/<int:sem>', views.LabExperimentListSem.as_view()),
    # path('resources/res/<int:r_id>', views.ResourceDetail.as_view()),
    # path('resource/<int:id>', views.ModifyResource.as_view()),
    # path('resourcefile/<int:id>', views.ModifyResourceFile.as_view()),
]