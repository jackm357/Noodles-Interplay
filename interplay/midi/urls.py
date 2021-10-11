from django.urls import path, include


from midi.views import midi, contin

urlpatterns = [
    path('', midi.main),
    path('continue/', contin.main),
]