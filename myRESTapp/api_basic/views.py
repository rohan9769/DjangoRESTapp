from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article,Student
from .serializers import ArticleSerializer,StudentSerializer
from django.views.decorators.csrf import csrf_exempt

#api_views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins


#Generics
class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    
    def put(self,request,id=None):
        return self.update(request,id)


#classbased api_views
class ArticleAPIView(APIView):
    def get(self,request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    def post(self,request):
         serializer = ArticleSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
         else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailsAPIView(APIView):
    def get_object(self,id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self,request,id):
         article = self.get_object(id)
         serializer = ArticleSerializer(article,data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StudentDetailsAPIView(APIView):
    def get(self,request):
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
#Using api_view() decorator in Functional based views
#Function based API Views
@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# # Create your views here.
# @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         else:
#             return JsonResponse(serializer.errors,status=400)

# def student_list(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students,many=True)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         else:
#             return JsonResponse(serializer.errors,status=400)

# @csrf_exempt
# def article_detail(request,pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return JsonResponse(serializer.data,safe=False)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticleSerializer(article,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors,status=400)
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)
    