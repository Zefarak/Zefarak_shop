from django.db.models.signals import post_save
from django.utils.text import slugify
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models import Sum
from django.conf import settings
from django.dispatch import receiver

from site_settings.constants import MEDIA_URL, CURRENCY, TAXES_CHOICES
from .validators import validate_file
WAREHOUSE_ORDERS_TRANSCATIONS = settings.WAREHOUSE_ORDERS_TRANSCATIONS


class Vendor(models.Model):
    active = models.BooleanField(default=True)
    title = models.CharField(unique=True, max_length=70, verbose_name="'Ονομα")
    vat = models.CharField(max_length=9, blank=True, null=True, verbose_name="VAT")
    vat_city = models.CharField(max_length=100, blank=True, null=True, verbose_name="ΑΦΜ")
    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name="Τηλέφωνο")
    phone1 = models.CharField(max_length=10, null=True, blank=True, verbose_name="Τηλέφωνο")
    fax = models.CharField(max_length=10, null=True, blank=True, verbose_name="Fax")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")

    site = models.URLField(max_length=40, blank=True, null=True, verbose_name='Site')
    address = models.CharField(max_length=40, null=True, blank=True, verbose_name='Διεύθυνση')
    city = models.CharField(max_length=40, null=True, blank=True, verbose_name='Πόλη')
    zipcode = models.CharField(max_length=40, null=True, blank=True, verbose_name='TK')
    description = models.TextField(null=True, blank=True, verbose_name="Περιγραφή")
    timestamp = models.DateField(auto_now_add=True)
    taxes_modifier = models.CharField(max_length=1, choices=TAXES_CHOICES, default='3')
    # managing deposits
    remaining_deposit = models.DecimalField(default=0, decimal_places=2, max_digits=100,
                                            verbose_name='Υπόλοιπο προκαταβολών')
    balance = models.DecimalField(default=0, max_digits=100, decimal_places=2, verbose_name="Υπόλοιπο")

    class Meta:
        verbose_name_plural = '9. Προμηθευτές'
        ordering = ['title', ]

    def save(self, *args, **kwargs):
        orders = self.vendor_orders.all()
        self.balance = orders.aggregate(Sum('final_value'))['final_value__sum'] if orders else 0
        self.balance -= orders.aggregate(Sum('paid_value'))['paid_value__sum'] if orders else 0
        super(Vendor, self).save(*args, **kwargs)

    def get_edit_url(self):
        return reverse('warehouse:vendor_detail', kwargs={'pk': self.id})

    def get_phones(self):
        cellphone = self.phone if self.phone else 'No Data'
        phone = self.phone1 if self.phone1 else 'No Data'
        return f'{cellphone} - {phone}'

    def full_address(self):
        address, city = self.address if self.address else 'No data', self.city if self else 'No data'
        zipcode = self.zipcode if self.zipcode else 'No data'
        return f'{address} - {city} - {zipcode}'

    def tax_details(self):
        vat, vat_city = self.vat if self.vat else 'No data', self.vat_city if self.vat_city else 'No data'
        return f'{vat} - {vat_city}'

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        vendor_name = request.GET.getlist('vendor_name', None)
        balance_name = request.GET.get('balance_name', None)
        try:
            queryset = queryset.filter(title__icontains=search_name) if search_name else queryset
            queryset = queryset.filter(balance__gte=1) if balance_name else queryset
            queryset = queryset.filter(id__in=vendor_name) if vendor_name else queryset
        except:
            queryset = queryset
        return queryset

    def __str__(self):
        return self.title

    def get_report_url(self):
        return reverse('reports:vendor_detail', kwargs={'pk': self.id})

    def template_tag_remaining_deposit(self):
        return ("{0:.2f}".format(round(self.remaining_deposit, 2))) + ' %s' % (CURRENCY)

    def tag_balance(self):
        return ("{0:.2f}".format(round(self.balance, 2))) + ' %s' % (CURRENCY)
    tag_balance.short_description = 'Υπόλοιπο'

    def tag_deposit(self):
        return "%s %s" % (self.remaining_deposit, CURRENCY)

    def tag_phones(self):
        return '%s' % self.phone if self.phone else ' ' + ', %s' % self.phone1 if self.phone1 else ' '

    def get_absolute_url_form(self):
        return reverse('edit_vendor_id', kwargs={'dk': self.id})


class Brand(models.Model):
    active = models.BooleanField(default=True, verbose_name='Ενεργοποίηση')
    title = models.CharField(max_length=120, verbose_name='Ονομασία Brand')
    image = models.ImageField(blank=True, upload_to='brands/', verbose_name='Εικόνα', validators=[validate_file, ])
    order_by = models.IntegerField(default=1,verbose_name='Σειρά Προτεριότητας')
    meta_description = models.CharField(max_length=255, blank=True)
    width = models.IntegerField(default=240)
    height = models.IntegerField(default=240)
    slug = models.SlugField(blank=True, null=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = '4. Brands'
        ordering = ['title']

    def __str__(self):
        return self.title

    def tag_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="400px" height="400px" />')

    def image_tag_tiny(self):
        return mark_safe('<img scr="%s/%s" width="100px" height="100px" />' % (MEDIA_URL, self.image))
    tag_image.short_description = 'Είκονα'

    def tag_active(self):
        return 'Active' if self.active else 'No active'

    def get_absolute_url(self):
        return reverse('brand', kwargs={'slug': self.slug})

    def get_edit_url(self):
        return reverse('dashboard:brand_edit_view', kwargs={'pk':self.id})

    @staticmethod
    def filters_data(queryset, request):
        search_name = request.GET.get('search_name', None)
        active_name = request.GET.getlist('active_name', None)
        brand_name = request.GET.getlist('brand_name', None)
        queryset = queryset.filter(id__in=brand_name) if brand_name else queryset
        queryset = queryset.filter(title__icontains=search_name) if search_name else queryset
        queryset = queryset.filter(active=True) if active_name else queryset
        return queryset


@receiver(post_save, sender=Brand)
def create_slug(sender, instance, **kwargs):
    if not instance.slug:
        new_slug = slugify(instance.title, allow_unicode=True)
        qs_exists = Brand.objects.filter(slug=new_slug).exists()
        instance.slug = f'{new_slug}-{instance.id}' if qs_exists else new_slug
        instance.save()