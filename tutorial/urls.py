from django.urls import path
from . import views

app_name = 'tutorial'
urlpatterns = [
   	
Path(‘’, views.homepage, name=“homepage”),
      
]