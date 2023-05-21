from rest_framework import serializers
from datetime import date

from ..patients.models import Patient, Allergy, Time_of_activity


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"

    def validate(self, value):
        if value['first_name'] == 0:
            raise serializers.ValidationError("Field 'first_name' cannot be empty!")
        if len(value['first_name']) > 50:
            raise serializers.ValidationError("Field 'first_name' cannot have more than 50 characters!")
        if value['last_name'] == 0:
            raise serializers.ValidationError("Field 'last_name' cannot be empty!")
        if len(value['last_name']) > 50:
            raise serializers.ValidationError("Field 'last_name' cannot have more than 50 characters!")
        if value['email'] == 0:
            raise serializers.ValidationError("Field 'email' cannot be empty!")
        if len(value['email']) > 50:
            raise serializers.ValidationError("Field 'email' cannot have more than 50 characters!")
        if value['password'] == 0:
            raise serializers.ValidationError("Field 'password' cannot be empty!")
        if len(value['password']) > 255:
            raise serializers.ValidationError("Field 'password' cannot have more than 255 characters!")
        if len(value['pesel']) != 11:
            raise serializers.ValidationError("Field 'pesel' has to be exactly 11 characters long!")
        if len(value['phone_number']) != 11:
            raise serializers.ValidationError("Field 'phone_number' has to be exactly 11 characters long!")
        if (value['age']) <= 0:
            raise serializers.ValidationError("Field 'age' cannot be empty or negative number!")
        if value['age'] > 100:
            raise serializers.ValidationError("Field 'age' cannot be than 100 number!")
        return value


class AllergySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergy
        fields = "__all__"

    def validate(self, value):
        if value['name'] == 0:
            raise serializers.ValidationError("Field 'name' cannot be empty!")
        if len(value['name']) > 45:
            raise serializers.ValidationError("Field 'name' cannot have more than 11 characters!")
        return value


class TimeOfActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Time_of_activity
        fields = "__all__"

    def validate(self, value):  # TODO Do we need additional validation here?
        if value['date_start'] < date.today():  # TODO check if it's correct in logic way
            raise serializers.ValidationError("Field 'date_start' cannot be placed in the future!")
        if value['date_start'] > value['date_end']:
            raise serializers.ValidationError("Field 'date_start' cannot be placed after date_end!")
        if value['date_end'] < date.today():  # TODO check if it's correct in logic way
            raise serializers.ValidationError("Field 'data_end' cannot be placed in the past!")
        return value