from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .serializers import TaskSerializer, CategorySerializer
from .models import Task, Category
from .pagination import TasksPagination
from .filters import TaskFilter

# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TasksPagination
    filterset_class = TaskFilter

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer