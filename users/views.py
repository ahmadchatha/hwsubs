from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from hwsubs.permissions import StudentReadOnly
from users.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, StudentReadOnly]

    def get_queryset(self):
        """
        This view should return a list of all the users
        if the user is a staff member. Otherwise just the user itself
        """
        user = self.request.user
        queryset = User.objects.all().order_by('-date_joined')

        if not user.is_staff:
            queryset = User.objects.filter(id=user.id)

        return queryset

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]