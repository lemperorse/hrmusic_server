from rest_framework.viewsets import ModelViewSet
from exercise.serializers import HeartSongSerializer, ProgramSerializer, DurationSerializer, PlanSerializer, \
    GoalSerializer, GoalViewSerializer, PlanViewSerializer
from exercise.models import HeartSong, Program, Duration, Plan, Goal
from rest_framework import generics,filters
from django_filters.rest_framework import DjangoFilterBackend, BaseInFilter, NumberFilter

class HeartSongViewSet(ModelViewSet):
    queryset = HeartSong.objects.order_by('pk')
    serializer_class = HeartSongSerializer


class ProgramViewSet(ModelViewSet):
    queryset = Program.objects.order_by('pk')
    serializer_class = ProgramSerializer


class DurationViewSet(ModelViewSet):
    queryset = Duration.objects.order_by('pk')
    serializer_class = DurationSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ['program', ]


class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.order_by('pk')
    serializer_class = PlanSerializer


class GoalViewSet(ModelViewSet):
    queryset = Goal.objects.order_by('pk')
    serializer_class = GoalSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = [ 'user',]

class PlanAllViewSet(ModelViewSet):
    queryset = Plan.objects.order_by('pk')
    serializer_class = PlanViewSerializer

class GoalAllViewSet(ModelViewSet):
    queryset = Goal.objects.order_by('pk')
    serializer_class = GoalViewSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = [ 'user',]