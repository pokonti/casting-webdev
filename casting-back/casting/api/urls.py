from django.contrib import admin
from django.urls import path
from .views import *
import api.views as views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('castings/', views.castings_list),
    path('castings/<int:id>/', views.casting_details),
    path("castings/<int:id>/positions/", views.CastingPositionsView.as_view()),
    # path("castings/<int:id>/positions/<int:pk>/", views.PositionDetailAPIView.as_view()),
    path("positions/", views.PositionList.as_view()),
    path('positions/<int:pk>/', views.Position.as_view()),
    path('ads/', views.AdListAPIView.as_view()),
    path('applicantions/', views.appToPos),
    path('forms/', views.FormList.as_view()),
    path('forms/<int:id>', views.form_details),
    path('profile/', UserProfileView.as_view()),

]

