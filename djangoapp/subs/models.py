from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _

class Subscriber(models.Model):

    name = models.CharField(_('Name'), max_length=150, blank=True)
    lastname = models.CharField(_('Last name'), max_length=150, blank=True)
    email = models.EmailField(blank=True, unique=True)
    phone = PhoneNumberField(_('Phone'), blank=True, unique=True)
    valid = models.BooleanField(_('Valid'), default=True)
    other = models.CharField(_('Other info'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('subscriber')
        verbose_name_plural = _('subscribers')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
