from rest_framework.viewsets import ModelViewSet
from account.serializers import UserProfileSerializer
from account.models import UserProfile


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.order_by('pk')
    serializer_class = UserProfileSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)