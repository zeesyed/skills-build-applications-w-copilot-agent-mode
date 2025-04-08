# Models for OctoFit Tracker
from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Use ObjectIdField as the primary key
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)  # Reference to User model
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # Add ObjectIdField as the primary key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.team.name} - {self.points} points"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # in minutes
    calories_burned = models.FloatField()

    def __str__(self):
        return self.name
