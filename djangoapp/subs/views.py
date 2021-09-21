from rest_framework import generics
from .serializers import SubscriberSerializer


class CreateSubscriberView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer
