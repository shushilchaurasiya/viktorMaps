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
        features=[
            MapPoint( 52.5200, 13.4050, title='Berlin, Germany'),
            MapPoint(47.6062, -122.3321, title='Seattle, USA'),
            MapPoint(53.3498, -6.2603, title='Dublin, Ireland'),
            MapPoint(43.6511, -79.3470, title='Toronto, Canada'),
            MapPoint(41.3851, 2.1734, title='Barcelona, Spain'),
            MapPoint(-34.6037, -58.3816, title='Buenos Aires, Argentina'),
            MapPoint(-33.9249, 18.4241, title='Cape Town, South Africa')
        ]
        return MapResult(features)
