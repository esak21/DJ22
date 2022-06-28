from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from yaml import serialize
from profiles.serializers import  HelloSerializer, ProfileFeedItemSerializer, UserProfileSerializer

from rest_framework import viewsets

from profiles.models import ProfileFeedItem, UserProfile

from rest_framework.authentication import TokenAuthentication
from profiles import permissions
from rest_framework import filters 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

class HelloApiView(APIView):
    """ Test API VIEW """
    # we are assigning serializer class 
    serializer_class = HelloSerializer

    def get(self,request, format=None):
        """ Returns the List of APIVIEW Features"""
        an_api_view = [
            'uses HTTP Methods as Functions get put patch delete post',
            'is similiar to a django view ',
            'gives u the most control to logic',
            'it mapped manually to te URLS'
        ]

        return Response({"message": 'Hello', 'data': an_api_view})

    
    def post(self, request):
        """ Create a message with Name """

        # retrieve the serializer and pass in the data that was send in the request 
        # send the request data to the serializer class , it converts them back to the python Objects
        serializer = self.serializer_class(data=request.data)

        # valid this serializers 
        if serializer.is_valid():
            # get the Column name from the validated data
            name = serializer.validated_data.get('name')

            message = f"Hello {name} welcome to HELLLLLLLLLL"
            return Response({"data": message})
        # if the data is not valid 
        # then return a bad http statu code 
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """ Handle Updating Object """
        # replace the Object with the Object Provided by the user 
        # if first and last name are available 
        # user provided only last name, then first name will be deleted and we only had the last name 
        return Response({"data": "Method is PUTTTTTT"})

    
    def patch(self, request, pk=None):
        """ Handle Updating Object """
        # it will handle the partial update
        # Only update the Fields Provided 
        # if first and last name are available 
        # user provided only last name, Last Name alone updated , first name will be available as it is 
        return Response({"data": "Method is patch"})


    
    def delete(self, request, pk=None):
        """ Handle Updating Object """
        # delete the Objects 
        return Response({"data": "Method is delete"})



class HelloViewSets(viewsets.ViewSet):
    """ Creating ViewSets """

    serializer_class = HelloSerializer

    def list(self, request):
        """ Return a hello Message""" 
        a_viewset = [
            'Uses action list create retrieve partialupdate ',
            'Automatically mappes to URL using routers',
            'provides more functinality using simple code'
        ]

        return Response( { "message": "hello" , "data": a_viewset })

    def create(self, request):
        """ REturn a Name """

        serializervalue = self.serializer_class(data = request.data)
        if serializervalue.is_valid():
            name = serializervalue.validated_data.get('name')
            message = f"Hello {name}"

            return Response({"message": message})
        
        return Response(serializervalue.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """ Retrieve a Single Object by Id  """
        return Response ({"message": "HTTP Method GET"})

    def update(self, request, pk=None):
        """ Update  Single Object by Id  """
        return Response ({"message": "HTTP Method PUT"})

    def partial_update(self, request, pk=None):
        """ Update  part of an Single Object by Id  """
        return Response ({"message": "HTTP Method PATCH"})

    def destroy(self, request, pk=None):
        """ delete Single Object by Id  """
        return Response ({"message": "HTTP Method DELETE"})



class UserProfileViewSets(viewsets.ModelViewSet):
    """ Handle creating and Updating Profiles """

    serializer_class = UserProfileSerializer

    queryset = UserProfile.objects.all()
    # it will create tokens when user logged in 
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateProfile,)
    # we are adding the DRF Filter Backend and search Feature
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """ Handle user authentication Token """
    # To make it visible in Browser API 
    # 
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Jandle Creating and updating Profile Feed """

    serializer_class = ProfileFeedItemSerializer
    queryset = ProfileFeedItem.objects.all()

    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticatedOrReadOnly, IsAuthenticated)

    # When a new Object is created DRF will call the perform_create Method 
    # serializer is a Model Serializer and it has the saev method which save the serializer to the database 
    # 
    def perform_create(self, serializer):
        """Sets the user profile to loged in user  """
        serializer.save(user_profile=self.request.user)