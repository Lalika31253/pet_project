from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

from django.forms import modelformset_factory
from .models import City, Branch, Pet, PetImage

from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect

from .models import Branch, Pet, Favorite, PetImage, City

from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework import generics

from django.views.generic import ListView
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.views import View
from django.shortcuts import render, redirect
from .forms import PetForm, CustomRegisterForm, LostPetForm



from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from .utils import get_user_role

from django.forms import modelformset_factory

from django.template.loader import render_to_string

from .models import PetImage
from .forms import PetForm, PetImageForm


User = get_user_model()

# ─────────────────────────────
# AUTHENTICATION
# ─────────────────────────────
# class RegisterView(View):

#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, "adoption/auth/register.html", {"form": form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("login")

#         return render(request, "adoption/auth/register.html", {"form": form})

class RegisterView(View):

    def get(self, request):
        form = CustomRegisterForm()
        return render(request, "adoption/auth/register.html", {"form": form})

    def post(self, request):
        form = CustomRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        return render(request, "adoption/auth/register.html", {"form": form})


class LandingView(TemplateView):
    template_name = "adoption/landing.html"


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



# ─────────────────────────────
# PETS
# ─────────────────────────────
class PetListView(ListView):
    model = Pet
    template_name = "adoption/pet_list.html"
    context_object_name = "pets"

    def get_queryset(self):
        return Pet.objects.filter(pet_status="shelter")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cities"] = City.objects.all() 
        if self.request.user.is_authenticated:
            favorites = Favorite.objects.filter(user=self.request.user).values_list("pet_id", flat=True)
            context["favorite_ids"] = set(favorites)
        else:
            context["favorite_ids"] = set()

        return context
    
def pet_list(request):
    pets = Pet.objects.all()

    favorite_ids = []
    if request.user.is_authenticated:
        favorite_ids = Favorite.objects.filter(
            user=request.user
        ).values_list('pet_id', flat=True)

    return render(request, 'adoption/pet_list.html', {
        'pets': pets,
        'favorite_ids': favorite_ids,
    })


class LostPetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = "adoption/lost_pet_form.html"
    success_url = reverse_lazy("lost-pets")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        PetImageFormSet = modelformset_factory(
            PetImage,
            fields=("image",),
            extra=3,
            can_delete=False
        )

        if self.request.POST:
            context["formset"] = PetImageFormSet(
                self.request.POST,
                self.request.FILES,
                queryset=PetImage.objects.none()
            )
        else:
            context["formset"] = PetImageFormSet(queryset=PetImage.objects.none())

        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context["formset"]

        self.object = form.save()

        if formset.is_valid():
            for f in formset:
                if f.cleaned_data:
                    img = f.save(commit=False)
                    img.pet = self.object
                    img.save()

        return super().form_valid(form)
    


class LostPetsView(ListView):
    model = Pet
    template_name = "adoption/lost_pets.html"
    context_object_name = "pets"

    def get_queryset(self):
        return Pet.objects.filter(pet_status__in=["lost", "found"]).order_by("-id")


class LostPetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = LostPetForm
    template_name = "adoption/lost_pet_form.html"
    success_url = reverse_lazy("lost-pets")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # only owner can edit
        if obj.created_by != request.user:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)


class LostPetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = "adoption/pet_confirm_delete.html"
    success_url = reverse_lazy("lost-pets")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        # ONLY owner can delete
        if obj.created_by != request.user:
            return HttpResponseForbidden()

        return super().dispatch(request, *args, **kwargs)


class LostPetDetailView(DetailView):
    model = Pet
    template_name = "adoption/lost_pet_detail.html"
    context_object_name = "pet"

class PetDetailView(DetailView):
    model = Pet
    template_name = "adoption/pet_detail.html"
    context_object_name = "pet"


class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = "adoption/pet_form.html"
    success_url = reverse_lazy("pet-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        PetImageFormSet = modelformset_factory(
            PetImage,
            fields=("image",),
            extra=3
        )

        if self.request.POST:
            context["formset"] = PetImageFormSet(
                self.request.POST,
                self.request.FILES,
                queryset=PetImage.objects.none()
            )
        else:
            context["formset"] = PetImageFormSet(
                queryset=PetImage.objects.none()
            )

        return context

    def form_valid(self, form):

        context = self.get_context_data()
        formset = context["formset"]

        # SAVE PET
        self.object = form.save()

        # SAVE IMAGES
        if formset.is_valid():

            for f in formset:

                if f.cleaned_data:

                    image = f.save(commit=False)
                    image.pet = self.object
                    image.save()

        return redirect(self.success_url)


