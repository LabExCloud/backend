from django.urls import path, include

from resources import views

urlpatterns = [
    path('resources', views.ResourceList.as_view()),
    path('resources/sem/<int:sem>', views.ResourceListSem.as_view()),
    path('resources/class/<int:id>', views.ResourceListClass.as_view()),
    path('resources/res/<int:id>', views.ResourceDetail.as_view()),
    path('resources/file/<int:id>', views.ModifyResourceFile.as_view()),
]