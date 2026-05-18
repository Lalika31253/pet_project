from rest_framework import generics
from .models import Pet, Branch, Favorite
from .serializers import PetSerializer, BranchSerializer, FavoriteSerializer


# ───────── PETS ─────────
class PetListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        queryset = Pet.objects.all()

        species = self.request.query_params.get('species')
        if species:
            queryset = queryset.filter(species=species)

        gender = self.request.query_params.get('gender')
        if gender:
            queryset = queryset.filter(gender=gender)

        return queryset


class PetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetSearchAPIView(generics.ListAPIView):
    serializer_class = PetSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q")
        if query:
            return Pet.objects.filter(name__icontains=query)
        return Pet.objects.all()


# ───────── BRANCHES ─────────
class BranchListCreateAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# ───────── FAVORITES ─────────
class FavoriteAPIView(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer