from django.urls import path
from .views import *

urlpatterns = [
    path('', UserListView.as_view(), name='customuser_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='customuser_detail'),
    path('users/create/', UserCreateView.as_view(), name='customuser_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='customuser_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='customuser_delete'),

    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    path('debts/', DebtListView.as_view(), name='debt_list'),
    path('debts/<int:pk>/', DebtDetailView.as_view(), name='debt_detail'),
    path('debts/create/', DebtCreateView.as_view(), name='debt_create'),
    path('debts/<int:pk>/update/', DebtUpdateView.as_view(), name='debt_update'),
    path('debts/<int:pk>/delete/', DebtDeleteView.as_view(), name='debt_delete'),

    path('payments/', PaymentListView.as_view(), name='payment_list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment_detail'),
    path('payments/create/', PaymentCreateView.as_view(), name='payment_create'),
    path('payments/<int:pk>/update/', PaymentUpdateView.as_view(), name='payment_update'),
    path('payments/<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment_delete'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchases/<int:pk>/update/', PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchases/<int:pk>/delete/', PurchaseDeleteView.as_view(), name='purchase_delete'),

    path('contact-history/', ContactHistoryListView.as_view(), name='contacthistory_list'),
    path('contact-history/<int:pk>/', ContactHistoryDetailView.as_view(), name='contacthistory_detail'),
    path('contact-history/create/', ContactHistoryCreateView.as_view(), name='contacthistory_create'),
    path('contact-history/<int:pk>/update/', ContactHistoryUpdateView.as_view(), name='contacthistory_update'),
    path('contact-history/<int:pk>/delete/', ContactHistoryDeleteView.as_view(), name='contacthistory_delete'),

    path('fines/', FineListView.as_view(), name='fine_list'),
    path('fines/<int:pk>/', FineDetailView.as_view(), name='fine_detail'),
    path('fines/create/', FineCreateView.as_view(), name='fine_create'),
    path('fines/<int:pk>/update/', FineUpdateView.as_view(), name='fine_update'),
    path('fines/<int:pk>/delete/', FineDeleteView.as_view(), name='fine_delete'),

    path('notifications/', NotificationListView.as_view(), name='notification_list'),
    path('notifications/<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
    path('notifications/create/', NotificationCreateView.as_view(), name='notification_create'),
    path('notifications/<int:pk>/update/', NotificationUpdateView.as_view(), name='notification_update'),
    path('notifications/<int:pk>/delete/', NotificationDeleteView.as_view(), name='notification_delete'),

    path('checklists/', ChecklistListView.as_view(), name='checklist_list'),
    path('checklists/<int:pk>/', ChecklistDetailView.as_view(), name='checklist_detail'),
    path('checklists/create/', ChecklistCreateView.as_view(), name='checklist_create'),
    path('checklists/<int:pk>/update/', ChecklistUpdateView.as_view(), name='checklist_update'),
    path('checklists/<int:pk>/delete/', ChecklistDeleteView.as_view(), name='checklist_delete'),
]
