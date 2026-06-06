from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from web.models.user import UserProfile
from web.models.character import Character


class CreateCharacterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user = request.user
            user_profile = UserProfile.objects.get(user=user)

            name = request.data.get('name', '').strip()
            profile = request.data.get('profile', '')[:100000]
            photo = request.FILES.get('photo')
            background = request.FILES.get('background')

            if not name:
                return Response({'result': '名字不能为空'})
            if not profile:
                return Response({'result': '角色介绍不能为空'})
            if not photo:
                return Response({'result': '头像不能为空'})
            if not background:
                return Response({'result': '聊天背景不能为空'})

            Character.objects.create(
                author=user_profile,
                name=name,
                profile=profile,
                photo=photo,
                background=background,
            )

            return Response({'result': 'success'})

        except:
            return Response({'result': '系统异常，请稍后重试'})
