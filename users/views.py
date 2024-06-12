from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, AddYourSelfSerializer, \
    PaperInformationSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .models import User, PaperInformation
from rest_framework import status
from django.shortcuts import get_object_or_404


class LoginView(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)
        user = User.objects.filter(email=email).first()
        if user is not None:
            return Response(
                {
                    'id': user.id,
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'affiliation': user.affiliation,
                }
            )
        else:
            return Response(
                {
                    'success': False,
                    'message': "email or password is incorrect",
                }
            )
        

class RegisterView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

    

class AddYourSelfView(APIView):
    def get(self, request):
        add_your_self = User.objects.all()
        serializer = AddYourSelfSerializer(add_your_self, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AddYourSelfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddYourSelfDetailView(APIView):
    def get(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            add_your = get_object_or_404(User, id=id)
        except:
            return Response(data='Not found', status=status.HTTP_404_NOT_FOUND)
        add_your.delete()
        return Response(data='Successfully deleted', status=status.HTTP_200_OK)



class AddAuthorView(APIView):
    def get(self, request):
        add_your_self = User.objects.all()
        serializer = AddYourSelfSerializer(add_your_self, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AddYourSelfSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AddAuthorDetailView(APIView):
    def get(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        add_your_self = get_object_or_404(User, id=id)
        serializer = AddYourSelfSerializer(add_your_self, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            add_your = get_object_or_404(User, id=id)
        except:
            return Response(data='Not found', status=status.HTTP_404_NOT_FOUND)
        add_your.delete()
        return Response(data='Successfully deleted', status=status.HTTP_200_OK)
    


class PaperInformationView(APIView):
    def get(self, request):
        paper_information = PaperInformation.objects.all()
        serializer = PaperInformationSerializer(paper_information, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PaperInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PaperInformationDetailView(APIView):
    def get(self, request, id):
        paper_information = get_object_or_404(PaperInformation, id=id)
        serializer = PaperInformationSerializer(paper_information)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        paper_information = get_object_or_404(PaperInformation, id=id)
        serializer = PaperInformationSerializer(paper_information, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        paper_information = get_object_or_404(PaperInformation, id=id)
        serializer = PaperInformationSerializer(paper_information, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            paper_information = get_object_or_404(PaperInformation, id=id)
        except:
            return Response(data='Not found', status=status.HTTP_404_NOT_FOUND)
        paper_information.delete()
        return Response(data='Successfully deleted', status=status.HTTP_200_OK)