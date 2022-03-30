import json

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from core.auth.serializers import LoginSerializer
from CoreRoot.consumers  import ChatConsumer
from channels.layers import get_channel_layer

from asgiref.sync import async_to_sync

class ComissionViewSet(ModelViewSet, TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.query_params)
        layer = get_channel_layer()
        async_to_sync(layer.group_send)('events', {
            'type': 'events.alarm',
            'content': 'triggered',
            'new_comission_address':request.query_params['comission_address'],
            'new_comission_rate':request.query_params['comission_percentage']
        })


        return Response('', status=status.HTTP_200_OK)


