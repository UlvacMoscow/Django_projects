from django.contrib import admin
from sand.models import Ghost, Ghostship, Group, GroupGhost, GroupVampire, GroupZombie, User, Vampire, Zombie, GroupElements
# Register your models here.


class GroupVampireAdmin(admin.ModelAdmin):
    list_display = ['name', 'flying']

class VampireAdmin(admin.ModelAdmin):
    list_display = ['name', 'damage', 'health']

class GhostAdmin(admin.ModelAdmin):
    list_display = ['name']


class GhostshipAdmin(admin.ModelAdmin):
    list_display = ('ghost', 'GroupGhost', 'data_joined', 'invite_reason')


class GroupGhostAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(GroupVampire, GroupVampireAdmin)
admin.site.register(Vampire, VampireAdmin)
admin.site.register(Ghost, GhostAdmin)
admin.site.register(Ghostship, GhostshipAdmin)
admin.site.register(GroupGhost, GroupGhostAdmin)

class GroupElementsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(GroupElements, GroupElementsAdmin)
