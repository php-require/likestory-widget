from rest_framework.views import APIView
from rest_framework.response import Response

class likeAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = [{"id":1, "name":"vasja"},{"id":2, "name":"petja"}]
        return Response(data)