from django.urls import path
from home import views

app_name='home'
urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.index)
]