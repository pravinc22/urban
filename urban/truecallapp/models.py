from django.db import models

class true_form(models.Model):
    eu="eu"
    world ="World"
    andriod ="Andriod"
    iPhone ="IPhone"
    truecaller_business="truecaller_business"
    developer="Developer_l"

    list=(
    (eu,'eu__eea_and_switzerland'),
    (world,'rest_of_the_world'),
    )
    list_os=(
        (andriod,'Andriod'),
        (iPhone,'iPhone'),
        (truecaller_business,'Truecaller_business'),
        (developer,'developer'),
    )
    email = models.EmailField()
    number =models.IntegerField()
    platform = models.CharField(choices=list_os,max_length=20)
    description = models.TextField(max_length=200)
    subject = models.CharField(max_length=30)
    attachment = models.FileField(upload_to='files',blank=True)
    region = models.CharField(choices=list,max_length=10)
    def __str__(self):
        return self.email

class careerModel(models.Model):
    First_Name=models.CharField(max_length=30)
    Last_Name=models.CharField(max_length=30)
    Email=models.EmailField()
    Number =models.IntegerField()
    Linkedin_Profile=models.URLField(blank=True)
    Website=models.URLField(blank=True)
    How_did_you_know_about_this_job=models.CharField(max_length=100)
    Attachment = models.FileField(upload_to='files',blank=True)
    Cover_Later =models.ImageField(upload_to='cover_Later',blank=True)

    def __str__(self):
        return self.First_Name

# Create your models here.
