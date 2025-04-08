from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        try:
            # Clear existing data using Django ORM
            User.objects.all().delete()
            Team.objects.all().delete()
            Activity.objects.all().delete()
            Leaderboard.objects.all().delete()
            Workout.objects.all().delete()

            # Create users
            users = [
                User(
                    _id=ObjectId(),
                    username='thundergod',
                    email='thundergod@mhigh.edu',
                    password='thundergodpassword'
                ),
                User(
                    _id=ObjectId(),
                    username='metalgeek',
                    email='metalgeek@mhigh.edu',
                    password='metalgeekpassword'
                ),
                User(
                    _id=ObjectId(),
                    username='zerocool',
                    email='zerocool@mhigh.edu',
                    password='zerocoolpassword'
                ),
                User(
                    _id=ObjectId(),
                    username='crashoverride',
                    email='crashoverride@mhigh.edu',
                    password='crashoverridepassword'
                ),
                User(
                    _id=ObjectId(),
                    username='sleeptoken',
                    email='sleeptoken@mhigh.edu',
                    password='sleeptokenpassword'
                ),
            ]
            User.objects.bulk_create(users)

            # Create teams and assign members
            team1 = Team(_id=ObjectId(), name='Blue Team')
            team2 = Team(_id=ObjectId(), name='Gold Team')
            team1.save()
            team2.save()
            # Since members is an ArrayReferenceField, we append users to the list
            team1.members = [users[0], users[1], users[2]]  # First 3 users to Blue Team
            team2.members = [users[3], users[4]]  # Last 2 users to Gold Team
            team1.save()
            team2.save()

            # Create activities
            activities = [
                Activity(
                    _id=ObjectId(),
                    user=users[0],
                    activity_type='Cycling',
                    duration=60,
                    calories_burned=300.0,
                    date=date.today() - timedelta(days=1)
                ),
                Activity(
                    _id=ObjectId(),
                    user=users[1],
                    activity_type='Crossfit',
                    duration=120,
                    calories_burned=600.0,
                    date=date.today() - timedelta(days=2)
                ),
                Activity(
                    _id=ObjectId(),
                    user=users[2],
                    activity_type='Running',
                    duration=90,
                    calories_burned=450.0,
                    date=date.today() - timedelta(days=3)
                ),
                Activity(
                    _id=ObjectId(),
                    user=users[3],
                    activity_type='Strength',
                    duration=30,
                    calories_burned=150.0,
                    date=date.today() - timedelta(days=4)
                ),
                Activity(
                    _id=ObjectId(),
                    user=users[4],
                    activity_type='Swimming',
                    duration=75,
                    calories_burned=375.0,
                    date=date.today() - timedelta(days=5)
                ),
            ]
            Activity.objects.bulk_create(activities)

            # Create leaderboard entries
            leaderboard_entries = [
                Leaderboard(team=team1, points=100),
                Leaderboard(team=team2, points=80),
            ]
            Leaderboard.objects.bulk_create(leaderboard_entries)

            # Create workouts
            workouts = [
                Workout(
                    name='Cycling Training',
                    description='Training for a road cycling event',
                    duration=60,
                    calories_burned=300.0
                ),
                Workout(
                    name='Crossfit',
                    description='Training for a crossfit competition',
                    duration=120,
                    calories_burned=600.0
                ),
                Workout(
                    name='Running Training',
                    description='Training for a marathon',
                    duration=90,
                    calories_burned=450.0
                ),
                Workout(
                    name='Strength Training',
                    description='Training for strength',
                    duration=30,
                    calories_burned=150.0
                ),
                Workout(
                    name='Swimming Training',
                    description='Training for an olympic swimming competition',
                    duration=75,
                    calories_burned=375.0
                ),
            ]
            Workout.objects.bulk_create(workouts)

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}'))
            raise