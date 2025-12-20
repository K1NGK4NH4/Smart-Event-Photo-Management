from django.shortcuts import render
from apps.photo.models import Photo,Like
from accounts.models import User
from rest_framework.views import APIView
from .serializers import PhotoLikeSerializer
from rest_framework.response import Response
from django.db import transaction,IntegrityError
from rest_framework import generics
from apps.photo.serializers import PhotoListSerializer
# Create your views here.

#add like 
class LikeAdd(APIView):
    def post(self,request,*args,**kwargs):
        serializer = PhotoLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        photo = serializer.validated_data.get("photo_id")  
        user = self.request.user 
        try:
            with transaction.atomic():
                photo.liked_users.add(user)
        except IntegrityError:
            return Response(
                {"message": "Already liked"},
                status=400
            )
        # print(user,photo)
        return Response({
            "message":"You Liked the photo"
        })

add_like = LikeAdd.as_view()
# remove like

class RemoveLike(APIView):
    def delete(self,request,*args,**kwargs):
        serializer = PhotoLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        photo = serializer.validated_data.get("photo_id")  
        user = self.request.user
        if photo.liked_users.filter(email=user.email).exists() :
            photo.liked_users.remove(user)
        return Response({
            "message":"Like Removed"
        })

remove_like = RemoveLike.as_view()


#all below are only allowed to members
#add photo to my favourites 
class AddToFavourite(APIView):
    def post(self,request,*args,**kwargs):
        serializer = PhotoLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        photo = serializer.validated_data.get("photo_id")  
        user = self.request.user 
        try:
            with transaction.atomic():
                photo.is_favourite_of.add(user)
        except IntegrityError:
            return Response(
                {"message": "Already added to Favourites"},
                status=400
            )
        return Response({
            "message":"You added the photo to your favourites"
        })

add_favourite = AddToFavourite.as_view()

# Remove Photo from my favourites 
class RemoveFavourite(APIView):
    def delete(self,request,*args,**kwargs):
        serializer = PhotoLikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        photo = serializer.validated_data.get("photo_id")  
        user = self.request.user
        if photo.liked_users.filter(email=user.email).exists() :
            photo.is_favourite_of.remove(user)
        return Response({
                "message":"Removed from your Favourite List"
            })

remove_favourite = RemoveFavourite.as_view()

# Favourite Photo List give only thumbnail and id 
class ListFavouritePhotos(generics.ListAPIView):
    def get_queryset(self):
        return Photo.objects.filter(is_favourite_of=self.request.user)
    serializer_class = PhotoListSerializer
    
list_favourites = ListFavouritePhotos.as_view()

# Tagged In Photo List
class ListTaggedInPhotos(generics.ListAPIView):
    def get_queryset(self):
        return Photo.objects.filter(tagged_user=self.request.user)
    serializer_class = PhotoListSerializer
    
list_tagged_in = ListTaggedInPhotos.as_view()

#Download a photo means Download to the particular folder of your system have to make an download table for this to track total download of a photo


#Share a Photo absolute URL means want to share url of that photo 
#(Frontend copy the url in frontend)