import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from hwsubs.permissions import StudentReadOnly
from grades.serializers import GradeSerializer
from grades.models import Grade


class GradeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows assigmnets to be viewed or edited.
    """
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated, StudentReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('final_grade', 'submission__assignment__name', )

    def get_queryset(self):
        """
        This view should return a list of all the assignments
        for a particular student. Otherwise just return all for staff
        """
        user = self.request.user
        queryset = Grade.objects.all().order_by('created')

        if not user.is_staff:
            queryset = Grade.objects.filter(submission__creator=user).order_by('created')

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)