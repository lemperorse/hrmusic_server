from django.contrib import admin
from django.utils.safestring import mark_safe
from dal import autocomplete

from exercise.models import Program, Plan, HeartSong, Goal, Duration, InPlan
from adminsortable2.admin import SortableAdminMixin,SortableInlineAdminMixin
from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple


# Register your models here.

class DurationInline(SortableInlineAdminMixin,admin.TabularInline):
    model = Duration
    list_display = ['no','place']

class ProgramAdmin(admin.ModelAdmin):
    inlines = (DurationInline,)
    change_form_template = 'program.html'
    list_display = ['name', 'difficulty']
    list_filter = ['difficulty'] 

    pass

admin.site.register(Program,ProgramAdmin)

admin.site.register(InPlan)



from dal import autocomplete

from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = InPlan
        fields = ('__all__')
        widgets = {
            'program': autocomplete.ModelSelect2( )
        }

class InPlanInline(SortableInlineAdminMixin,admin.TabularInline):
    model = InPlan
    form = PersonForm
    list_display = ['no','program']
class PlanAdmin(admin.ModelAdmin):
    inlines = (InPlanInline,)
    # change_form_template = 'plan.html'
    list_display = ['name', 'coach_name', ]
    search_fields = ['name', 'coach_name', ]
    # filter_horizontal = ('program',)
    # list_filter = ['program', ]

    # def formfield_for_manytomany(self, db_field, request=None, **kwargs):
    #     if db_field.name == 'program':
    #         kwargs['widget'] = SortedFilteredSelectMultiple()
    #     return super(PlanAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)


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


class GoalAdmin(admin.ModelAdmin):
    list_display = ['user', 'plan', 'running_distance', 'race_date']
    list_filter = ['plan', 'race_date', 'running_distance']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'plan__name', 'running_distance']

admin.site.register(Goal,GoalAdmin)

class DurationAdmin(admin.ModelAdmin):
    list_display = ['no','place','duration','rest','rest_duration','reps','program_name','program_name','level']
    list_filter = ['program','program__difficulty',]
    search_fields = ['no', 'place','program__name']
admin.site.register(Duration,DurationAdmin)
