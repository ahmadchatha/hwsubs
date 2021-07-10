import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from hwsubs.permissions import StudentReadOnly
from assignments.serializers import AssignmentSerializer
from assignments.models import Assignment


class AssignmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assigmnets to be viewed or edited.
    """
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, StudentReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = {'name': ['exact'], 'submissions': ['isnull'], 'submissions__grade': ['isnull']}

    def get_queryset(self):
        """
        This view should return a list of all the assignments
        for a particular student. Otherwise just return all for staff
        """
        user = self.request.user
        queryset = Assignment.objects.all().order_by('created')

        if not user.is_staff:
            queryset = Assignment.objects.filter(group__user=user).order_by('created')

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)