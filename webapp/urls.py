from django.urls import path
from . import views
from . import tts   # ✅ idagdag ito

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_page'),

    # ✅ ADD THIS
    path('speak/', tts.speak, name='speak'),
]