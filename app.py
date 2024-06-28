from viktor import ViktorController
from viktor.parametrization import ViktorParametrization, Text, GeoPointField, GeoPolygonField
from viktor.views import MapPolygon, MapResult, MapPoint, MapView


class Parametrization(ViktorParametrization):
    pass


class Controller(ViktorController):
    label = 'My Entity Type'
    parametrization = Parametrization

    @MapView("Map", duration_guess=1)
    def starter_guide_map(self, params, **kwargs):
        features=[]
        return MapResult(features)
