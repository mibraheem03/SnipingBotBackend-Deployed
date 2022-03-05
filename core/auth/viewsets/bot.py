from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework import viewsets
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


class BotViewSet(viewsets.ViewSet, TokenRefreshView):
    permission_classes = (AllowAny,)
    http_method_names = ['get']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        serializer.validated_data['bot'] = {"BotName": "Bot One"}
        print(serializer.validated_data)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):

        information = make_json()
        print("Bot Data")
        print(information)

        #serializer = self.get_serializer(data=request.data)
#
        #try:
        #    serializer.is_valid(raise_exception=True)
        #except TokenError as e:
        #    raise InvalidToken(e.args[0])
        serializer = {"BotName": "Bot One"}
        return Response(serializer, status=status.HTTP_200_OK)