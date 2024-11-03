from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.sessions.models import Session
from waffle.models import Flag, Switch, Sample
from axes.models import AccessLog, AccessAttempt, AccessFailureLog

admin.site.unregister(get_user_model())
admin.site.unregister(Group)
admin.site.unregister(Flag)
admin.site.unregister(Switch)
admin.site.unregister(Sample)
admin.site.unregister(AccessLog)
admin.site.unregister(AccessAttempt)
admin.site.unregister(AccessFailureLog)


@admin.register(AccessLog)
class AccessLogAdmin(ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(ModelAdmin):
    pass


@admin.register(AccessAttempt)
class AccessAttempAdmin(ModelAdmin):
    pass


@admin.register(AccessFailureLog)
class AccessFailureLogAdmin(ModelAdmin):
    pass


@admin.register(get_user_model())
class UserAdmin(ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass


@admin.register(Flag)
class FlagAdmin(ModelAdmin):
    pass


@admin.register(Switch)
class SwitchAdmin(ModelAdmin):
    pass


@admin.register(Sample)
class SampleAdmin(ModelAdmin):
    pass
