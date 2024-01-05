from django.db import models

# Create your models here.
class Districts(models.Model):
    district=models.CharField(max_length=250)
    def __str__(self):
        return self.district
class Branches(models.Model):
    selectdistrict=models.ForeignKey(Districts,on_delete=models.CASCADE)
    branch=models.CharField(max_length=250)
    def __str__(self):
        return self.branch

class Customer(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    ACCOUNT_CHOICES=[('S','Select Account Type'),('C','Current Account'),('S','Savings Account'),('N','Nri Account')]
    MATERIAL_CHOICES=[('C','Cheque Book'),('D','Debit Card'),('C','Credit Card')]
    Name=models.CharField(max_length=100)
    BirthDate=models.DateField(null=True,blank=True)
    Age=models.IntegerField(null=True,blank=True)
    Gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    Phone=models.IntegerField(null=True,blank=True)
    Address=models.TextField(max_length=500)
    Account_type=models.CharField(max_length=50)
    District=models.ForeignKey(Districts,on_delete=models.CASCADE)
    Branch=models.ForeignKey(Branches,on_delete=models.CASCADE)
    Materials=models.CharField(max_length=500)

    def __str__(self):
        return self.name



