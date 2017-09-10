from django.shortcuts import render
from django.views.generic import View

from toolbox.models import ToolList
from field_support.models import (
    DutyStation,
    SituationContext, PersonsOfConcernContext,
    CRRFCountryOption, JointActivityOption,
    ServiceRequested,
    ActivityInformation, SupportSector,
    DataSource,
)


class FieldSupportView(View):
    def get(self, request):
        context = {}
        context['tool_lists'] = ToolList.objects.all()

        context['duty_stations'] = DutyStation.objects.all()
        context['situation_contexts'] = SituationContext.objects.all()
        context['person_of_concern_contexts'] = \
            PersonsOfConcernContext.objects.all()
        context['crrf_country_options'] = CRRFCountryOption.objects.all()
        context['services_requested'] = ServiceRequested.objects.all()
        context['activity_informations'] = ActivityInformation.objects.all()
        context['support_sectors'] = SupportSector.objects.all()
        context['data_sources'] = DataSource.objects.all()
        context['joint_activity_options'] = JointActivityOption.objects.all()

        return render(request, 'field_support/field-support.html', context)
