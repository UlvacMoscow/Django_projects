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
