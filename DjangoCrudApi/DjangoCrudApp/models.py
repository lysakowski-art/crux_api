from djongo import models


class Region(models.Model):
    _id=models.ObjectIdField()
    region_name=models.CharField(max_length=50, blank=False)
    group_of_regions=models.CharField(max_length=50, blank=False)


class Route(models.Model):
    _id=models.ObjectIdField()
    route_title=models.CharField(max_length=40,blank=False)
    route_author=models.CharField(max_length=30,blank=False)
    route_rank=models.IntegerField(blank=False)
    route_type=models.BooleanField(default=True,blank=False)
    region=models.CharField(max_length=30, blank=False, default=None)
    # route_img=models.URLField(max_length=1000)
    placemant_and_belay_anchor=models.IntegerField(default=1)
    route_description=models.CharField(max_length=250)
    # location=models.CharField(max_length=50)


class Page(models.Model):
    _id=models.ObjectIdField()
    page_title=models.CharField(max_length=50)
    page_content=models.TextField()
    language=models.BooleanField(default=True)


