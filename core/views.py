from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])
def ping(request):
    """
    A simple view to check if the server is running.
    """
    return Response({"message": "pong"}, status=200)
