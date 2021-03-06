from rest_framework.serializers import ModelSerializer, SerializerMethodField
from exercise.models import HeartSong, Program, Duration, Plan, Goal, InPlan, RunMain, RunResult


class HeartSongSerializer(ModelSerializer):

    class Meta:
        model = HeartSong
        fields = '__all__'

class DurationSerializer(ModelSerializer):

    class Meta:
        model = Duration
        fields = '__all__'

class ProgramSerializer(ModelSerializer):
    durations = SerializerMethodField()
    class Meta:
        model = Program
        fields = '__all__'
    def get_durations(self,obj):
        try:
            durations = Duration.objects.filter(program=obj.id).order_by('no')
            durations = DurationSerializer(durations,many=True)
            return durations.data
        except:
            return None





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

class InPlanSerializer(ModelSerializer):
    class Meta:
        model = InPlan
        fields = '__all__'


class PlanViewSerializer(ModelSerializer):
    program = SerializerMethodField()
    class Meta:
        model = Plan
        fields = '__all__'
    def get_program(self,obj):
        inPlans = InPlan.objects.filter(plan=obj.id).order_by('no')
        programs = []
        for plan in inPlans:
            program_set = Program.objects.get(id=plan.program.id)
            program_data = ProgramViewSerializer(program_set).data
            program_data['no'] = plan.no
            programs.append(program_data)

        return programs



class GoalViewSerializer(ModelSerializer):
    plan = PlanViewSerializer(read_only=True)
    class Meta:
        model = Goal
        fields = '__all__'

class RunResultSerializer(ModelSerializer):
    class Meta:
        model = RunResult
        fields = '__all__'

class RunMainSerializer(ModelSerializer):
    result = SerializerMethodField(read_only=True)
    class Meta:
        model = RunMain
        fields = '__all__'
    def get_result(self, obj):
        try:
            data = RunResult.objects.filter(run_main=obj.id).order_by('id')
            data = RunResultSerializer(data, many=True)
            return data.data
        except:
            return None


