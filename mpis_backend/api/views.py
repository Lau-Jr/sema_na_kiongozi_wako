from rest_framework import status
from rest_framework.response import Response

from mpis_backend.api import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from mpis_backend import models
from django.http import JsonResponse, HttpResponse
from mpis_backend.api import utils
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError


class CreateMaoniAPIView(ListCreateAPIView):
    queryset = models.Maoni.objects.all()
    serializer_class = serializers.MaoniSerializer


class CheckMkoaAPIView(RetrieveAPIView):
    queryset = models.Jimbo.objects.all()

    def get(self, request, *args, **kwargs):
        if self.queryset.filter(mkoa=self.kwargs.get('mkoa')):
            result = {
                'jibu': True
            }
            return JsonResponse(result)
        else:
            result = {
                'jibu': False
            }
            return JsonResponse(result)


# class CreateMaoniAPIView(ListCreateAPIView):
#     queryset = models.Maoni.objects.all()
#     serializer_class = serializers.MaoniSerializer


class CheckJimboAPIView(RetrieveAPIView):
    queryset = models.Jimbo.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(mkoa=self.kwargs.get('mkoa'))
        if queryset.filter(id=self.kwargs.get('jimbo')):
            result = {
                'jibu': True
            }
            return JsonResponse(result)
        else:
            result = {
                'jibu': False
            }
            return JsonResponse(result)


class CheckSektaAPIView(RetrieveAPIView):
    queryset = models.Sekta.objects.all()

    def get(self, request, *args, **kwargs):
        if self.queryset.filter(jina=self.kwargs.get('jina')):
            result = {
                'jibu': True
            }
            return JsonResponse(result)
        else:
            result = {
                'jibu': False
            }
            return JsonResponse(result)


class SektaListAPIView(ListAPIView):
    queryset = models.Sekta.objects.all()

    def get(self, request, *args, **kwargs):
        m = self.queryset.all()
        serializer = serializers.SektaSerializer(m, many=True)
        sekta = utils.get_sekta(serializer.data)
        result = {'sekta': sekta}
        return JsonResponse(result)


class JimboListAPIView(ListAPIView):
    queryset = models.Jimbo.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.queryset.filter(mkoa=self.kwargs.get('mkoa'))
        serializer = serializers.JimboSerializer(queryset, many=True)
        majimbo = utils.get_majimbo(serializer.data)
        result = {'majimbo': majimbo}
        return JsonResponse(result)


def get_feedback(request, uname):
    # print(request.method)
    if request.method == 'GET':
        try:
            user = models.User.objects.get(username=uname)
        except models.User.DoesNotExist:
            result = {'error': 'username does not exist'}
            return JsonResponse(result)
        mbunge = models.Mbunge.objects.get(user=user)
        jimbo = mbunge.jimbo_id
        maoni = models.Maoni.objects.filter(jimbo=jimbo)
        serializer = serializers.MaoniSerializer(maoni, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        result = {'error': 'send get request'}
        return JsonResponse(result)


# @api_view(['POST', 'GET'])
# def create_user(request):
#     if request.method == 'POST':
#         print(request.data['username'])
#         print(request.data['passwd1'])
#         print(request.data['passwd2'])
#         return HttpResponse('thanks')


class CreateListUserAPIView(ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.RegistrationSerializer


class CreateMbugeAPIView(ListCreateAPIView):
    queryset = models.Mbunge.objects.all()
    serializer_class = serializers.MbugeSerializer


@api_view(['GET'])
def get_regions(request):
    if request.method == 'GET':
        regions = set(models.Jimbo.objects.values_list('mkoa', flat=True))
        result = {'regions': list(regions)}
        return JsonResponse(result)
    else:
        pass


@api_view(["POST"])
def create_rc(request):
    result = '''
    make sure you have included the following fields
    'username:'
    'password:' 
    'password2:'
    'region:' 
    '''
    if request.method == 'POST':
        data = request.data
        print(data)
        if is_valid_rc(data):
            try:
                rc = save(data)
            except ValidationError as error:
                result = error
                print(result)
                print(result.messages)
                return JsonResponse(data=result.messages, safe=False)
            return rc
        else:
            print(result)
            return JsonResponse(data=result, safe=False)
    else:
        print(result)


def is_valid_rc(data):
    valid = True
    username = data.get('username', 1)
    password = data.get('password', 1)
    password2 = data.get('password2', 1)
    region = data.get('region', 1)
    if username == 1 or password == 1 or password2 == 1 or region == 1:
        valid = False
        print(username, password, password2, region)
        print('invalid data')
        return valid
    else:
        print('data is valid')
        return valid


def save(validated_data):
    regions_from_db = set(models.Jimbo.objects.values_list('mkoa', flat=True))
    password = validated_data['password']
    password2 = validated_data['password2']
    region = validated_data['region']
    username = validated_data['username']
    user = models.User(username=username)
    if password != password2:
        raise ValidationError({"password": "Passwords must match."})
    user.set_password(password)
    user.save()
    if region not in regions_from_db:
        raise ValidationError({'region': 'region not found'})
    rc = models.RC(region=region, user=user)
    rc.save()
    return HttpResponse('RC is created successful', status=201)


@api_view(["POST"])
def create_region_commissioner(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        rc_serializer = serializers.UserSerializer(data=data)
        if rc_serializer.is_valid():
            rc_serializer.save()
            return Response(rc_serializer.errors, status=status.HTTP_201_CREATED)
        return Response(rc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass
