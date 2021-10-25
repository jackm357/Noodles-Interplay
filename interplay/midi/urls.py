from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('continue/', views.continue_page, name='continue'),
    path('interpolate/', views.interpolate_page, name='interpolate'),
    path('generate/', views.generate_page, name='generate'),
]