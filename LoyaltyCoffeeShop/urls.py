from django.urls import path, include
from . import views

auth = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', views.reset_password, name='password_reset'),
    path('login-master/', views.login_master, name='login_master'),
]

customer = [
    path('', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/history/', views.order_history, name='order_history'),
    path('checkout/', views.checkout, name='checkout'),
    path('final-payment/', views.final_payment, name='final_payment'),
    path('error-payment/', views.error_payment, name="error_payment"),
]

worker = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('order/', views.order, name='order'),
    path('order/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order/add/', views.add_order, name='add_order'),
    path('order/update/<int:order_id>/', views.update_order, name='update_order'),
    path('order/summary/<int:order_id>/', views.order_summary, name='order_summary'),
    path('loyalty/', views.loyalty_program, name='loyalty_program'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/update/<int:item_id>/', views.update_menu_item, name='update_menu_item'),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
    path('settings/', views.settings, name='settings'),
    path('settings/update/', views.update_settings, name='update_settings'),
    path('discounts/', views.discounts, name='discounts'),
    path('discounts/add/', views.add_discount, name='add_discount'),
    path('discounts/update/<int:discount_id>/', views.update_discount, name='update_discount'),
    path('discounts/delete/<int:discount_id>/', views.delete_discount, name='delete_discount'),
    path('reports/', views.reports, name='reports'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.customer_detail, name='customer_detail'),
]

urlpatterns = [
    path('', include(customer)),
    path('auth/', include(auth)),
    path('worker/', include(worker)),
]  