from django.urls import path

from . import views

urlpatterns = [
    path('sales', views.SalesListView.as_view(), name="sales-list"),
    path('new-sales', views.new_sales, name="new-sales"),
    path('new-sales-edit/<str:invoice_no>', views.new_sales_edit, name="new-sales-edit"),
    path('sales-post/<str:invoice_no>', views.sales_post, name="post-sales"),
    # path('sales-delete/<str:invoice_no>', views.sales_delete, name="sales-delete"),
    path('print-challan/<str:invoice_no>', views.print_challan, name='print-challan'),
    path('print-bill/<str:invoice_no>', views.print_bill, name='print-bill'),
    path('customer-information', views.customer_info, name="customer-information"),
    path('get-available-stock-by-warehouse', views.stock_by_warehouse, name="available-stock-by-warehouse"),
    path('sales_item_popup', views.sales_item_popup, name='sales-item-popup'),
    path('add-new-customer', views.add_new_customers, name="add-new-customer"),
    # path('new-shipper', views.new_shipper, name="new-shipper"),
    #  path('shipper-information', views.shipper_info, name="shipper-information"),

    # path('print-challan/<str:invoice_no>', views.test, name='print-challan'),
]
