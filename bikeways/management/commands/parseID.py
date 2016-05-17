from django.core.management.base import BaseCommand
from xml.etree.ElementTree import ElementTree
from bikeways.models import CoordinateWithID
import os
import django
import re


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):

        tree = ElementTree()
        data = tree.parse('bikeways.kml')
        placemark = data.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

        i = 1
        for multiGeom in placemark:
            placemarkid = i
            for item in multiGeom:
                for lineString in item:
                    for coord in lineString:
                        key = placemarkid
                        splitcoords = coord.text
                        splitbycomma = re.split(',0 |,', splitcoords)
                        for index in range(len(splitbycomma)-1):
                            if index % 2 == 0:
                                lng = splitbycomma[index]
                                lat = splitbycomma[index+1]
                                c = CoordinateWithID(key=key, latitude=float(lat), longitude=float(lng))
                                c.save()

            i += 1

    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
        django.setup()
        self._create_tags()