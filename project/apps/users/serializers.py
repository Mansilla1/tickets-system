from rest_framework import (
    fields,
    serializers,
)


class UserSerializer(serializers.Serializer):
    username = fields.CharField(max_length=150, required=True)
