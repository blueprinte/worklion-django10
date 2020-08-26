from django.urls import path
from . import views

app_name="doggy"

urlpatterns = [
    path('doggy_list/', views.doggy_list, name="doggy_list"),
    path('doggy_api/', views.doggy_api, name="doggy_api"),
]