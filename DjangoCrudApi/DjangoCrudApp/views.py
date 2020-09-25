from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from bson import ObjectId
# Create your views here.
from DjangoCrudApp.models import Routes
from DjangoCrudApp.models import Pages
from DjangoCrudApp.serializers import RouteSerializer
from DjangoCrudApp.serializers import PageSerializer


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def routes_list(request):

    if request.method == "GET":
        routes = Routes.objects.all()

        route_title = request.query_params.get('route_title', None)
        if route_title is not None:
            routes = routes.filter(route_title__icontains=route_title)
        routes_serializer = RouteSerializer(routes, many=True)
        return JsonResponse(routes_serializer.data, safe=False)

    elif request.method == "POST":
        route_data = JSONParser().parse(request)
        route_serializer = RouteSerializer(data=route_data)

        if route_serializer.is_valid():
            route_serializer.save()
            return JsonResponse(route_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(route_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def routes_id(request, id):
    try:
        route = Routes.objects.get(_id=ObjectId(id))
    except Routes.DoesNotExist:
        return JsonResponse({'message': 'The route does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        route_serializer = RouteSerializer(route)
        return JsonResponse(route_serializer.data)

    elif request.method == 'PUT':
        route_data = JSONParser().parse(request)
        route_serializer = RouteSerializer(route, data=route_data)
        if route_serializer.is_valid():
            route_serializer.save()
            return JsonResponse(route_serializer.data)
        return JsonResponse(route_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def pages_id(request, id):
    try:
        page = Pages.objects.get(_id=ObjectId(id))
    except Pages.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        page_serializer = PageSerializer(page)
        return JsonResponse(page_serializer.data)
