from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from .models import Branch, Pet, User, Favorite, AdoptionApplication

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegisterForm

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics

from django.views.generic import ListView



# ─────────────────────────────
# AUTHENTICATION
# ─────────────────────────────
class RegisterView(CreateView):
    form_class    = RegisterForm
    template_name = 'adoption/auth/register.html'
    success_url   = reverse_lazy('branch-list')

    def form_valid(self, form):
        # Save the user, then log them in immediately
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

class LandingView(TemplateView):
    template_name = 'adoption/landing.html'

class AboutView(TemplateView):
    template_name = "adoption/about.html"

class HelpView(TemplateView):
    template_name = "adoption/help.html"


# ─────────────────────────────
# BRANCHES
# ─────────────────────────────
class BranchListView(ListView):
    model = Branch
    template_name = "adoption/branch_list.html"
    context_object_name = "branches"


# # # class BranchDetailView(DetailView):
# # #     model = Branch
# # #     template_name = "adoption/branch_detail.html"
# # #     context_object_name = "branch"
    
# # class BranchListCreateAPIView(generics.ListCreateAPIView):
# #     queryset = Branch.objects.all()
# #     serializer_class = BranchSerializer


# # class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Branch.objects.all()
# #     serializer_class = BranchSerializer


# ─────────────────────────────
# PETS
# ─────────────────────────────
class PetListView(ListView):
    model = Pet
    template_name = "adoption/pet_list.html"
    context_object_name = "pets"

    def get_queryset(self):
        return Pet.objects.filter(pet_type='shelter')

class LostPetsView(ListView):
    model = Pet
    template_name = "adoption/lost_pets.html"
    context_object_name = "pets"
    
    def get_queryset(self):
        return Pet.objects.filter(pet_type='lost')

# # class PetDetailView(DetailView):
# #     model = Pet
# #     template_name = "adoption/pet_detail.html"
# #     context_object_name = "pet"


# # class PetCreateView(LoginRequiredMixin, CreateView):
# #     model = Pet
# #     fields = "__all__"
# #     template_name = "adoption/pet_form.html"
# #     success_url = reverse_lazy("pet-list")
    

# # class PetUpdateView(LoginRequiredMixin, UpdateView):
# #     model = Pet
# #     fields = "__all__"
# #     template_name = "adoption/pet_form.html"
# #     success_url = reverse_lazy("pet-list")


# # class PetDeleteView(LoginRequiredMixin, DeleteView):
# #     model = Pet
# #     template_name = "adoption/pet_confirm_delete.html"
# #     success_url = reverse_lazy("pet-list")


# # class PetSearchView(ListView):
# #     model = Pet
# #     template_name = "adoption/pet_list.html"
# #     context_object_name = "pets"

# #     def get_queryset(self):
# #         query = self.request.GET.get("q")
# #         if query:
# #             return Pet.objects.filter(name__icontains=query)
# #         return Pet.objects.all()


# # class PetInlineDeleteView(LoginRequiredMixin, DeleteView):
# #     model = Pet
# #     template_name = "adoption/pet_confirm_delete.html"
# #     success_url = reverse_lazy("pet-list")




# ─────────────────────────────
# USERS
# ─────────────────────────────
class UserListView(LoginRequiredMixin,ListView):
    model = User
    template_name = "adoption/user_list.html"
    context_object_name = "users"


# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     template_name = "adoption/user_detail.html"
#     context_object_name = "user"


# class UserCreateView(LoginRequiredMixin, CreateView):
#     model = User
#     fields = "__all__"
#     template_name = "adoption/user_form.html"
#     success_url = reverse_lazy("user-list")


# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = "__all__"
#     template_name = "adoption/user_form.html"
#     success_url = reverse_lazy("user-list")


# class UserDeleteView(LoginRequiredMixin, DeleteView):
#     model = User
#     template_name = "adoption/user_confirm_delete.html"
#     success_url = reverse_lazy("user-list")


# class UserSearchView(ListView):
#     model = User
#     template_name = "adoption/user_list.html"
#     context_object_name = "users"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         if query:
#           return User.objects.filter(username__icontains=query) | User.objects.filter(email__icontains=query)
#         return User.objects.all()


# # ─────────────────────────────
# # FAVORITES
# # ─────────────────────────────
# # class FavoriteListView(LoginRequiredMixin, ListView):
# #     model = Favorite
# #     template_name = "adoption/favorite_list.html"
# #     context_object_name = "favorites"

# #     def get_queryset(self):
# #         return Favorite.objects.filter(user=self.request.user).select_related("pet")
    

# # ─────────────────────────────
# # ADOPTION APPLICATIONS (optional but recommended)
# # ─────────────────────────────
# class AdoptionApplicationListView(LoginRequiredMixin, ListView):
#     model = AdoptionApplication
#     template_name = "adoption/application_list.html"
#     context_object_name = "applications"

#     def get_queryset(self):
#       return AdoptionApplication.objects.select_related("user", "pet")

