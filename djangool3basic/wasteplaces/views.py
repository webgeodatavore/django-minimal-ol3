from django.shortcuts import render
# Create your views here.

from djgeojson.views import GeoJSONLayerView

class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4

def my_view(request):
    return render(request, 'index.html')
