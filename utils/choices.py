from django.db import models

class UserTypeChoices(models.IntegerChoices):
    CUSTOMER = 1, "Customer"
    STAFF = 2, "Staff"