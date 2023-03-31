from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drugs.views import DrugViewSet

router = DefaultRouter()
router.register(r'drugs', DrugViewSet, basename='drug')

urlpatterns = router.urls
