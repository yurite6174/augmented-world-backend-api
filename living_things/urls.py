from django.urls import path, include
from rest_framework.routers import DefaultRouter

from living_things.views import (
    LivingThingsEachList,
    LivingThingsEachDetail,
    LivingThingsEachCreate,
    LivingThingsHabitatList,
    LivingThingsHabitatDetail,
    LivingThingsHabitatCreate,
    LivingThingsSpecieList,
    LivingThingsSpecieDetail,
    LivingThingsSpecieCreate,
    LivingThingsCountryList,
    LivingThingsCountryDetail,
    LivingThingsCountryCreate,
)

urlpatterns = [
    path(
        "each/",
        LivingThingsEachList.as_view(),
        name="living-things-each-list",
    ),
    path(
        "each/<slug:slug>/",
        LivingThingsEachDetail.as_view(),
        name="living-things-each-detail",
    ),
    path(
        "each/create/",
        LivingThingsEachCreate.as_view(),
        name="living-things-each-create",
    ),
    path(
        "habitats/",
        LivingThingsHabitatList.as_view(),
        name="living-things-habitat-list",
    ),
    path(
        "habitats/<slug:slug>/",
        LivingThingsHabitatDetail.as_view(),
        name="living-things-habitat-detail",
    ),
    path(
        "habitats/create/",
        LivingThingsHabitatCreate.as_view(),
        name="living-things-habitat-create",
    ),
    path(
        "species/",
        LivingThingsSpecieList.as_view(),
        name="living-things-specie-list",
    ),
    path(
        "species/<slug:slug>/",
        LivingThingsSpecieDetail.as_view(),
        name="living-things-specie-detail",
    ),
    path(
        "species/create/",
        LivingThingsSpecieCreate.as_view(),
        name="living-things-specie-create",
    ),
    path(
        "countries/",
        LivingThingsCountryList.as_view(),
        name="living-things-country-list",
    ),
    path(
        "country/<slug:slug>/",
        LivingThingsCountryDetail.as_view(),
        name="living-things-country-detail",
    ),
    path(
        "country/create/",
        LivingThingsCountryCreate.as_view(),
        name="living-things-country-create",
    ),
]
