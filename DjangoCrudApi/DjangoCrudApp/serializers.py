from rest_framework import serializers 
from DjangoCrudApp.models import Routes
from DjangoCrudApp.models import Pages 
 
class RouteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Routes
        fields = ('_id',
                  'route_title',
                  'route_author',
                  'route_rank',
                  'route_type',
                  'region',
                  'placemant_and_belay_anchor',
                  'route_description',
                  'location')


class PageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = (
            '_id',
            'page_title',
            'page_content'
        )