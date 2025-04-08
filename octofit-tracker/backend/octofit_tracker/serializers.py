from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

# Custom field to handle MongoDB ObjectId
class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = User
        fields = ['_id', 'username', 'email', 'created_at']  # Exclude password for security

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    members = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members', 'created_at']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer(read_only=True)  # Expand the user object

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration', 'calories_burned', 'date']

class LeaderboardSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)  # Expand the team object

    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points', 'updated_at']  # Use 'id' since Leaderboard uses Django's default PK

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'duration', 'calories_burned']  # Use 'id' since Workout uses Django's default PK