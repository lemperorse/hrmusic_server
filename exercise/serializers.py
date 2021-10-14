from rest_framework.serializers import ModelSerializer
from exercise.models import HeartSong, Program, Duration, Plan, Goal


class HeartSongSerializer(ModelSerializer):

    class Meta:
        model = HeartSong
        fields = '__all__'


class ProgramSerializer(ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'


class DurationSerializer(ModelSerializer):

    class Meta:
        model = Duration
        fields = '__all__'


class PlanSerializer(ModelSerializer):

    class Meta:
        model = Plan
        fields = '__all__'


class GoalSerializer(ModelSerializer):

    class Meta:
        model = Goal
        fields = '__all__'
class ProgramViewSerializer(ModelSerializer):

    class Meta:
        model = Program
        fields = '__all__'



class PlanViewSerializer(ModelSerializer):
    program = ProgramViewSerializer(many=True)
    class Meta:
        model = Plan
        fields = '__all__'

class GoalViewSerializer(ModelSerializer):
    plan = PlanViewSerializer(read_only=True)
    class Meta:
        model = Goal
        fields = '__all__'
