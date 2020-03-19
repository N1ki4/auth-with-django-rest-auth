from rest_framework import generics

from .serializers import RecipeSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Recipe


class RecipeList(generics.ListCreateAPIView):
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly, )
	queryset = Recipe.objects.all()
	serializer_class = RecipeSerializer
