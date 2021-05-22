from django.urls import path, include
from bboard.views import index, by_rubric, BbCreateView, BbViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', BbViewSet)


urlpatterns = [
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('test_rest_bb', include(router.urls), name='test_rest_bb'),
    path('', index, name='index'),
]
