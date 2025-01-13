from rest_framework import serializers
from .models import Tag, Note, Folder, User, Application
from rest_framework.serializers import CurrentUserDefault


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'title', 'notes')

class NoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'tags', 'created_at', 'modified_at')


    
class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id', 'title', 'parent_folder', 'notes')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name')

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'application_type', 'application_file')

