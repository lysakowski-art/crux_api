from rest_framework import serializers
from DjangoCrudApp.models import Route
from DjangoCrudApp.models import Page
from DjangoCrudApp.models import Region


class RouteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Route
        fields = ('_id',
                  'route_title',
                  'route_author',
                  'route_rank',
                  'route_type',
                  'region',
                  'route_img',
                  'placemant_and_belay_anchor',
                  'route_description',
                  'added_by',
                  'location')


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = (
            '_id',
            'page_title',
            'page_content',
            'language'
        )
class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = (
            '_id',
            'region_name',
            'group_of_regions'
        )
