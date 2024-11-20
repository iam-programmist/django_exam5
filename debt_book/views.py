from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import CustomUser, Client, Debt, Payment, Product, Purchase, ContactHistory, Fine, Notification, Checklist

class UserListView(ListView):
    model = CustomUser
    template_name = 'customuser_list.html'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'customuser_detail.html'

class UserCreateView(CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'username', 'image', 'phone_number', 'email', 'address', 'role']
    template_name = 'customuser_form.html'
    success_url = reverse_lazy('client_create')

class UserUpdateView(UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'username', 'image', 'phone_number', 'email', 'address', 'role']
    template_name = 'customuser_form.html'
    success_url = reverse_lazy('client_create')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'customuser_confirm_delete.html'
    success_url = reverse_lazy('client_create')

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'

class ClientCreateView(CreateView):
    model = Client
    fields = ['seller', 'first_name', 'last_name', 'image', 'phone_number', 'email', 'address']
    template_name = 'client_form.html'
    success_url = reverse_lazy('product_create')

class ClientUpdateView(UpdateView):
    model = Client
    fields = ['seller', 'first_name', 'last_name', 'image', 'phone_number', 'email', 'address']
    template_name = 'client_form.html'
    success_url = reverse_lazy('product_create')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('product_create')

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('debt_create')

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'price']
    template_name = 'product_form.html'
    success_url = reverse_lazy('debt_create')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('debt_create')

class DebtListView(ListView):
    model = Debt
    template_name = 'debt_list.html'

class DebtDetailView(DetailView):
    model = Debt
    template_name = 'debt_detail.html'

class DebtCreateView(CreateView):
    model = Debt
    fields = ['client', 'amount', 'reason', 'due_date', 'is_paid']
    template_name = 'debt_form.html'
    success_url = reverse_lazy('notification_create')

class DebtUpdateView(UpdateView):
    model = Debt
    fields = ['client', 'amount', 'reason', 'due_date', 'is_paid']
    template_name = 'debt_form.html'
    success_url = reverse_lazy('notification_create')

class DebtDeleteView(DeleteView):
    model = Debt
    template_name = 'debt_confirm_delete.html'
    success_url = reverse_lazy('notification_create')

class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_detail.html'

class NotificationCreateView(CreateView):
    model = Notification
    fields = ['user', 'message', 'is_read']
    template_name = 'notification_form.html'
    success_url = reverse_lazy('fine_create')

class NotificationUpdateView(UpdateView):
    model = Notification
    fields = ['user', 'message', 'is_read']
    template_name = 'notification_form.html'
    success_url = reverse_lazy('fine_create')

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('fine_create')

class FineListView(ListView):
    model = Fine
    template_name = 'fine_list.html'

class FineDetailView(DetailView):
    model = Fine
    template_name = 'fine_detail.html'

class FineCreateView(CreateView):
    model = Fine
    fields = ['client', 'reason', 'amount']
    template_name = 'fine_form.html'
    success_url = reverse_lazy('payment_create')

class FineUpdateView(UpdateView):
    model = Fine
    fields = ['client', 'reason', 'amount']
    template_name = 'fine_form.html'
    success_url = reverse_lazy('payment_create')

class FineDeleteView(DeleteView):
    model = Fine
    template_name = 'fine_confirm_delete.html'
    success_url = reverse_lazy('payment_create')

class PaymentListView(ListView):
    model = Payment
    template_name = 'payment_list.html'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payment_detail.html'

class PaymentCreateView(CreateView):
    model = Payment
    fields = ['debt', 'amount']
    template_name = 'payment_form.html'
    success_url = reverse_lazy('checklist_create')

class PaymentUpdateView(UpdateView):
    model = Payment
    fields = ['debt', 'amount']
    template_name = 'payment_form.html'
    success_url = reverse_lazy('checklist_create')

class PaymentDeleteView(DeleteView):
    model = Payment
    template_name = 'payment_confirm_delete.html'
    success_url = reverse_lazy('checklist_create')

class ChecklistListView(ListView):
    model = Checklist
    template_name = 'checklist_list.html'

class ChecklistDetailView(DetailView):
    model = Checklist
    template_name = 'checklist_detail.html'

class ChecklistCreateView(CreateView):
    model = Checklist
    fields = ['seller', 'task', 'is_completed']
    template_name = 'checklist_form.html'
    success_url = reverse_lazy('purchase_create')

class ChecklistUpdateView(UpdateView):
    model = Checklist
    fields = ['seller', 'task', 'is_completed']
    template_name = 'checklist_form.html'
    success_url = reverse_lazy('purchase_create')

class ChecklistDeleteView(DeleteView):
    model = Checklist
    template_name = 'checklist_confirm_delete.html'
    success_url = reverse_lazy('purchase_create')

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'purchase_list.html'

class PurchaseDetailView(DetailView):
    model = Purchase
    template_name = 'purchase_detail.html'

class PurchaseCreateView(CreateView):
    model = Purchase
    fields = ['client', 'product', 'quantity']
    template_name = 'purchase_form.html'
    success_url = reverse_lazy('contacthistory_create')

class PurchaseUpdateView(UpdateView):
    model = Purchase
    fields = ['client', 'product', 'quantity']
    template_name = 'purchase_form.html'
    success_url = reverse_lazy('contacthistory_create')

class PurchaseDeleteView(DeleteView):
    model = Purchase
    template_name = 'purchase_confirm_delete.html'
    success_url = reverse_lazy('contacthistory_create')

class ContactHistoryListView(ListView):
    model = ContactHistory
    template_name = 'contacthistory_list.html'

class ContactHistoryDetailView(DetailView):
    model = ContactHistory
    template_name = 'contacthistory_detail.html'

class ContactHistoryCreateView(CreateView):
    model = ContactHistory
    fields = ['client', 'seller', 'notes']
    template_name = 'contacthistory_form.html'
    success_url = reverse_lazy('client_list')

class ContactHistoryUpdateView(UpdateView):
    model = ContactHistory
    fields = ['client', 'seller', 'notes']
    template_name = 'contacthistory_form.html'
    success_url = reverse_lazy('client_list')

class ContactHistoryDeleteView(DeleteView):
    model = ContactHistory
    template_name = 'contacthistory_confirm_delete.html'
    success_url = reverse_lazy('client_list')
