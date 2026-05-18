from django.urls import path
from . import views_api

urlpatterns = [
    # PETS
    path('pets/', views_api.PetListCreateAPIView.as_view(), name='api-pets'),
    path('pets/<int:pk>/', views_api.PetDetailAPIView.as_view(), name='api-pet-detail'),
    path('pets/search/', views_api.PetSearchAPIView.as_view(), name='api-pet-search'),

    # BRANCHES
    path('branches/', views_api.BranchListCreateAPIView.as_view(), name='api-branches'),
    path('branches/<int:pk>/', views_api.BranchDetailAPIView.as_view(), name='api-branch-detail'),

    # FAVORITES
    path('favorites/', views_api.FavoriteAPIView.as_view(), name='api-favorites'),
]