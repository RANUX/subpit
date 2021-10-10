from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
import string

def _simple_host_name_validator(value):
    """
    Validate that the given value contains no whitespaces to prevent common
    typos.
    """
    checks = ((s in value) for s in string.whitespace)
    if any(checks):
        raise ValidationError(
            _("The domain name cannot contain any spaces or tabs."),
            code='invalid',
        )

class Subscriber(models.Model):

    name = models.CharField(_('name'), max_length=150, blank=True)
    lastname = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(_('phone'), max_length=30, blank=True)
    valid = models.BooleanField(_('valid'), default=True)
    host = models.CharField(            # host from where sub data came from
        _('host name'),
        max_length=100,
        validators=[_simple_host_name_validator],
    )
    other = models.CharField(_('Other info'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
