from rest_framework import serializers, status
from user.models import LoginModel, RegistrationModel
from rest_framework.response import Response


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ['username','password']


    def validate(self, request):
        username = request['username']
        password = request['password']

        if not username and password :
            return Response({
                    'status': False,
                    'message': 'Username or Password is missing'
                }, status.HTTP_400_BAD_REQUEST)
        
        return request


class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistrationModel
        fields = '__all__'

    def validate(self, request):
        # check if user email already exists or not 
        if request['email']:
            email = request['email']
            if RegistrationModel.objects.filter(email=email).exists():
                raise serializers.ValidationError({'Massage': 'Ops!!! User Email already exists'})
            
        # check if user already exists or not 
        if request['username']:
            username = request['username']
            if RegistrationModel.objects.filter(username = username).exists():
                raise serializers.ValidationError({'Massage': 'Ops!!! User already exists'})
            
        return request

