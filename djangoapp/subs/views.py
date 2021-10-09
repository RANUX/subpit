from rest_framework import generics
import requests
from .serializers import SubscriberSerializer
from django.core.mail import send_mail
from django.conf import settings

class CreateSubscriberView(generics.CreateAPIView):
    serializer_class = SubscriberSerializer

    def _send_telegram(self, message):
        bot_token = getattr(settings, "TELEGRAM_BOT_TOKEN", '')
        bot_chat_id = getattr(settings, "TELEGRAM_BOT_CHAT_ID", '')

        if not (bot_token and bot_chat_id):
            return

        send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chat_id}&parse_mode=Markdown&text={message}'

        response = requests.get(send_text)
        return response.json()


    def _send_email(self, message):
        recipient_list = getattr(settings, "NOTIFS_EMAIL_RECIPIENT_LIST", [])
        if recipient_list:
            send_mail(
                        subject=f'New subscriber',
                        message=message,
                        from_email=None,
                        recipient_list=recipient_list,
                        html_message=message,
                    )

    def post(self, request, *args, **kwargs):
        message_func = getattr(settings, "NOTIFS_MESSAGE_FUNC", None)
        if message_func:
            message = message_func(request)
        else:
            message = f'New subscriber {request.data.get("name")} from host {request.data.get("host")}.'
        
        self._send_email(message)
        self._send_telegram(message)

        return self.create(request, *args, **kwargs)
