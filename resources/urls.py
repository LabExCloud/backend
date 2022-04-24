from django.urls import path, include

from resources import views

urlpatterns = [
    path('resources', views.ResourceList.as_view()),
    path('resources/sem/<int:sem>', views.ResourceListSem.as_view()),
    path('resources/res/<int:r_id>', views.ResourceDetail.as_view()),
]