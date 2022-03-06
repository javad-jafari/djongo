from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    confirm_password = serializers.CharField(write_only = True)


    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        print("************************")
        print(validated_data)
        print("************************")
        return "ok"