from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig


class InvoicesConfig(OscarConfig):
    label = 'oscar_invoices'
    name = 'oscar_invoices'
    verbose_name = _('Invoices')
