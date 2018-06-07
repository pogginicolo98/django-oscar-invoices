from django.test import TestCase

from oscar.core.loading import get_model
from oscar.test.factories import UserFactory, create_order

from oscar_invoices.utils import create_invoice

Country = get_model('address', 'Country')
Invoice = get_model('oscar_invoices', 'Invoice')
LegalEntity = get_model('oscar_invoices', 'LegalEntity')
LegalEntityAddress = get_model('oscar_invoices', 'LegalEntityAddress')


class TestInvoiceUtils(TestCase):

    def setUp(self):
        super(TestInvoiceUtils, self).setUp()
        self.user = UserFactory()
        self.order = create_order(number='000042', user=self.user)

    def test_invoice_cannot_be_created_without_legal_entity(self):
        self.assertFalse(Invoice.objects.exists())
        create_invoice(self.order)
        self.assertFalse(Invoice.objects.exists())

    def test_invoice_cannot_be_created_without_legal_entity_address(self):
        LegalEntity.objects.create(
            business_name='Test company', vat_number='test-vat-number')
        self.assertFalse(Invoice.objects.exists())
        create_invoice(self.order)
        self.assertFalse(Invoice.objects.exists())

    def test_invoice_can_be_created_with_legal_entity_and_its_address(self):
        legal_entity = LegalEntity.objects.create(
            business_name='Test company', vat_number='test-vat-number')
        country = Country.objects.create(
            iso_3166_1_a2='GB', name="UNITED KINGDOM")
        LegalEntityAddress.objects.create(
            legal_entity=legal_entity,
            line1='1 Egg Street',
            line4='London',
            postcode='N12 9RE',
            country=country,
        )

        self.assertFalse(Invoice.objects.exists())
        create_invoice(self.order)
        self.assertTrue(Invoice.objects.exists())
        invoice = Invoice.objects.first()
        # Document created and saved
        self.assertIsNotNone(invoice.document)
