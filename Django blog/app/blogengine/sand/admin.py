from django.contrib import admin
from sand.models import Ghost, Ghostship, Group, GroupGhost, GroupVampire, GroupZombie, User, Vampire, Zombie
# Register your models here.


class GhostAdmin(admin.ModelAdmin):
    list_display = ['name']


class GhostshipAdmin(admin.ModelAdmin):
    list_display = ('ghost', 'GroupGhost', 'data_joined', 'invite_reason')


class GroupGhostAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Ghost, GhostAdmin)
admin.site.register(Ghostship, GhostshipAdmin)
admin.site.register(GroupGhost, GroupGhostAdmin)
