# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NotesViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet,basename='Cat')
router.register('notes', NotesViewSet,basename="Allnote")

urlpatterns = [
    path('', include(router.urls)),
]

