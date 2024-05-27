from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import LoginModel, RegistrationModel
from .serializer import LoginSerializer, RegisterSerializers
from django.contrib.auth.hashers import check_password 
from django.contrib.auth.hashers import make_password


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
        # Noob version 
        # if serializer.is_valid():
        #     user_object = RegistrationModel.objects.get(username =request.data['username'] )
        #     print('user => ',user_object)
        #     if user_object:
        #         if user_object.password == request.data['password'] and user_object.username == request.data['username']:
        #             serializer.save()
        #             return Response({
        #                 'message': 'Login sucessful'}, 
        #                 status=status.HTTP_200_OK
        #                 )
                
        #         return Response({
        #             "Message": 'Incorrect data'}, 
        #             status=status.HTTP_406_NOT_ACCEPTABLE
        #             )
                
        # return Response({
        #             "Message": serializer.errors}, 
        #             status=status.HTTP_406_NOT_ACCEPTABLE
        #             )  

        if serializer.is_valid():
            username = request.data.get('username')
            password = request.data.get('password')

            try:
                user_object = RegistrationModel.objects.get(username=username)
            except RegistrationModel.DoesNotExist:
                return Response({
                    "Message": "Username does not exist"},
                    status=status.HTTP_404_NOT_FOUND)

            # print(user_object.username ,user_object.password, " => " , request.data)

            if check_password(password, user_object.password):  
                return Response({
                    "message": "Login successful",
                    "user_id": user_object.uid}, 
                    status=status.HTTP_200_OK)
            else:
                return Response({
                    "Message": "Incorrect password"}, 
                    status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                "Message": serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST)


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
            username = serializer.validated_data.get('username')
            raw_password = serializer.validated_data.get('password')
            email = serializer.validated_data.get('email')

            hashed_password = make_password(raw_password)

            user = RegistrationModel(password=hashed_password,email=email,username=username)
            user.save()

            return Response({
                        'message': 'Registration sucessfull',
                        'data': serializer.data}, 
                        status=status.HTTP_200_OK
                        )
                
        return Response({
                    "Message": serializer.errors}, 
                    status=status.HTTP_406_NOT_ACCEPTABLE
                    )  

