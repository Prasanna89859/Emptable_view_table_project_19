from django.db import models

# Create your models here.

class EmployeeTable(models.Model):
    Empo = models.IntegerField(primary_key=True)
    Ename = models.CharField(max_length=100)
    Job = models.IntegerField()
    Mgr = models.IntegerField()
    Hire = models.DateField()
    Sal = models.IntegerField()
    Comm = models.IntegerField()
    Dept = models.IntegerField()
    def __str__(self):
        return  self.Ename
    


class Dept(models.Model):
    Deptno = models.OneToOneField(EmployeeTable,on_delete = models.CASCADE)
    D_name = models.CharField(max_length=50)
    Loc = models.CharField(max_length=200)
    def __str__(self):
        return str(self.pk)
    
class salgrade(models.Model):
    Grade = models.IntegerField(primary_key=True)
    Losal = models.IntegerField()
    Hisal = models.IntegerField()
    def __str__(self):
        return str(self.pk)

    




    



