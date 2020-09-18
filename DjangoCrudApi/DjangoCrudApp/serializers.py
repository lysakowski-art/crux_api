from rest_framework import serializers 
from DjangoCrudApp.models import Routes
 
 
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