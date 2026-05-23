# from django.urls import path
# from . import views_api

# urlpatterns = [
#     # PETS
#     path('pets/', views_api.PetListCreateAPIView.as_view(), name='api-pets'),
#     path('pets/<int:pk>/', views_api.PetDetailAPIView.as_view(), name='api-pet-detail'),
#     path('pets/search/', views_api.PetSearchAPIView.as_view(), name='api-pet-search'),

#     # BRANCHES
#     path('branches/', views_api.BranchListCreateAPIView.as_view(), name='api-branches'),
#     path('branches/<int:pk>/', views_api.BranchDetailAPIView.as_view(), name='api-branch-detail'),

#     # FAVORITES
#     path('favorites/', views_api.FavoriteAPIView.as_view(), name='api-favorites'),
# ]


from django.urls import path
from . import views_api

urlpatterns = [

    # PETS API
    path('pets/', views_api.PetListCreateAPIView.as_view(), name='api-pets'),
    path('pets/<int:pk>/', views_api.PetDetailAPIView.as_view(), name='api-pet-detail'),

    # Adoption search (ONLY shelter pets)
    path('pets/adoption-search/', views_api.PetAdoptionSearchAPIView.as_view(), name='api-adoption-search'),
    # Lost & Found search (ONLY lost/found pets)
    path('pets/search/', views_api.PetSearchAPIView.as_view(), name='api-pet-search'),
      

    # BRANCH API
    path('branches/', views_api.BranchListCreateAPIView.as_view(), name='api-branches'),
    # path('branches/<int:pk>/', views_api.BranchDetailAPIView.as_view(), name='api-branch-detail'),

    # FAVORITES API
    path('favorites/', views_api.FavoriteAPIView.as_view(), name='api-favorites'),
]