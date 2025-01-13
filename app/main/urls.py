from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from .views import TagViewSet, NoteViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
# router.register(r'application', views.ApplicationViewSet)
# router.register(r'note', views.NoteViewSet)
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'notes', NoteViewSet, basename='notes')


urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]