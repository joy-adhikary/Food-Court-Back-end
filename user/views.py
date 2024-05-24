from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import LoginModel, RegistrationModel
from .serializer import LoginSerializer, RegisterSerializers


class UserLogin(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = LoginModel.objects.get(id =request.data['id'] )
            print('user => ',user)
            if user:
                if user.password == request.data['password'] and user.username == request.data['username']:
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





