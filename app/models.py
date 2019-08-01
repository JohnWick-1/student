from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_nu=models.CharField(max_length=50)
    dob=models.DateField()
    country=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    password=models.CharField(max_length=50)
# s=Student(first_name='abc',last_name='zxc',phone_nu=123458,dob='2009-07-07',country='india',status=0)

    def __str__(self):
        # self.__dict__.pop('_state')
        return f'{self.__dict__}'
    def __repr__(self):
        return str(self)

    class Meta:
        db_table='Student_info'
