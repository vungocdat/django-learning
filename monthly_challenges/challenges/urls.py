from django.urls import path
from . import views

# after reachving /challenges

urlpatterns = [
        path('<str:month>', views.monthly_challenges)       # palceholder with label 'month'
]
