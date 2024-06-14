from django.contrib import admin
from django.urls import path
from .views import *
import api.views as views


urlpatterns = [
    path('castings/', views.castings_list),
    path('castings/<int:id>/', views.casting_details),
    path("castings/<int:id>/positions/", views.casting_positions),
    # path("castings/<int:id>/positions/<int:pk>/", views.PositionDetailAPIView.as_view()),
    path("positions/", views.PositionList.as_view()),
    path('positions/<int:pk>/', views.Position.as_view()),
    path('ads/', views.AdListAPIView.as_view()),
    path('applicantions/', views.appToPos),
    path('forms', views.form_list),

]

