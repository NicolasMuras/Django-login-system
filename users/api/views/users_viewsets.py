from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from users.authentication_mixins import Authentication
from users.api.serializers.users_serializers import RegisterUserSerializer, UserSerializer
from users.models import Quota


class UserViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = UserSerializer


    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter()


    def list(self, request):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user

        if user.is_superuser:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': '[!] Not authorized.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    def create(self, request):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user

        if user.is_superuser:
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': '[+] User created successfully.'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '[!] Not authorized.'}, status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, pk=None):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user

        if user.is_superuser:
            user = self.get_queryset().filter(id=pk, is_active=True).first()
            if user:
                user.is_active = False
                user.save()
                return Response({'message':'[*] User deleted successfully.'}, status=status.HTTP_200_OK)
            return Response({'error':"[!] Doesn't exist an active User with that information."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '[!] Not authorized.'}, status=status.HTTP_401_UNAUTHORIZED)
        
    @action(detail=True, methods=['put'])
    def quota(self, request, pk):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user

        if user.is_superuser:
            user = self.get_queryset().filter(id=pk, is_active=True).first()
            if user:
                quota = Quota.objects.filter(user=user)[0]
                quota.max_resources = request.data['quota']
                quota.save()
                return Response({'message':'[*] User quota updated successfully.'}, status=status.HTTP_200_OK)
            return Response({'error':"[!] Doesn't exist an active User with that information."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': '[!] Not authorized.'}, status=status.HTTP_401_UNAUTHORIZED)
