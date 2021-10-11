from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('continue/', views.continue_page, name='continue'),
]