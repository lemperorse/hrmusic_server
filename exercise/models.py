from django.db import models

from account.models import UserProfile

ZONE = [(1,'Zone 1'),(2,'Zone 2'),(3,'Zone 3'),(4,'Zone 4')]
DIFFICULTY = [(1,'Easy'),(2,'Moderate'),(3,'Hard')]


def getLevel(diff):
    if(diff == 1):
        return 'Easy'
    elif (diff == 2):
        return 'Moderate'
    elif (diff == 3):
        return 'Hard'
    else:
        return '-'


class HeartSong(models.Model):
    song = models.FileField(blank=True,null=True)
    place = models.IntegerField(choices=ZONE)
    heartrate_start = models.FloatField(default=60 , max_length=120)
    heartrate_end = models.FloatField(default=100,max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.place)

# Create your models here.


class Program(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField(choices=DIFFICULTY)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.name, getLevel(self.difficulty))


class Duration(models.Model):

    no = models.PositiveIntegerField(default=0)
    place = models.IntegerField(choices=ZONE)
    duration = models.TimeField()
    rest = models.IntegerField(choices=ZONE)
    rest_duration = models.TimeField()
    reps = models.IntegerField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    class Meta(object):
        ordering = ['no']

    def __str__(self):
        return '{} ({})'.format(self.program.name, getLevel(self.program.difficulty))

    @property
    def program_name(self):
        return '{}'.format(self.program.name)

    @property
    def level(self):
        return '{}'.format(getLevel(self.program.difficulty))


class Plan(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    coach_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    number_day = models.IntegerField(default=1)
    day_traning_program = models.DateField(blank=True,null=True)
    program = models.ManyToManyField(Program)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def count_program(self):
        return '{}'.format(self.program)


class Goal(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    running_distance = models.IntegerField(default=1)
    race_date = models.DateField(blank=True,null=True)
    plan = models.ForeignKey(Plan,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)