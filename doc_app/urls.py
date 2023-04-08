
from django.urls import path

from doc_app import views

urlpatterns = [
    path('', views.all_students, name='all_students'),
    path('graduate_students/', views.graduate_students, name='graduate_students'),
    path('studying/', views.studying, name='studying'),
    path('courses/', views.all_courses, name='courses'),
    path('crate_certification/<int:id>/', views.crate_certification, name='crate_certification'),
]
