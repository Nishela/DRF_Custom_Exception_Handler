from rest_framework import serializers

from custom_api.exceptions import ApiException, ChildApiException


class CustomSerializer(serializers.Serializer):
    custom_field = serializers.IntegerField()

    def validate(self, attrs):
        super().validate(attrs)
        if attrs['custom_field'] == 0:
            raise ApiException
        elif attrs['custom_field'] == 1:
            raise ChildApiException
        return attrs
