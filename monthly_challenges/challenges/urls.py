from django.urls import path
from . import views

# after reachving /challenges

urlpatterns = [
    path("january", views.jan),      # reching for /challenges/january
    path('february', views.feb)
]
