# coding: utf-8


from django.conf.urls import patterns, url
# from djgeojson.views import GeoJSONLayerView
from .views import MapLayer

from .models import loc_colonnes_enterrees_nm

urlpatterns = patterns(
    '',
    #url(r'^$', views.index, name='index'),
    url(r'^data.geojson$',
        MapLayer.as_view(model=loc_colonnes_enterrees_nm),
        name='data'),
)