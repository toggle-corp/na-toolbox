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

            guidance_list = None
            try:
                guidance_list = ToolList.objects.get(
                    title__iexact='Guidance and resource documents')
            except:
                guidance_list = ToolList(
                    title='Guidance and resource documents')
                guidance_list.save()

            for i, row in enumerate(data):
                if i == 0:
                    continue

                current_list = None
                if row[2] == 'gg':
                    current_list = guidance_list
                elif row[2] == 'tt':
                    current_list = tool_list
                else:
                    continue

                category_name = row[0][3:]

                category = None
                try:
                    category = Category.objects.get(
                        title__iexact=category_name,
                        tool_list=current_list)
                except:
                    category = Category(title=category_name,
                                        tool_list=current_list)

                category.order = row[0][:1]
                category.save()

                tool = None
                try:
                    tool = Tool.objects.get(title=row[5], category=category,
                                            organization=row[4])
                except:
                    tool = Tool()

                tool.category = category
                tool.order = row[1]

                tool.url = row[3]
                tool.organization = row[4]
                tool.title = row[5]
                tool.description = row[6]
                tool.tool_type = row[7]

                format = None
                try:
                    format = Format.objects.get(title__iexact=row[8])
                except:
                    format = Format(title=row[8])
                    format.save()

                tool.format = format

                tool.save()
