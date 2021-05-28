from django.urls import path
from . import views

urlpatterns = [

    path('',views.CVTemplate.as_view())
]
