from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import *
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', views.register.as_view(), name="register"),
    path('user_login/', views.user_login.as_view(), name="user_login"),
    path('dashboard/', views.dashboard.as_view(), name="dashboard"),
    path('add_employee_view/', views.add_employee_view.as_view(), name="add_employee_view"),
    path('add_agent_view/', views.add_agent_view.as_view(), name="add_agent_view"),
    path('employee_details/', views.employee_details.as_view(), name="employee_details"),
    path('expenses/', views.expenses.as_view(), name="expenses"),
    path('add_balance/', views.add_balance.as_view(), name="add_balance"),
    path('Balance_details/', views.Balance_details.as_view(), name="Balance_details"),
    path('agent_list/', views.agent_list.as_view(), name="agent_list"),
    path('payroll/', views.payroll.as_view(), name="payroll"),
    path('orders/', views.orders.as_view(), name="orders"),
    path('add_new_order/', views.add_new_order.as_view(), name="add_new_order"),
    path('new_orders/', views.new_orders.as_view(), name="new_orders"),
    path('canceled_orders/', views.canceled_orders.as_view(), name="canceled_orders"),
    path('payment_sucessfully/', views.payment_sucessfully.as_view(), name="payment_sucessfully"),









]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
