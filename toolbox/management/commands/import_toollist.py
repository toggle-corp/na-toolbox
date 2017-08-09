from django.core.management.base import BaseCommand
from django.contrib.staticfiles import finders

import os
import csv

from toolbox.models import ToolList, Category, Format, Tool


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        directory = finders.find('files/')
        filename = 'toolbox_list.csv'
        with open(os.path.join(directory, filename), 'r') as file:
            data = csv.reader(file)

            tool_list = None
            try:
                tool_list = ToolList.objects.get(
                    title__iexact='tools and templates')
            except:
                tool_list = ToolList(title='Tools and templates')
                tool_list.save()

            for i, row in enumerate(data):
                if i == 0:
                    continue
                category_name = row[0][3:]

                category = None
                try:
                    category = Category.objects.get(
                        title__iexact=category_name,
                        tool_list=tool_list)
                except:
                    category = Category(title=category_name,
                                        tool_list=tool_list)

                category.order = row[0][:1]
                category.save()

                tool = None
                try:
                    tool = Tool.objects.get(title=row[3], category=category,
                                            organization=row[2])
                except:
                    tool = Tool()

                tool.category = category
                tool.order = row[1]
                tool.organization = row[2]
                tool.title = row[3]
                tool.description = row[4]
                tool.tool_type = row[5]

                format = None
                try:
                    format = Format.objects.get(title__iexact=row[6])
                except:
                    format = Format(title=row[6])
                    format.save()

                tool.format = format
                tool.url = row[8]

                tool.save()
