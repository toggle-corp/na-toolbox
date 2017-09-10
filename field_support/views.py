from django.shortcuts import render, redirect
from django.views.generic import View

from toolbox.models import ToolList
from field_support.models import (
    DutyStation,
    SituationContext, PersonsOfConcernContext,
    CRRFCountryOption, JointActivityOption,
    ServiceRequested,
    ActivityInformation, SupportSector,
    DataSource,
    FieldSupportRequest,
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

    def post(self, request):
        fsr = FieldSupportRequest()

        fsr.full_name = request.POST['name']

        fsr.duty_station = DutyStation.objects.get(
            pk=request.POST['duty-station'])
        fsr.situation_context = SituationContext.objects.get(
            pk=request.POST['context-situation'])
        fsr.persons_of_concern_context = PersonsOfConcernContext.objects.get(
            pk=request.POST['context-persons-of-concern'])
        fsr.crrf_country = CRRFCountryOption.objects.get(
            pk=request.POST['crrf-country'])
        fsr.joint_activity = JointActivityOption.objects.get(
            pk=request.POST['joint-activity'])
        fsr.comment = request.POST.get('comment')

        service_requested = request.POST.get('service-requested')
        service_requested_other = request.POST.get('service-requested-other')

        if service_requested and service_requested != 'other':
            fsr.service_requested = ServiceRequested.objects.get(
                pk=service_requested)
        else:
            fsr.service_requested_other = service_requested_other

        activity_information = request.POST.get('activity-information')
        activity_information_other = request.POST.get(
            'activity-information-other')

        if activity_information and activity_information != 'other':
            fsr.activity_information = ActivityInformation.objects.get(
                pk=activity_information)
        else:
            fsr.activity_information_other = activity_information_other

        fsr.save()

        support_sectors = request.POST.getlist('support-sectors')
        support_sectors_other = request.POST.get('support-sectors-other')

        for sector in support_sectors:
            if sector == 'other':
                fsr.support_sectors_other = support_sectors_other
            else:
                fsr.support_sectors.add(
                    SupportSector.objects.get(pk=sector))

        data_sources = request.POST.getlist('data-sources')
        data_sources_other = request.POST.get('data-sources-other')

        for sector in data_sources:
            if sector == 'other':
                fsr.data_sources_other = data_sources_other
            else:
                fsr.data_sources.add(
                    DataSource.objects.get(pk=sector))

        fsr.save()

        return render(request, 'field_support/field-support-result.html')
