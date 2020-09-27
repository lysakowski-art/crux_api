from djongo import models

class Routes(models.Model):
    _id=models.ObjectIdField()
    route_title=models.CharField(max_length=40,blank=False)
    route_author=models.CharField(max_length=30,blank=False)
    route_rank=models.IntegerField(blank=False)
    route_type=models.BooleanField(default=True,blank=False)
    region=models.CharField(max_length=30,blank=False)
    #route_img=models.ImageField()
    placemant_and_belay_anchor=models.IntegerField(blank=False)
    route_description=models.CharField(max_length=250)
    #added_by==models.CharField(max_length=30)
    location=models.CharField(max_length=50)

class Pages(models.Model):
    _id=models.ObjectIdField()
    page_title=models.CharField(max_length=50)
    page_content=models.TextField(max_length=600)

class Regions(models.Model):
    _id=models.ObjectIdField()
    region_name=models.CharField(max_length=50, blank=False)
    group_of_regions=models.CharField(max_length=50, blank=False)