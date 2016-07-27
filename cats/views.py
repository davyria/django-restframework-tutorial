from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from cats.models import Cat
from cats.serializers import CatSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def cat_list(request):
    """
    List all cats, or create a new cat.
    """
    if request.method == 'GET':
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def cat_detail(request, pk):
    """
    Retrieve, update or delete a cat.
    """
    try:
        cat = Cat.objects.get(pk=pk)
    except Cat.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CatSerializer(cat)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CatSerializer(cat, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        cat.delete()
        return HttpResponse(status=204)
