import datetime

from rest_framework import serializers

from .models import Role, Degree, Employee


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = "__all__"

    def validate(self, value):
        if len(value['name']) == 0:
            raise serializers.ValidationError("Field 'name' cannot be empty!")
        if len(value['name']) > 50:
            raise serializers.ValidationError("Field 'name' cannot be longer than 50 characters!")


class DegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"

    def validate(self, value):
        if len(value['name']) == 0:
            raise serializers.ValidationError("Field 'name' cannot be empty!")
        if len(value['name']) > 100:
            raise serializers.ValidationError("Field 'name' cannot be longer than 100 characters!")


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

    def validate(self, value):
        if len(value['first_name']) == 0:
            raise serializers.ValidationError("Field 'first_name' cannot be empty!")
        if len(value['first_name']) > 50:
            raise serializers.ValidationError("Field 'first_name' cannot be longer than 50 characters!")
        if len(value['last_name']) == 0:
            raise serializers.ValidationError("Field 'last_name' cannot be empty!")
        if len(value['last_name']) > 50:
            raise serializers.ValidationError("Field 'last_name' cannot be longer than 50 characters!")
        if value['employed_at'] > datetime.datetime.now(): #TODO check if it's correct in logic way
            raise serializers.ValidationError("Field 'employed_at' cannot be placed in the future")



