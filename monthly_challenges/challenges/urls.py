from django.urls import path
from . import views

# after reachving /challenges

urlpatterns = [
        path('<int:month>', views.monthly_challenges_num),       # palceholder with label 'month'
        path('<str:month>', views.monthly_challenges)       # palceholder with label 'month'
]
