from rest_framework import serializers
from .models import LivingThings, Habitat, Species
from general.serializers import TagSerializer, GenreSerializer, ArticleSerializer


class LivingThingsSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = LivingThings
        fields = "__all__"


class HabitatSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Habitat
        fields = "__all__"


class SpeciesSerializer(serializers.ModelSerializer):
    article = ArticleSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Species
        fields = "__all__"
