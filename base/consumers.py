import json

from channels.generic.websocket import AsyncWebsocketConsumer, SyncConsumer
from asgiref.sync import sync_to_async
from .models import Profile, User, Notification, ForumPost
from channels.db import database_sync_to_async

users_websockets = {}


class NotiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        users_websockets[self.scope['user'].id] = self

    async def disconnect(self, close_code):
        del users_websockets[self.scope['user'].id]

    async def receive(self, text_data):
        message = json.loads(text_data)
        action = message.get('action')

        if action == 'update_profile':
            profile = await self.get_user_profile()
            if profile:
                profile.unread_notifications = False
                await self.save_profile(profile)
        elif action == 'notify_update':
            targeted_user_id = message.get('target_user_id')
            forum = message.get('forum')
            info = await self.create_notification(targeted_user_id, forum)
            await self.send_notification(targeted_user_id, info)

    async def send_notification(self, targeted_user_id, info):
        if targeted_user_id in users_websockets:
            targeted_user_socket = users_websockets[targeted_user_id]
            await targeted_user_socket.send(
                text_data=json.dumps({
                    'action': 'notify_update',
                    'sender': info['sender'],
                    'forum_name': info['forum_name'],
                    'forum': info['forum'],
                    'text': info['text'],
                    'picture':'static'+info['picture']
                }))

    @database_sync_to_async
    def get_user_profile(self):
        user = self.scope["user"]
        try:
            profile = Profile.objects.get(user=user)
            return profile
        except Profile.DoesNotExist:
            return None

    @database_sync_to_async
    def save_profile(self, profile):
        profile.save()

    @database_sync_to_async
    def create_notification(self, targeted_user_id, forum):
        sender = User.objects.get(id=self.scope["user"].id)
        receiver = User.objects.get(id=targeted_user_id)
        profile = Profile.objects.get(user=sender)
        forum = ForumPost.objects.get(id=forum)
        Notification.objects.create(receiver=receiver,
                                    sender=sender.username,
                                    forum=forum,
                                    text="respondeu à sua dúvida",
                                    notification_image=profile.profile_picture)
        return {
            'sender': sender.username,
            'forum_name': forum.title,
            'forum': forum.id,
            'text': "respondeu à sua dúvida",
            'picture':profile.profile_picture.url
        }
