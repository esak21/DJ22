from curses import meta
from unittest.util import _MAX_LENGTH
from rest_framework import serializers

from profiles import models 

class HelloSerializer(serializers.Serializer):
    """     Serialize the Name Field for Testing APIView """
    name = serializers.CharField(max_length=10)



class UserProfileSerializer(serializers.ModelSerializer):
    """ Model Serializer """

    # we are using meta class to configure the serializer to point to a specific model 

    class Meta:
        # define the models 
        model = models.UserProfile
        # list of fields we want to use in the API 
        fields = ('id', 'email', 'name', 'password')
        # Since password is more sensitive , we only want to use it when we create the new User 
        # while retrieve a user it wont be needed 
        extra_kwargs = {
            'password' : {
                'write_only': True, 
                'style': {
                    'input_type': 'password'
                } 
            }
        }

        # override the Function 

        def create(self, validated_data):
            """ Create and Return a new User """
            user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password = validated_data['password'],
            )

            return user 

        def update(self, instance, validated_data):
            """Handle updating user account"""
            if 'password' in validated_data:
                password = validated_data.pop('password')
                instance.set_password(password)

            return super().update(instance, validated_data)



class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ Serialize the Profile Feed Items """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only': True
            }
        }