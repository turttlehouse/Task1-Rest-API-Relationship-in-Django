from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from .models import Category, Notes
from .serializers import CategorySerializer, NotesSerializer
from rest_framework import status



# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    def list(self,request):
        AllCategory = Category.objects.all()
        serializer = CategorySerializer(AllCategory,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id= pk
        if id is not None:
            category = Category.objects.get(id=id)
            serializer = CategorySerializer(category)
            return Response(serializer.data)
    
    def create(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"New Category Added"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id=pk   
        category = Category.objects.get(pk=id)
        serializer = CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"all data of Category Updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        category = Category.objects.get(pk=id)
        serializer = CategorySerializer(category,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"partial data of category updated"})
        return Response(serializer.errors)
        
    
    def destroy(self, request,pk):
        id=pk
        AllCategory = Category.objects.get(pk=id)
        AllCategory.delete()
        return Response({'message':'category deleted'})

# class NotesViewSet(viewsets.ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_class = NotesSerializer

class NotesViewSet(viewsets.ViewSet):
    def list(self,request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes,many =True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            note = Notes.objects.get(id=id)
            serializer = NotesSerializer(note)
            return Response(serializer.data)
        
    
    def create(self,request):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Notes successfully created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        id = pk
        note = Notes.objects.get(pk=id)
        note.delete()
        return Response({"message":"Note successfully deleted"})
    
    def update(self,request,pk):
        id =pk
        note = Notes.objects.get(pk=id)
        serializer = NotesSerializer(note,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"All notes updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    
    def partial_update(self,request,pk):
        id= pk
        note = Notes.objects.get(pk=id)
        serializer = NotesSerializer(note,data=request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"notes data partially updated"})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        



