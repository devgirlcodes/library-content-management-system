from django.db import models
from django.conf import settings
from datetime import date
from django.core.validators import RegexValidator

# Create your models here.


class Section(models.Model):
    sec = models.CharField(max_length=20, help_text="Enter class and section", verbose_name="Class and Section")

    def __str__(self):
        return self.sec


class Year(models.Model):
    session = models.CharField(max_length=20, help_text="Enter academic session", verbose_name="Session")

    def __str__(self):
        return self.session


class Department(models.Model):
    dept = models.CharField(max_length=20, help_text="Enter department", verbose_name="Department")

    def __str__(self):
        return self.dept


MEMBER_TYPE = (
        ('STD', 'Student'),
        ('EMP', 'Employee'),
    )


class Member(models.Model):
    member_type = models.CharField( max_length=3, choices=MEMBER_TYPE, verbose_name="Member Type")
    card = models.CharField(unique=True, verbose_name="Card Number", max_length=20)
    si = models.PositiveIntegerField(unique= True, verbose_name="SI Number", null=True, blank=True)
    admission = models.PositiveIntegerField(unique=True, verbose_name="Admission Number", null=True, blank=True)
    employee = models.PositiveIntegerField(unique=True, verbose_name="Employee ID", null=True, blank=True)
    name = models.CharField(max_length=30)
    date_of_entry = models.DateField(default=date.today, verbose_name="Date of Entry")
    department = models.ForeignKey(Department, on_delete=models.PROTECT, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, blank=True, null=True)
    year = models.ForeignKey(Year, on_delete=models.PROTECT, blank=True, null=True)
    father = models.CharField(max_length=30, verbose_name="Father's Name", blank=True, null=True)
    phone = models.CharField(null=False, validators=[RegexValidator(r'\+?\d[\d -]{8,12}\d')], max_length=13, verbose_name="Phone No.")
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, help_text="abc@xyz.com")
    books_in_hand = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Books in Hand")
    books_issued = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Books Issued")
    textbooks_in_hand = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Textbooks in Hand")
    magazines_in_hand = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Magazines in Hand")
    late = models.PositiveSmallIntegerField(default=0, blank=True, null=True, verbose_name="Late Returns")
    remarks = models.CharField(max_length=200, default="NIL", verbose_name="Remarks", null=True)

    class Meta:
        verbose_name = "Member"

    def __str__(self):
        """String for representing model object"""
        return self.name
