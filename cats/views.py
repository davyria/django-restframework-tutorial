from rest_framework import status
from rest_framework.response import Response
from cats.models import Cat
from cats.serializers import CatSerializer
from rest_framework.views import APIView
from django.http import Http404


class CatList(APIView):
    """
    List all cats, or create a new one.
    """
    def get(self, request, format=None):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatDetail(APIView):
    """
    Retrieve, update or delete a cat instance.
    """
    def get_object(self, pk):
        try:
            return Cat.objects.get(pk=pk)
        except Cat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        cat = self.get_object(pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cat = self.get_object(pk)
        serializer = CatSerializer(cat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cat = self.get_object(pk)
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
