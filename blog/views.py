from django.shortcuts import render
from django.http import JsonResponse, response

from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

from .models import BlogModel

# from rest_framework import generics
# from rest_framework import viewsets


# Create your views here.


# def name(request):
#     return JsonResponse({"method": request.method})


@csrf_exempt
def name(request):
    method = request.method.lower()
    nn = [1,2,3,4,5]
    if method == "get":
        return JsonResponse({"data": nn})
    elif method == "post":
        return  JsonResponse({"data": "update"})

    return JsonResponse({"method": request.method})

class simple(APIView):

    def get(self, request):
        content = BlogModel.objects.all().values()
        # print(content)
        return JsonResponse({"data": list(content)})

    def post(self, request):
        content = BlogModel.objects.create(
            name = request.data["name"],
            body = request.data["body"],
            title = request.data["title"]

                       
        )

        print(content)
        return JsonResponse({"data": request.data})





# class you_See_ViewSet(viewsets.ModelViewSet):
#     queryset = BlogModel.objects.all()
#     serializer_class = Model_simple_serializer

