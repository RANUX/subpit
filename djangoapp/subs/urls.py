from django.urls import path
from .views import CreateSubscriberView

app_name = 'subs'

urlpatterns = [
    path('create/', CreateSubscriberView.as_view(), name='create'),
]