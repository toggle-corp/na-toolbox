from django.db import models


class DutyStation(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class SituationContext(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class PersonsOfConcernContext(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class ServiceRequested(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class ActivityInformation(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class SupportSector(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class DataSource(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class CRRFCountryOption(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class JointActivityOption(models.Model):
    title = models.CharField(max_length=255)
    order = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class FieldSupport(models.Model):
    full_name = models.CharField(max_length=255)

    duty_station = models.ForeignKey(DutyStation)
    situation_context = models.ForeignKey(SituationContext)
    persons_of_concern_context = models.ForeignKey(PersonsOfConcernContext)
    crrf_country = models.ForeignKey(CRRFCountryOption)

    service_requested = models.ForeignKey(ServiceRequested,
                                          default=None, null=True,
                                          blank=True)
    service_requested_other = models.CharField(max_length=500, blank=True)

    activity_information = models.ForeignKey(ActivityInformation,
                                             default=None, null=True,
                                             blank=True)
    activity_information_other = models.CharField(max_length=500, blank=True)

    activity_support = models.ManyToManyField(SupportSector, blank=True)
    activity_support_other = models.CharField(max_length=500, blank=True)

    data_sources = models.ManyToManyField(DataSource, blank=True)
    data_sources_other = models.CharField(max_length=500, blank=True)

    joint_activity = models.ForeignKey(JointActivityOption,
                                       default=None, null=True, blank=True)

    comment = models.TextField(blank=True)

    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'At {} by {}'.format(self.sent_at, self.full_name)
