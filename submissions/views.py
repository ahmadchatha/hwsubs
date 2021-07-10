import django_filters
from rest_framework import viewsets
from rest_framework import permissions
from hwsubs.permissions import IsOwnerOrIsStaff
from submissions.serializers import SubmissionSerializer
from submissions.models import Submission


class SubmissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Submission to be viewed or edited.
    """
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsStaff]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = {'grade': ['exact', 'isnull'], 'grade__final_grade': ['exact'], 'assignment__name': ['exact'],
                     'created': ['gte', 'lte', 'exact']}

    def get_queryset(self):
        """
        This view should return a list of all the submission
        of a student. Otherwise return all for staff.
        """
        user = self.request.user
        queryset = Submission.objects.all().order_by('created')

        if not user.is_staff:
            queryset = Submission.objects.filter(creator=user).order_by('created')

        return queryset

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)