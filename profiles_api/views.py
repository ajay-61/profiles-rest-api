from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test api view"""
    
    def get(self, request, format=None):
        """Returns a list of apiview features"""
       
        an_apiview = [
            'uses http methods',
            'hi this is ajay',
            'sdasd sdas'
        ]

        return Response({'message':'Hello!','an_apiview': an_apiview})