from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import PetListCreateAPIView, PetDetailAPIView, PetSearchAPIView 

urlpatterns = [

    # ── Public ────────────────────────────────────────────────────────────
    path('', views.LandingView.as_view(), name='landing'),
    path('about', views.AboutView.as_view(), name='about'),
    path('help', views.HelpView.as_view(), name='help'),

    # ── Auth ──────────────────────────────────────────────────────────────
    path('login/',
         LoginView.as_view(template_name='adoption/auth/login.html'),
         name='login'),
    path('logout/',  LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # ── Branches ──────────────────────────────────────────────────────────
    # path('branches/',                   views.BranchListView.as_view(),   name='branch-list'),
    # path('branches/<int:pk>/',          views.BranchDetailView.as_view(), name='branch-detail'),
    path('', views.LandingView.as_view(), name='landing'),

    path('branches/',                     views.BranchListView.as_view(),    name='branch-list'),
    path('branches/<int:pk>/',            views.BranchDetailAPIView.as_view(),  name='branch-detail'),


    # ── Pets ──────────────────────────────────────────────────────────────
    # path('pets/',                        views.PetListView.as_view(),          name='pet-list'),
    # path('pets/<int:pk>/',               views.PetDetailView.as_view(),        name='pet-detail'),
    # path('pets/add/',                    views.PetCreateView.as_view(),        name='pet-create'),
    # path('pets/search/',                 views.PetSearchView.as_view(),        name='pet-search'),
    # path('pets/<int:pk>/edit/',          views.PetUpdateView.as_view(),        name='pet-update'),
    # path('pets/<int:pk>/delete/',        views.PetDeleteView.as_view(),        name='pet-delete'),
    # path('pets/<int:pk>/inline-delete/', views.PetInlineDeleteView.as_view(),  name='pet-inline-delete'),

    path('api/pets/',                   PetListCreateAPIView.as_view(),     name='pet-list'),
    path('api/pets/<int:pk>/',          PetDetailAPIView.as_view(),         name='pet-detail'),
    path('api/search/',                 PetSearchAPIView.as_view(),      name='api-pet-detail'),

    # ── Users ───────────────────────────────────────────────────────────
    path('users/',                       views.UserListView.as_view(),   name='user-list'),
    path('users/add/',                   views.UserCreateView.as_view(), name='user-create'),
    path('users/search/',                views.UserSearchView.as_view(), name='user-search'),
    path('users/<int:pk>/',              views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/edit/',         views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/',       views.UserDeleteView.as_view(), name='user-delete'),

    # ── Favorites ──────────────────────────────────────────────────────────
    # path('favorites/',                   views.FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/',                   views.FavoriteAPIView.as_view(), name='api-favorite-list'),

]