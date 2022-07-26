from datetime import date

from django.db.models import (
    CharField,
    DateTimeField,
    EmailField,
    IntegerField,
    Model,
    TextChoices,
    URLField,
)
from django.utils.translation import gettext_lazy as _


class Company(Model):
    """
    Company model for backend.
    For display company info on the list and profile for company user
    Create, delete and update from company user
    View for all users if company user choose to publish
    """

    EMPLOYEE_COUNT_CHOICES = [
        ("1-5", "1-5"),
        ("6-10", "6-10"),
        ("11-20", "11-20"),
        ("21-50", "21-50"),
        ("51-100", "51-100"),
        ("101-200", "101-200"),
        ("201-500", "201-500"),
        ("501-1000", "501-1000"),
        ("1000+", "1000+"),
    ]
    name = CharField(_("Name of Company"), max_length=20)
    full_name = CharField(_("Full Name of Company"), max_length=200, blank=True)
    slogan = CharField(_("Slogan"), max_length=140, blank=True)
    website = URLField(_("Website"), blank=True)
    description = CharField(_("Description"), max_length=800, blank=True)
    location = CharField(_("Location"), max_length=200, blank=True)
    zip_code = IntegerField(_("Zip Code"), blank=True)
    founding_year = IntegerField(_("Founding Year"), default=date.today().year)
    employee_count = CharField(
        _("Employee Count"), choices=EMPLOYEE_COUNT_CHOICES, max_length=10
    )
    business = CharField(_("Type of Business"), max_length=100, blank=True)
    phone = CharField(_("Contact Phone"), max_length=20, blank=True)
    fax = CharField(_("Contact Fax"), max_length=20, blank=True)
    email = EmailField(_("Contact Email"), blank=True)
    created = DateTimeField(_("Created Time"), auto_now_add=True)
    last_update = DateTimeField(_("Last Update"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
