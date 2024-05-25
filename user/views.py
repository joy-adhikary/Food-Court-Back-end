from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import LoginModel, RegistrationModel
from .serializer import LoginSerializer, RegisterSerializers


class UserLogin(APIView):

    def get(self,request):
        allUser = LoginModel.objects.all()
        serializer = LoginSerializer(allUser,many=True)
        return Response({
            'data': serializer.data},
            status=status.HTTP_200_OK
            )

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_object = RegistrationModel.objects.get(username =request.data['username'] )
            print('user => ',user_object)
            if user_object:
                if user_object.password == request.data['password'] and user_object.username == request.data['username']:
                    serializer.save()
                    return Response({
                        'message': 'Login sucessful'}, 
                        status=status.HTTP_200_OK
                        )
                
                return Response({
                    "Message": 'Incorrect data'}, 
                    status=status.HTTP_406_NOT_ACCEPTABLE
                    )
                
        return Response({
                    "Message": serializer.errors}, 
                    status=status.HTTP_406_NOT_ACCEPTABLE
                    )  


class UserRegistration(APIView):

    def get(self,request):
        data = RegistrationModel.objects.all();
        serializer = RegisterSerializers(data, many=True)
        
        return Response({
            'data': serializer.data},
            status=status.HTTP_200_OK
            )

    def post(self, request):
        serializer = RegisterSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({
                        'message': 'Registration sucessfull',
                        'data': serializer.data
                        }, 
                        status=status.HTTP_200_OK
                        )
                
        return Response({
                    "Message": serializer.errors}, 
                    status=status.HTTP_406_NOT_ACCEPTABLE
                    )  





