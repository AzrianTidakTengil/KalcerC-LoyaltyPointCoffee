from django.urls import path, include
from . import views

auth = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password-reset/', views.reset_password, name='password_reset'),
]

customer = [
    path('', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    path('order/history/', views.order_history, name='order_history'),
    path('checkout/', views.checkout, name='checkout'),
]

worker = [
    path('order/', views.order, name='order'),
    path('order/cancel/<int:order_id>/', views.cancel_order, name='cancel_order'),
    path('order/add/', views.add_order, name='add_order'),
    path('order/update/<int:order_id>/', views.update_order, name='update_order'),
    path('loyalty/', views.loyalty_program, name='loyalty_program'),
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('menu/update/<int:item_id>/', views.update_menu_item, name='update_menu_item'),
    path('menu/delete/<int:item_id>/', views.delete_menu_item, name='delete_menu_item'),
]

urlpatterns = [
    path('', include(customer)),
    path('auth/', include(auth)),
    path('worker/', include(worker)),
]  