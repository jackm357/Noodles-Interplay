from django.urls import path, include


from . import views

urlpatterns = [
    path('', views.index, name='main'),
    #path('continue/', views.continue_page, name='continue'),
    path('interpolate/', views.interpolate_page, name='interpolate'),
    path('generate/', views.generate_page, name='generate'),
    path('melody/', views.melody_page, name='melody'),
    path('drums/', views.drum_page, name='drums'),
    path('download/', views.download_page, name='download')
]
