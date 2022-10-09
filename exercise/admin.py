from django.contrib import admin
from django.shortcuts import redirect
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from dal import autocomplete

from exercise.models import Program, Plan, HeartSong, Goal, Duration, InPlan, RunMain, RunResult
from adminsortable2.admin import SortableAdminMixin,SortableInlineAdminMixin
# from sortedm2m_filter_horizontal_widget.forms import SortedFilteredSelectMultiple
from dal import autocomplete

from django import forms


# Register your models here.

class DurationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DurationForm, self).__init__(*args, **kwargs)
        # self.fields['program'].queryset = Program.objects.filter(user=self.user)
        self.fields['duration'].widget.attrs.update({'placeholder': 'hh:mm:ss'})
        self.fields['rest_duration'].widget.attrs.update({'placeholder': 'hh:mm:ss'})

    class Meta:
        model = Duration
        fields = ('__all__')
        # widgets = {
        #     'body': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        # }
    pass

class DurationInline(SortableInlineAdminMixin,admin.TabularInline):
    model = Duration
    list_display = ['no','place']
    form = DurationForm

class ProgramAdmin(admin.ModelAdmin):
    inlines = (DurationInline,)
    change_form_template = 'program.html'
    list_display = ['name', 'difficulty','user','created_at']
    list_filter = ['difficulty','user','created_at']

    def has_change_permission(self, request, obj=None):
        return obj is None or obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.user == request.user

    def changelist_view(self, request, extra_context=None):
        referrer = request.META.get('HTTP_REFERER', '')
        get_param = '{}={}'.format("user__id__exact",str(request.user.id))
        if len(request.GET) == 0 and '?' not in referrer:
            return redirect("{url}?{get_parms}".format(url=request.path, get_parms=get_param))
        return super(ProgramAdmin, self).changelist_view(request, extra_context=extra_context)

    pass

admin.site.register(Program,ProgramAdmin)

admin.site.register(InPlan)





class ProgramWidget(autocomplete.ModelSelect2):
    def get_queryset(self):
        def get_queryset(self):
            # Don't forget to filter out results depending on the visitor !
            if not self.request.user.is_authenticated:
                return Program.objects.none()

            qs = Program.objects.all()

            if self.q:
                qs = qs.filter(name__istartswith=self.q)
            return qs



class ProgramForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        # self.fields['program'].queryset = Program.objects.filter(user=self.user)


    class Meta:
        model = InPlan
        fields = ('__all__')
        widgets = {
            'program': autocomplete.ModelSelect2(),
        }


class InPlanInline(SortableInlineAdminMixin,admin.TabularInline):
    model = InPlan
    form = ProgramForm
    list_display = ['no','program']

    # def get_queryset(self, request):
    #     qs = super(InPlanInline).get_queryset(request)
    #     return qs.filter(program__user=request.user)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "program":
            kwargs["queryset"] = Program.objects.filter(user=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class PlanAdmin(admin.ModelAdmin):
    inlines = (InPlanInline,)
    change_form_template = 'plan.html'
    list_display = ['name', 'coach_name', 'user' ,'created_at']
    search_fields = ['name', 'coach_name', 'user','created_at' ]
    list_filter = ['user','created_at' ]
    def has_change_permission(self, request, obj=None):
        return obj is None or obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj is None or obj.user == request.user

    def changelist_view(self, request, extra_context=None):
        referrer = request.META.get('HTTP_REFERER', '')
        get_param = '{}={}'.format("user__id__exact",str(request.user.id))
        if len(request.GET) == 0 and '?' not in referrer:
            return redirect("{url}?{get_parms}".format(url=request.path, get_parms=get_param))
        return super(PlanAdmin, self).changelist_view(request, extra_context=extra_context)


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




class RunResultInline(admin.TabularInline):
    model = RunResult
    list_display = ['hr_bpm','hr_zone','music_bpm','music_zone','music']


class RunMainAdmin(admin.ModelAdmin):
    inlines = (RunResultInline,)
    change_form_template = 'runmain.html'
    list_display = ['user', 'goal', 'plan', 'program']
    list_filter = ['plan', 'program', 'created_at']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'plan__name', 'program__name']

admin.site.register(RunMain,RunMainAdmin)
# admin.site.register(RunResult)