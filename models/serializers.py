from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['is_superadmin', 'is_admin']

class UserBanSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['is_ban']

class UserActiveSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['is_active']

class PersonalDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'region', 'district', 'phone_number']


class UpdateFirstNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']

class UpdateLastNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['last_name']

class UpdateRegionSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['region']


class UpdateDistrictSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['district']


class UpdatePhoneNumberSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number']


class ScoresSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['math_score', 'iq_score', 'english_score', 'total_score']


class OlimpiadaSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['olimpiada']

class ExcelSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['telegram_id', 'is_active', 'first_name', 'last_name', 'tg_full_name', 'tg_username', 'region', 'district', 'phone_number', 'olimpiada', 'create_time']


class ExcelGrandSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['telegram_id', 'is_active', 'first_name', 'last_name', 'tg_full_name', 'tg_username', 'region', 'district', 'phone_number', 'total_score', 'english_score', "math_score", "iq_score",  'create_time']