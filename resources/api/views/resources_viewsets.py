from resources.api.serializers.resources_serializers import ResourceSerializer
from resources.models import Resource
from users.authentication_mixins import Authentication
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class ResourceViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    model_to_format = "Resource"

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    
    def list(self, request):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user

        if user.is_superuser:
            queryset = Resource.objects.filter(state=True)
        else:
            quota = user.quota
            if quota.max_resources:
                queryset = Resource.objects.filter(owner=user, state=True)[:quota.max_resources]
            else:
                queryset = Resource.objects.filter(owner=user, state=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            req_token = request.META['HTTP_AUTHORIZATION']
            user = Token.objects.get(key=req_token.split(" ")[1]).user

            if user.is_superuser:
                value = request.data['value']
                resource_obj = Resource.objects.create(value=value, owner=user)
                resource_obj.save()
                return Response({'message': '[+] {} created successfully.'.format(self.model_to_format)}, status=status.HTTP_201_CREATED)
            else:
                quota = user.quota
                if quota.max_resources and Resource.objects.filter(owner=user, state=True).count() > quota.max_resources:
                    return Response({'error':"[!] Resource quota exceeded."}, status=status.HTTP_400_BAD_REQUEST)
                value = request.data['value']
                resource_obj = Resource.objects.create(value=value, owner=user)
                resource_obj.save()
                return Response({'message': '[+] {} created successfully.'.format(self.model_to_format)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        req_token = request.META['HTTP_AUTHORIZATION']
        user = Token.objects.get(key=req_token.split(" ")[1]).user
        if user.is_superuser:
            resource = self.get_queryset().filter(id=pk).first()
            if resource:
                resource.state = False
                resource.save()
                return Response({'message':'[*] {} deleted successfully.'.format(self.model_to_format)}, status=status.HTTP_200_OK)
            return Response({'error':"[!] Doesn't exist a {} with that information.".format(self.model_to_format)}, status=status.HTTP_400_BAD_REQUEST)
        elif self.get_queryset().filter(id=pk).first().owner == user:
            resource = self.get_queryset().filter(id=pk).first()
            if resource:
                resource.state = False
                resource.save()
                return Response({'message':'[*] {} deleted successfully.'.format(self.model_to_format)}, status=status.HTTP_200_OK)
            return Response({'error':"[!] Doesn't exist a {} with that information.".format(self.model_to_format)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':"[!] Access denied to that resource."}, status=status.HTTP_401_UNAUTHORIZED)
