from django.core.management.base import BaseCommand
from field_support.models import DutyStation

import json
import urllib.request


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with urllib.request.urlopen(
                'https://restcountries.eu/rest/v2/all'
        ) as response:
            data = json.loads(response.read().decode('utf-8'))

            for country in data:
                name = country['name']

                if DutyStation.objects.filter(title=name).count() == 0:
                    ds = DutyStation()
                    ds.title = name
                    ds.save()
