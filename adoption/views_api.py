#PetListCreateAPIView(generics.ListCreateAPIView)
#PetDetailAPIView(generics.RetrieveUpdateDestroyAPIView)
#BranchListCreateAPIView(generics.ListCreateAPIView)
#FavoriteAPIView(generics.ListCreateAPIView)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from .models import Pet, Branch, Favorite
from .serializers import PetSerializer, BranchSerializer, FavoriteSerializer
from django.db.models import Q
from django.views import View

from django.http import HttpResponseForbidden
from .utils import get_user_role
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponseForbidden
from .forms import PetForm


# ───────── PETS ─────────
class PetListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()

        species = self.request.query_params.get("species")
        if species:
            queryset = queryset.filter(species=species)

        gender = self.request.query_params.get("gender")
        if gender:
            queryset = queryset.filter(gender=gender)

        return queryset


# class PetCreateAPIView(LoginRequiredMixin, CreateView):
#     model = Pet
#     fields = "__all__"
#     template_name = "adoption/pet_form.html"
#     success_url = reverse_lazy("pet-list")


#     def dispatch(self, request, *args, **kwargs):
#         role = get_user_role(request.user)

#         if role not in ["admin", "staff"]:
#             return HttpResponseForbidden("You are not allowed")

#         return super().dispatch(request, *args, **kwargs)
    


class PetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


# for lost/found page
class PetSearchAPIView(View):

    def get(self, request):
        query = request.GET.get("q", "")

        pets = Pet.objects.filter(
            Q(name__icontains=query)
            | Q(species__icontains=query)
            | Q(breed__icontains=query)
            | Q(location__icontains=query)
            | Q(gender__icontains=query)
            | Q(pet_status__icontains=query)
        ).filter(pet_status__in=["lost", "found"])

        return render(request, "adoption/partials/lost_pet_table.html", {"pets": pets})


# for adoption page
class PetAdoptionSearchAPIView(View):

    def get(self, request):
        query = request.GET.get("q", "")

        pets = Pet.objects.filter(
            Q(name__icontains=query)
            | Q(species__icontains=query)
            | Q(breed__icontains=query)
            | Q(location__icontains=query)
            | Q(gender__icontains=query)
            | Q(pet_status__icontains=query)
        ).filter(pet_status="shelter")

        return render(request, "adoption/partials/pet_table.html", {"pets": pets})
    

# ───────── BRANCHES ─────────
class BranchListCreateAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Branch.objects.all()
#     serializer_class = BranchSerializer


# ───────── FAVORITES ─────────
class FavoriteAPIView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
