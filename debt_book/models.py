from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('seller', 'Seller'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='seller')
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.username} - {self.role}'

class ClientManager(models.Manager):
    def total_debt(self):
        return Debt.objects.aggregate(total=Sum('amount'))['total'] or 0

    def clients_with_unpaid_debts(self):
        client_ids = Debt.objects.filter(is_paid=False).values_list('client_id', flat=True).distinct()
        return self.filter(id__in=client_ids)

class Client(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='clients')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/images', null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    address = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ClientManager()

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.phone_number} - {self.address}'

    def total_debt_for_client(self):
        return self.debts.aggregate(total=Sum('amount'))['total'] or 0

    def unpaid_debts(self):
        return self.debts.filter(is_paid=False)

class Debt(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='debts')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.amount} - {self.is_paid}'

class PaymentManager(models.Manager):
    def total_payments(self):
        return self.aggregate(total=Sum('amount'))['total'] or 0

class Payment(models.Model):
    debt = models.ForeignKey(Debt, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    objects = PaymentManager()

    def __str__(self):
        return f'{self.amount} - {self.paid_at}'

class ProductManager(models.Manager):
    def total_revenue(self):
        return Purchase.objects.aggregate(total=Sum('total_price'))['total'] or 0

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProductManager()

    def __str__(self):
        return f'{self.name} - {self.price}'

class Purchase(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.quantity} - {self.total_price} - {self.purchased_at}'

class ContactHistory(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contact_history')
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact_history')
    contact_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()

    def __str__(self):
        return f'{self.contact_date} - {self.notes}'

class Fine(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='fines')
    reason = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.reason} - {self.amount}'

class Notification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.message} - {self.is_read}'

class Checklist(models.Model):
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='checklists')
    task = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task} - {'Completed' if self.is_completed else 'Pending'}"

