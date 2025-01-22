from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import TagViewSet, NoteViewSet, ApplicationViewSet, FolderViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView

router = DefaultRouter()
router.register(r'tags', TagViewSet, basename='tags')
router.register(r'notes', NoteViewSet, basename='notes')
router.register(r'applications', ApplicationViewSet, basename='applications')
router.register(r'folders', FolderViewSet, basename='folders')

urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
]