from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'results', views.FlamesResultViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('calculate/', views.calculate_flames, name='calculate-flames'),
    path('history/', views.get_results_history, name='results-history'),
]
