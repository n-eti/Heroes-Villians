from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer

@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        super_name = request.query_params.get('type')
        print(super_name)
        
        queryset = Super.objects.all()
        serializer = SuperSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=400)

@api_view(['Get','PUT', 'DELETE'])
def super_detail(request, pk):
    super = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)

