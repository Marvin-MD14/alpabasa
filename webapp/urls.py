from django.urls import path
from . import views
from . import tts   # ✅ Nandito na ang tts

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about_page'),
    
    # ✅ DAGDAG ITO: Para mawala ang NoReverseMatch error
    path('aralin/', views.aralin, name='aralin'), 

    # ✅ TTS path
    path('speak/', tts.speak, name='speak'),

    path('talahayanan/', views.talahayanan, name='talahayanan'),
]