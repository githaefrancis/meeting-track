from django.conf import settings
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

UserCustom=settings.AUTH_USER_MODEL

class CustomUser(AbstractUser):
    '''
    Class that defines the custom fields for the user table
    '''
    designation=models.CharField(max_length=50,blank=True)
    phone=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.username

class TaskBlock(models.Model):
    created_by=models.ForeignKey(UserCustom,related_name='task_block',on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    block_title=models.CharField(max_length=100)
    block_description=models.CharField(max_length=500,blank=True)

    def add_task(self):
        self.save()
        return self

    def __str__(self):
        return self.block_title



class Priority(models.Model):
    priority_name=models.CharField(max_length=20)
    priority_description=models.CharField(max_length=50)

    def __str__(self):
        return self.priority_name
class Task(models.Model):
    task_ref=models.CharField(max_length=50)
    task_block=models.ForeignKey(TaskBlock,related_name='task_in_block',on_delete=models.CASCADE)
    content=models.TextField()
    assigned_to=models.ForeignKey(UserCustom,related_name='task',on_delete=models.CASCADE)
    initial_date=models.DateField(blank=True)
    new_target_date=models.DateField(blank=True)
    status=models.CharField(max_length=50)
    progress=models.CharField(max_length=10)
    comment=models.CharField(max_length=50)
    priority=models.ForeignKey(Priority,related_name='taskpriority',on_delete=models.CASCADE)

    def add_task(self):
        self.save()
        return self
    
    def __str__(self):
        return self.task_name

    @classmethod
    def get_all_tasks(cls):
        return cls.objects.all()

class SubTask(models.Model):
    task_ref=models.CharField(max_length=50)
    content=models.TextField()
    assigned_to=models.ForeignKey(UserCustom,related_name='subtask',on_delete=models.CASCADE)
    initial_date=models.DateField(blank=True)
    new_target_date=models.DateField(blank=True)
    status=models.CharField(max_length=50)
    progress=models.CharField(max_length=10)
    comment=models.CharField(max_length=50)
    priority=models.ForeignKey(Priority,related_name='subtask_priority',on_delete=models.CASCADE)

    def add_subtask(self):
        self.save()
        return self

    def __str__(self):
        return self.task_name