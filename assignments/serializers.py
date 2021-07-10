from rest_framework import serializers
from assignments.models import Assignment


class AssignmentSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Assignment
        fields = ['id', 'created', 'creator', 'description', 'group', 'name']