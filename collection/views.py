
#This Django code snippet uses Django REST Framework (DRF) and SimpleJWT to implement a user registration API that
#  creates a user and generates a JWT token for authentication.



from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Collection
from collections import Counter
from django.core.cache import cache
    

from django.core.paginator import Paginator
from django.http import JsonResponse
import requests
import os
from django.views import View
import os
import requests
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
from django.views import View

from django.views import View

from .serializers import CollectionSerializer
import os
import requests
from django.http import JsonResponse


class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already taken'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            'access_token': str(refresh.access_token),
        })
    #///movie list
    





def movielistview(request):
    url = 'https://demo.credy.in/api/v1/maya/movies/'
    MOVIE_API_USER = 'iNd3jDMYRKsN1pjQPMRz2nrq7N99q4Tsp9EY9cM0'
    MOVIE_API_PASS = 'Ne5DoTQt7p8qrgkPdtenTK8zd6MorcCR5vXZIJNfJwvfafZfcOs4reyasVYddTyXCz9hcL5FGGIVxw3q02ibnBLhblivqQTp4BIC93LZHj4OppuHQUzwugcYu7TIC5H1'
    max_retries = 3  # Number of retries
    
    for attempt in range(max_retries):
        try:
            # Disable SSL verification
            response = requests.get(url, auth=HTTPBasicAuth(MOVIE_API_USER, MOVIE_API_PASS), timeout=5, verify=False)
            response.raise_for_status()  # Check for HTTP errors
            return JsonResponse(response.json())  # Return the JSON response
        except requests.exceptions.RequestException as e:
            if attempt == max_retries - 1:  # Last attempt
                return JsonResponse({'error': str(e)}, status=500) 

#/////api for creating collection api/////
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_collection(request):
    #re, a CollectionSerializer instance is created, which is responsible for converting the 
    # incoming JSON data (in request.data) into a valid Collection model instance.
#The data=request.data part passes the incoming POST data (like the title, description, and movies) into the serializer for validation and deserialization.

    serializer=CollectionSerializer(data=request.data)
    if serializer.is_valid():
        collection=serializer.save(user=request.user)
        return Response({"collection_uuid":collection.uuid},status=201)
    else:
        return Response(serializer.errors,status=400)

#////api for viewing collection/////
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_collections(request):
    ct=Collection.objects.filter(user=request.user)
    st=CollectionSerializer(ct,many=True)
    all_genre=[]
    for i in ct:
        for j in i.movies.all():
            all_genre.extend(j.genre.split(","))
            genre_count = Counter(all_genre)
            favorite_genres = ", ".join([genre for genre, _ in genre_count.most_common(3)])

    return Response({
        "is_success":True,
        "ct":st.data,
        "favourite_genres":favorite_genres
    })


#///modifying api////
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_collection(request,collection_uuid):
    #retrieving the info
    try:
        collection=Collection.objects.get(user=request.user,uuid=collection_uuid)
    except:
        return Response("error",status=404)
    serializer=CollectionSerializer(collection,data=request.data,partial=True)    
    if serializer.is_valid():
        serializer.save()
        return  Response({"message":"collection updated successfully"})
    return Response(serializer.errors,status=400)

#deleting the collection
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_collection(request,collection_uuid):
    try:
        collection=Collection.objects.get(user=request.user,uuid=collection_uuid)
        collection.delete()
        return Response({"message":"deleted successfully"})
    except:
        return Response({"message":"data didnt exist"},status=404)
    

#views to request and reset the count in the middleware
def get_count(request):
     request_count = cache.get('request_count', 0)
     return JsonResponse({'request_count': request_count})


def reset_count(request):
    cache.set('req_count', 0)
    return JsonResponse({'message': 'Request counter reset successfully'})
  
         