def cities_by_province(request):
    province = request.GET.get("province")

    cities = City.objects.filter(province=province)

    html = render_to_string(
        "adoption/city_options.html",
        {"cities": cities}
    )
    return HttpResponse(html)



class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = "adoption/pet_form.html"
    success_url = reverse_lazy("pet-list")

    def dispatch(self, request, *args, **kwargs):
        role = get_user_role(request.user)

        if not request.user.is_superuser and role != "shelter":
            return HttpResponseForbidden("Only shelter staff can update pets.")

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        PetImageFormSet = modelformset_factory(
            PetImage,
            fields=("image",),
            extra=3,
            can_delete=True
        )

        if self.request.POST:
            context["formset"] = PetImageFormSet(
                self.request.POST,
                self.request.FILES,
                queryset=PetImage.objects.filter(pet=self.object)
            )
        else:
            context["formset"] = PetImageFormSet(
                queryset=PetImage.objects.filter(pet=self.object)
            )

        return context

    def form_valid(self, form):
        self.object = form.save()

        context = self.get_context_data()
        formset = context["formset"]

        if formset.is_valid():
            images = formset.save(commit=False)

            for img in images:
                img.pet = self.object
                img.save()

            for obj in formset.deleted_objects:
                obj.delete()

        return super().form_valid(form)



class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = "adoption/pet_confirm_delete.html"
    success_url = reverse_lazy("pet-list")



# # class PetUpdateView(LoginRequiredMixin, UpdateView):
# #     model = Pet
# #     fields = "__all__"
# #     template_name = "adoption/pet_form.html"
# #     success_url = reverse_lazy("pet-list")


class LostPetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = "adoption/pet_confirm_delete.html"
    success_url = reverse_lazy("lost-pets")



class ProvincePetsView(ListView):
    model = Pet
    template_name = "adoption/province_pets.html"
    context_object_name = "pets"

    def get_queryset(self):
        province = self.kwargs["province"]

        return Pet.objects.filter(
            branch__province=province,
            adoption_status="available"
        )

def province_pets(request, province):
    pets = Pet.objects.filter(
        branch__city__province__code=province,
        adoption_status="available"
    )

    return render(request, "adoption/province_pets.html", {
        "pets": pets,
        "province": province
    })





class CustomLoginView(LoginView):
    template_name = "adoption/auth/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)

        # HTMX login
        if self.request.headers.get("HX-Request"):
            return HttpResponse(status=204, headers={"HX-Redirect": reverse("landing")})

        return response

    def get_success_url(self):
        return reverse("landing")


# ─────────────────────────────
# FAVORITES
# ─────────────────────────────
@login_required
def toggle_favorite(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        pet=pet
    )

    if not created:
        favorite.delete()

    return redirect(request.META.get("HTTP_REFERER", "lost-pets"))
# # ─────────────────────────────
# # ADOPTION APPLICATIONS (optional but recommended)
# # ─────────────────────────────
# class AdoptionApplicationListView(LoginRequiredMixin, ListView):
#     model = AdoptionApplication
#     template_name = "adoption/application_list.html"
#     context_object_name = "applications"

#     def get_queryset(self):
#       return AdoptionApplication.objects.select_related("user", "pet")


@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "adoption/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        role = get_user_role(user)

        favorites = Favorite.objects.filter(user=user).select_related("pet")

        created_pets = Pet.objects.filter(created_by=user)

        context.update({
            "role": role,
            "favorites": favorites,
            "created_pets": created_pets,
        })

        return context
    
    
@login_required
def toggle_adoption_status(request, pk):
    pet = get_object_or_404(Pet, pk=pk)

    role = get_user_role(request.user)

    if not (request.user.is_superuser or role == "shelter"):
        return HttpResponseForbidden("Not allowed")

    # TOGGLE LOGIC
    if pet.adoption_status == "available":
        pet.adoption_status = "pending"
    elif pet.adoption_status == "pending":
        pet.adoption_status = "adopted"
    else:
        pet.adoption_status = "available"

    pet.save()
    return redirect("pet-list")


def pet_create(request):

    ImageFormSet = modelformset_factory(PetImage, form=PetImageForm, extra=3)

    if request.method == "POST":
        form = PetForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PetImage.objects.none())

        if form.is_valid() and formset.is_valid():
            pet = form.save()

            for f in formset:
                if f.cleaned_data:
                    img = f.save(commit=False)
                    img.pet = pet
                    img.save()

    else:
        form = PetForm()
        formset = ImageFormSet(queryset=PetImage.objects.none())

    return render(request, "adoption/pet_form.html", {
        "form": form,
        "formset": formset
    })