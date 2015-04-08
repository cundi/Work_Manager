from rest_framework import serializers

from Work_Manager.tasks_manager.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'time_elapsed', 'importance', 'project', 'developer')