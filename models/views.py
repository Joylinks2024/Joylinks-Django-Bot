from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


@api_view(['GET', 'POST'])
def UserList(request):
    if request.method == 'GET':
        snippets = User.objects.filter(is_active=True)
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def TopSoreUserList(request):
    if request.method == 'GET':
        snippets = User.objects.filter(is_active=True, total_score__gte=60) \
                       .order_by('-total_score', '-create_time')[:10]
        serializer = UserSerializer(snippets, many=True)
        ser_data = serializer.data
        if len(ser_data) <= 9:
            ser_data = []
            return Response(ser_data, status=status.HTTP_404_NOT_FOUND)
        return Response(ser_data, status.HTTP_200_OK)


@api_view(['GET'])
def NextTopSoreUserList(request):
    if request.method == 'GET':
        snippets = User.objects.filter(is_active=True, total_score__gte=60) \
                       .order_by('-total_score', '-create_time')[10:20]
        serializer = UserSerializer(snippets, many=True)
        ser_data = serializer.data
        if len(ser_data) <= 9:
            ser_data = []
            return Response(ser_data, status=status.HTTP_404_NOT_FOUND)
        return Response(ser_data)


@api_view(['GET', 'PUT', 'DELETE'])
def UserDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def ScoreList(request):
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = ScoresSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ScoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ScoreDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ScoresSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ScoresSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PermissionDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PermissionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PermissionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def UserBanDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserBanSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserBanSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def UserActiveDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserActiveSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserActiveSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PersonalDataDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonalDataSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalDataSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def FirstNameDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateFirstNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateFirstNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def LastNameDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateLastNameSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateLastNameSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def RegionDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateRegionSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateRegionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def DistrictDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdateDistrictSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdateDistrictSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def PhoneNumberDetail(request, telegram_id):
    try:
        user = get_object_or_404(User, telegram_id=telegram_id)
    except User.DoesNotExist:
        return Response(None, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UpdatePhoneNumberSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UpdatePhoneNumberSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
