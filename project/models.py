from django.db import models


"""Mixin for adding create and update fields in all the models"""
class CreationUpdationMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True, help_text='When this record is created!')
    updated = models.DateTimeField(auto_now=True, help_text='When this record was modified!')

    class Meta:
        abstract = True

"""Project Model"""
class Project(CreationUpdationMixin):
    name = models.CharField(max_length = 200)
    fmv = models.FloatField(default=0, help_text = 'Fair market value')

    def __str__(self):
        return self.name

"""Deal Model"""
class Deal(CreationUpdationMixin):
    name = models.CharField(max_length=255, unique=True)  # Unique name for each deal
    projects = models.ManyToManyField(to=Project, related_name = 'deals')
    tax_credit_transfer_rate = models.FloatField()

    def __str__(self):
        return self.name

