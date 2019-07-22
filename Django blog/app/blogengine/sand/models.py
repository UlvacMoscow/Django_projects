from django.db import models

# Create your models here.


class GroupElements(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name

class GroupVampire(models.Model):
    name = models.CharField(max_length=128)
    flying = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Vampire(models.Model):
    name = models.CharField(max_length=128)
    damage = models.IntegerField()
    health = models.IntegerField()
    groups = models.ManyToManyField(GroupVampire, related_name='inGroupVampire')

    def __str__(self):
        return self.name


class GroupZombie(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Zombie(models.Model):
    name = models.CharField(max_length=128)
    groups = models.ManyToManyField(GroupZombie, related_name='inGroupZombie')

    def __str__(self):
        return self.name


class Ghost(models.Model):
    name = models.CharField(max_length=128)


    def __str__(self):
        return self.name

    def my_elements(self):
        return self.group_set.all()


class GroupGhost(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Ghost, through='Ghostship')
    element = models.ForeignKey(GroupElements, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ghostship(models.Model):
    ghost = models.ForeignKey(Ghost, on_delete=models.CASCADE)
    GroupGhost = models.ForeignKey(GroupGhost, on_delete=models.CASCADE)
    data_joined = models.DateField()
    invite_reason = models.CharField(max_length=128)

