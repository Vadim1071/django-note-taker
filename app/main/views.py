from django.shortcuts import render, redirect
from .models import Note, Tag, Folder, Application
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .serializers import NoteSerializer, TagSerializer, FolderSerializer, ApplicationSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework import viewsets, status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import PermissionDenied

import logging

logger = logging.getLogger(__name__)


class RegisterView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            email = request.data.get('email', '')

            if not username or not password:
                logger.warning('Username and password are required')
                return Response(
                    {'error': 'Username and password are required'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if User.objects.filter(username=username).exists():
                logger.warning(f'Username {username} already exists')
                return Response(
                    {'error': 'Username already exists'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = User.objects.create_user(
                username=username, password=password, email=email)
            logger.info(f'User {username} registered successfully')
            return Response(
                {'message': 'User registered successfully'},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logger.error(f'Error during registration: {e}')
            return Response(
                {'error': 'Internal server error'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            raise PermissionDenied(
                "User must be authenticated to perform this action.")


class TagViewSet(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    permission_classes = [IsAuthenticated]


class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f"Creating note for user: {self.request.user}")
        serializer.save(user=self.request.user)

class FolderViewSet(ModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()
    permission_classes = [IsAuthenticated]


def index(request):
    return render(request, "index.html")
