from django.urls import path
from .views import (DashboardView,
                    StoreListView, StoreCreateView, StoreEditView,
                    PaymentMethodListView, PaymentMethodCreateView, PaymentMethodUpdateView,
                    ShippingListView, ShippingCreateView, ShippingEditView,
                    BannerListView, BannerCreateView, BannerUpdateView, banner_delete_view
                    )

app_name = 'site_settings'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('stores/', StoreListView.as_view(), name='stores'),
    path('stores/edit/<int:pk>/', StoreEditView.as_view(), name='store_edit'),
    path('stores/create/', StoreCreateView.as_view(), name='store_create'),

    path('payment-method-list/', PaymentMethodListView.as_view(), name='payment_methods'),
    path('payment/edit/<int:pk>/', PaymentMethodUpdateView.as_view(), name='payment_edit'),
    path('payment/create/', PaymentMethodCreateView.as_view(), name='payment_create'),

    path('shipping-list/', ShippingListView.as_view(), name='shipping'),
    path('shipping/edit/<int:pk>/', ShippingEditView.as_view(), name='shipping_edit'),
    path('shipping/create/', ShippingCreateView.as_view(), name='shipping_create'),

    path('banner-list/', BannerListView.as_view(), name='banner_list'),
    path('banner/edit/<int:pk>/', BannerUpdateView.as_view(), name='banner_edit'),
    path('banner/create/', BannerCreateView.as_view(), name='banner_create'),
    path('banner/delete/<int:pk>/', banner_delete_view, name='banner_delete'),
]