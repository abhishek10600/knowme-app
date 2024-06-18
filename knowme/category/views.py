from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser

from django.shortcuts import get_object_or_404

from .models import Category
from .serializers import CategorySerializer


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_category(request):
    data = request.data
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        category = Category.objects.create(name=data["name"])
        res = CategorySerializer(category, many=False)
        return Response({"category": res.data})
    return Response(serializer.errors)


@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response({"categories": serializer.data})


@api_view(["GET"])
def get_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response({"category": serializer.data})


@api_view(["PUT"])
@permission_classes([IsAdminUser])
def update_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    data = request.data
    category.name = data["name"]
    category.save()
    serializer = CategorySerializer(category, many=False)
    return Response({
        "message": "Category updated successfully.",
        "category": serializer.data
    })


@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def delete_category(request, pk):
    category = get_object_or_404(Category, id=pk)
    category.delete()
    return Response({"message": "Category deleted successfully."})
