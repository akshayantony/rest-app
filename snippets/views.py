from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from snippets.models import Heroes
from snippets.serializers import HeroesSerializer,UserSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import Http404
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import generics,permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Heroes.objects.all()
    serializer_class = HeroesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class SearchList(generics.ListAPIView):
    serializer_class = HeroesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
       return Heroes.objects.filter(name__contains=self.kwargs['name'])


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


#
# class Hero_detail(APIView):
#
#     def get_object(self,pk):
#         try:
#             heroes = Heroes.objects.get(pk=pk)
#         except Heroes.DoesNotExist:
#             raise Http404
#
#     def get(self,request,pk,format=None):
#         heroes=self.get_object(pk)
#         serializer = HeroesSerializer(heroes)
#         return Response(serializer.data)
#
#     def put(self,request,pk,format=None):
#         heroes=self.get_object(pk)
#         serializer = HeroesSerializer(heroes, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,pk,format=None):
#         heroes=self.get_object(pk)
#         heroes.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)
