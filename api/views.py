from ast import Return

from django.http import HttpResponse
from api.serializers import TaskSerializer
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
from tasks.models import Priority, Task,TaskBlock, CustomUser

from django.conf import settings

UserCustom=settings.AUTH_USER_MODEL
# Create your views here.

class TaskList(APIView):
    def get(self,request,format=None):
        all_tasks=Task.get_all_tasks()
        serializers=TaskSerializer(all_tasks,many=True)
        return Response(serializers.data)

    def post(self,request,format=None):
        serializers=TaskSerializer(data=request.data)
        task_block_id=request.data.get('task_block')
        assigned_to_id=request.data.get('assigned_to')
        priority_id=request.data.get('priority')
        task_block=TaskBlock.objects.get(pk=task_block_id)
        user=CustomUser.objects.get(pk=assigned_to_id)
        priority=Priority.objects.get(pk=priority_id)
        print(serializers)
        
        if serializers.is_valid():
            print('errrors')
            serializers.save(task_block=task_block,assigned_to=user,priority=priority)
            return Response(serializers.data,status=status.HTTP_201_CREATED)

        print(serializers.errors)
        return Response(status=status.HTTP_400_BAD_REQUEST)

