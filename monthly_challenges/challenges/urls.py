from django.urls import path
from . import views

# after reachving /challenges

urlpatterns = [
        path('', views.index),       # applies only for /challenges
        path('<int:month>', views.monthly_challenges_num),       # palceholder with label 'month'
        path('<str:month>', views.monthly_challenges, name='month-url')       # palceholder with label 'month'
]
