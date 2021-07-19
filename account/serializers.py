from rest_framework.serializers import ModelSerializer
from account.models import UserProfile


class UserProfileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
