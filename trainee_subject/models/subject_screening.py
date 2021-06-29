from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import datetime_not_future
from edc_base.sites import SiteModelMixin
from edc_identifier.model_mixins import NonUniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugModelMixin
from edc_constants.choices import GENDER
from edc_utils import get_utcnow
from django_countries.fields import CountryField
from ..utils import Eligibilty
from django.db import models


class SubjectScreening(NonUniqueSubjectIdentifierFieldMixin, SiteModelMixin, SearchSlugModelMixin, BaseUuidModel):
    screening_identifier = models.CharField(
        verbose_name='Eligibility Identifier',
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        validators=[datetime_not_future],
        help_text='Date and time of report.')
