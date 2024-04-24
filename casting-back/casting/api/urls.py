from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
    path('castings/', views.get_castings),
    path('castings/<int:id>/', views.casting_details),
    path("castings/<int:id>/positions/", views.casting_positions),
    path("positions/", views.PositionstListAPIView.as_view()),
    path('positions/<int:id>/', views.PositionsDetailAPIView.as_view()),

]

