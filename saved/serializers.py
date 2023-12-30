from django.db import IntegrityError
from rest_framework import serializers
from saved.models import Saved
from posts.models import Post 

class PostSavedSerializer (serializers.ModelSerializer):
    
    class Meta:
        model =Post
        fields = [
            'id', 'owner','title','image',
        ]
class SavedSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post = PostSavedSerializer(many=False,read_only=True)
    class Meta:
        model = Saved
        fields = ['id', 'created_at', 'owner', 'post']


    # def create(self, validated_data):
    #     try:
    #         print("validatedated data",validated_data)
    #         return super().create(validated_data)
    #     except IntegrityError:
    #         raise serializers.ValidationError({
    #             'detail': 'possible duplicate'
    #         })
