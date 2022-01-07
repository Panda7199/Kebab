from django.db import models


class Aboutus(models.Model):
    title = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class Chef(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='images/')
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

class Comment_cheff(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud Emas'),
    )
    cheff = models.ForeignKey(Chef, on_delete=models.CASCADE)
    name = models.CharField(max_length=55, blank=True)
    email = models.CharField(max_length=55, blank=True)
    comment = models.TextField(max_length=255,blank=True)
    ip = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, default='True')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('Read', 'O`qilgan'),
        ('Closed', 'Yopilgan'),
    )
    name = models.CharField(blank=True, max_length=20)
    surname = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=255)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=15, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('New', 'Yangi'),
        ('accepted', 'qabul qilingan'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=50)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def str(self):
        return self.name