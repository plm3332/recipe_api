from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeView, UserView

router = DefaultRouter()
router.register('recipes', RecipeView)
router.register('users', UserView)

urlpatterns = [
    path("", include(router.urls)),
]
