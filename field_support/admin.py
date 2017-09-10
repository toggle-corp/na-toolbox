from django.contrib import admin
from field_support.models import (
    DutyStation,
    SituationContext, PersonsOfConcernContext,
    CRRFCountryOption, JointActivityOption,
    ServiceRequested,
    ActivityInformation, SupportSector,
    DataSource,
)


admin.site.register(DutyStation)
admin.site.register(SituationContext)
admin.site.register(PersonsOfConcernContext)
admin.site.register(CRRFCountryOption)
admin.site.register(ServiceRequested)
admin.site.register(ActivityInformation)
admin.site.register(SupportSector)
admin.site.register(DataSource)
admin.site.register(JointActivityOption)
