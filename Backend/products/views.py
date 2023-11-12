from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from .models import Device, DeviceBrand, DeviceType
from .serializers import DeviceSerializer, DeviceTypeSerializer, DeviceBrandSerializer


class DeviceListCreateView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])


class DeviceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceBrandListCreateView(generics.ListCreateAPIView):
    queryset = DeviceBrand.objects.all()
    serializer_class = DeviceBrandSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])


class DeviceBrandRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceBrand.objects.all()
    serializer_class = DeviceBrandSerializer


class DeviceTypeListCreateView(generics.ListCreateAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[0])


class DeviceTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DeviceType.objects.all()
    serializer_class = DeviceTypeSerializer
