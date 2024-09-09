from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import generics
# Create your views here.

class CreateUser(APIView):
    def get(self, request):
        users = models.User.objects.all()
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = serializers.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailOPS(APIView):
    def get(self, request, id):
        user = models.User.objects.get(id=id)
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        user = get_object_or_404(models.User,id=id)
        serializer = serializers.UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status==status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        user = get_object_or_404(models.User,id=id)
        serializer = serializers.UserSerializer(user, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status==status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = models.User.objects.get(id=id)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Now I will be creating tasks and user views 

class CreateTask(APIView):
    def get(self, request, id):
        user = get_object_or_404(models.User, id=id)
        tasks = models.Task.objects.filter(user=user)
        serializer =serializers.TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, id):
        user = get_object_or_404(models.User, id=id)
        data1 = request.data.copy()
        data1['user'] = user.id
        serializer = serializers.TaskSerializer(data=data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetDetailedTask(APIView):
    def get(self, request, user_id, task_id):
        user = get_object_or_404(models.User, id=user_id)
        task = get_object_or_404(models.Task, id=task_id, user=user)
        serializer = serializers.TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def put(self, request, user_id, task_id):
        user = get_object_or_404(models.User, id=user_id)
        task = get_object_or_404(models.Task, id=task_id, user=user)
        serializer = serializers.TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, user_id, task_id):
        user = get_object_or_404(models.User, id=user_id)
        task = get_object_or_404(models.Task, id=task_id, user=user)
        serializer = serializers.TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, user_id, task_id):
        user = get_object_or_404(models.User, id=user_id)
        task = get_object_or_404(models.Task, id=task_id, user=user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserTasksFilter(APIView):
     def get(self, request,user_id):
         user = get_object_or_404(models.User, id=user_id)
         status1 = request.query_params.get('status', 'false')
         if status1.lower() == 'false':
             task = models.Task.objects.filter(user=user,status=False)
         else:
             task = models.Task.objects.filter(user=user,status=True)
         serializer = serializers.TaskSerializer(task, many=True)
         return Response(serializer.data,status=status.HTTP_200_OK )