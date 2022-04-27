from django.urls import path, include

from . import views

urlpatterns = [
    path('editor/languages', views.LanguageList.as_view()),
    path('editor/democode/<int:lang_id>', views.LanguageDemoCode.as_view()),
]