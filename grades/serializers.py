from rest_framework import serializers
from grades.models import Grade
from submissions.models import Submission


class GradeSerializer(serializers.HyperlinkedModelSerializer):
    submission = serializers.HyperlinkedRelatedField(view_name='submission-detail', queryset=Submission.objects.all())
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Grade
        fields = ['created', 'creator', 'notes', 'final_grade', 'submission']