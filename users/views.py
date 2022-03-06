from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from db import mydb

class UserAPI(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = mydb.auth_user.find()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        print("**************")
        print(request.data)
        print(UserSerializer(request.data))
        # print(UserSerializer(request.data).is_valid())
        print("**************")

        return Response(status=status.HTTP_201_CREATED)
        
