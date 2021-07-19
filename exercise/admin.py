from django.contrib import admin
from exercise.models import Program, Plan, HeartSong, Goal, Duration
from adminsortable2.admin import SortableAdminMixin,SortableInlineAdminMixin


# Register your models here.

class DurationInline(SortableInlineAdminMixin,admin.TabularInline):
    model = Duration
    list_display = ['no','place']

class ProgramAdmin(admin.ModelAdmin):
    inlines = (DurationInline,)
    list_display = ['name', 'difficulty']
    list_filter = ['difficulty']

    pass

admin.site.register(Program,ProgramAdmin)

class PlanAdmin(admin.ModelAdmin):
    list_display = ['name','coach_name','number_day']
    filter_horizontal = ('program',)

admin.site.register(Plan,PlanAdmin)

class HeartSongAdmin(admin.ModelAdmin):
    list_display = ['place', 'song', 'heartrate_start','heartrate_end']
    list_filter = ['place']
    fieldsets = (
        ('Song And HeartRate', {
            'fields': ('song','place', ('heartrate_start', 'heartrate_end'))
        }),
    )

admin.site.register(HeartSong,HeartSongAdmin)

admin.site.register(Goal)
admin.site.register(Duration)
