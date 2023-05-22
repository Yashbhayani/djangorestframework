from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import User, Book
from rest_framework.authtoken.models import Token
from .functions import handel_uploaded_file


# Create your views here.


@api_view(['GET'])
def home(request):
    print(request.headers['token'])
    userdata = User.objects.all()
    serializers = UserSerializer(userdata, many=True)
    return Response({'status': 200, 'data': serializers.data})


class BookAPI(APIView):
    def get(self, request):
        bookdata = Book.objects.all()
        serializers = BookSerializer(bookdata, many=True)
        return Response({'status': 200, 'data': serializers.data})

    def post(self, request):
        data = request.data
        print(data)
        serializers = BookSerializer(data=data)

        if not serializers.is_valid():
            return Response({'status': 403, 'message': 'Something went wrong!'})

        serializers.save()
        return Response({'status': 200, 'message': 'Data added'})

    def put(self, request):
        try:
            Book_obj = Book.objects.get(id=request.data['id'])
            serializers = BookSerializer(Book_obj, data=request.data)
            if not serializers.is_valid():
                return Response({'status': 403, 'message': 'Something went wrong!'})

            serializers.save()
            return Response({'status': 200, 'message': 'Data Updated'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Invalid Id'})

    def patch(self, request):
        try:
            Book_obj = Book.objects.get(id=request.data['id'])
            serializers = BookSerializer(Book_obj, data=request.data, partial=True)
            if not serializers.is_valid():
                return Response({'status': 403, 'message': 'Something went wrong!'})

            serializers.save()
            return Response({'status': 200, 'message': 'Data Updated'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Invalid Id'})

    def delete(self, request):
        # http://127.0.0.1:8000/book/?id=5
        try:
            id = request.GET.get('id')
            Book_obj = Book.objects.get(id=id)
            Book_obj.delete()
            return Response({'status': 200, 'message': 'Data Deleted !'})
        except Exception as e:
            return Response({'status': 403, 'message': 'Invalid Id'})
        
        
@api_view(['POST'])
def Post_FILE(request):
    handel_uploaded_file(request.FILES['image'])
    return Response({'status': 200, 'message': 'Data added'})

@api_view(['POST'])
def Post_FILE(request):
    handel_uploaded_file(request.FILES['image'])
    return Response({'status': 200, 'message': 'Data added'})



@api_view(['POST'])
def Post_User(request):
    data = request.data
    serializers = UserSerializer(data=data)
    email_user = User.objects.filter(email=data['email']).count()
    print(email_user)
    if email_user >= 1:
        return Response({'status': 403, 'message': 'Email id is already added'})

    if not serializers.is_valid():
        return Response({'status': 403, 'message': 'Something went wrong!'})
        
    serializers.save()
    return Response({'status': 200, 'message': 'Data added'})


@api_view(['PUT'])
def Update_User(request, id):
    try:
        User_obj = User.objects.get(id=id)
        serializers = UserSerializer(User_obj, data=request.data)
        if not serializers.is_valid():
            return Response({'status': 403, 'message': 'Something went wrong!'})

        serializers.save()
        return Response({'status': 200, 'message': 'Data Updated'})
    except Exception as e:
        return Response({'status': 403, 'message': 'Invalid Id'})


@api_view(['DELETE'])
def Delete_User(request, id):
    try:
        # i_d = request.GET.get('id')
        User_obj = User.objects.get(id=id)
        User_obj.delete()
        return Response({'status': 200, 'message': 'Data Deleted !'})
    except Exception as e:
        return Response({'status': 403, 'message': 'Invalid Id'})
