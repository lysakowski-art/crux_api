from django.http import HttpResponse
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from bson import ObjectId

# MODELS!
from DjangoCrudApp.models import Route
from DjangoCrudApp.models import Page
from DjangoCrudApp.models import Region

# SERIALIZERS
from DjangoCrudApp.serializers import RouteSerializer
from DjangoCrudApp.serializers import PageSerializer
from DjangoCrudApp.serializers import RegionSerializer

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def routes_list(request):

    if request.method == "GET":
        routes = Route.objects.all()

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
def routes_filtered(request, route_rank, region):
    try:
        routes = Route.objects.all()
        if request.method == "GET":
            if route_rank != 0 and region != "random":
                routes = routes.filter(route_rank=route_rank, region=region)
                routes_serializer = RouteSerializer(routes, many=True)
                return JsonResponse(routes_serializer.data, safe=False)
            elif route_rank != 0 and region == "random":
                routes = routes.filter(route_rank=route_rank)
                routes_serializer = RouteSerializer(routes, many=True)
                return JsonResponse(routes_serializer.data, safe=False)
            elif route_rank == 0 and region != "random":
                routes = routes.filter(region=region)
                routes_serializer = RouteSerializer(routes, many=True)
                return JsonResponse(routes_serializer.data, safe=False)

        elif request.method == 'PUT':
            route_data = JSONParser().parse(request)
            route_serializer = RouteSerializer(route, data=route_data)
            if route_serializer.is_valid():
                route_serializer.save()
                return JsonResponse(route_serializer.data)
            return JsonResponse(route_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Routes.DoesNotExist:
        return JsonResponse({'message': 'The route does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def pages_id(request, page_title):
    try:
        pages = Page.objects.all()
    except Page.DoesNotExist:
        return JsonResponse({'message': 'The page does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        # pages = Page.objects.all()
        # page_title = request.query_params.get('page_title', None)
        pages = pages.filter(page_title__icontains=page_title)

        pages_serializer = PageSerializer(pages, many=True)
        return JsonResponse(pages_serializer.data, safe=False)


@api_view(['GET', 'POST'])
def regions_list(request):
    if request.method == "GET":
        regions = Region.objects.all()

        region_name = request.query_params.get('region_name', None)
        if region_name is not None:
            regions = routes.filter(region_name__icontains=region_title)
        regions_serializer = RegionSerializer(regions, many=True)
        return JsonResponse(regions_serializer.data, safe=False)
    
    elif request.method == "POST":
        region_data = JSONParser().parse(request)
        region_serializer = RegionSerializer(data=region_data)

        if region_serializer.is_valid():
            region_serializer.save()
            return JsonResponse(region_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)