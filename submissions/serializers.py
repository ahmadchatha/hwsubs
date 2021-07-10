from rest_framework import serializers
from submissions.models import Submission


class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Submission
        fields = ['id', 'created', 'creator', 'link', 'assignment']