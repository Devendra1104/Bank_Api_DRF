from django.db import models

class Bank(models.Model):
    ifsc = models.CharField(max_length=150)
    bank_id = models.IntegerField()
    branch = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    bank_name = models.CharField(max_length=150)

    def __str__(self):
        return self.bank_name[0:25]