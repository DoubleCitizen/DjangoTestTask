from django.shortcuts import render
from rest_framework import generics

from core import models, serializers


class CarCreateView(generics.CreateAPIView):
    model = models.Car
    serializer_class = serializers.CarSerializer


class CarUpdateView(generics.UpdateAPIView):
    model = models.Car
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


class CarDeleteView(generics.DestroyAPIView):
    model = models.Car
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


class CarView(generics.RetrieveAPIView):
    model = models.Car
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


class CarListView(generics.ListAPIView):
    model = models.Car
    serializer_class = serializers.CarSerializer
    queryset = models.Car.objects.all()


class CommentCreateView(generics.CreateAPIView):
    model = models.Comment
    serializer_class = serializers.CommentSerializer


class CommentUpdateView(generics.UpdateAPIView):
    model = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentDeleteView(generics.DestroyAPIView):
    model = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentView(generics.RetrieveAPIView):
    model = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()


class CommentListView(generics.ListAPIView):
    model = models.Comment
    serializer_class = serializers.CommentSerializer
    queryset = models.Comment.objects.all()
