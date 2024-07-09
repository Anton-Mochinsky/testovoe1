from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)


class Bike(models.Model):
    bike_id = models.AutoField(primary_key=True)
    bike_name = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

class UserHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
