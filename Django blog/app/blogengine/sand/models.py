from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)

    # по related_name можно получить связанную модель в любую сторону
    def get_groups(self):
        return self.groups.all()

    def get_groups_related_set():
        # user.group_set.all() если related name не задан
        pass

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(User, related_name='groups')


class Vampire(models.Model):
    name = models.CharField(max_length=128)
    damage = models.IntegerField()
    groups = models.ManyToManyField(GroupVampire, related_name='inGroupVampire')


class GroupVampire(models.Model):
    name = models.CharField(max_length=128)
    flying = models.BooleanField(default=True)


class Zombie(models.Models):
    name = models.CharField(max_length=128)
    groups = models.ManyToManyField(GroupZombie, related_name='inGroupZombie')


class GroupZombie(models.Model):
    name = models.CharField(max_length=128)


class Ghost(models.Model):
    name = models.CharField(max_length=128)


class GroupGhost(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Ghost, through='Ghostship')


class Ghostship(models.Model):
    ghost = models.ForeignKey(Ghost, on_delete=models.CASCADE)
    GroupGhost = models.ForeignKey(GroupGhost, on_delete=models.CASCADE)
    data_joined = models.DateField()
    invite_reason = models.CharField()
