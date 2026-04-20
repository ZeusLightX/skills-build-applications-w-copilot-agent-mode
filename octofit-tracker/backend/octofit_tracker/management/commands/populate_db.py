from django.core.management.base import BaseCommand

from octofit_tracker.models import Team, Activity, Leaderboard, Workout, OctoUser

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        for model in [Activity, Leaderboard, Workout, OctoUser, Team]:
            for obj in model.objects.all():
                if getattr(obj, 'pk', None):
                    obj.delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (Superheroes)

        users = [
            {'username': 'ironman', 'email': 'ironman@marvel.com', 'team': marvel},
            {'username': 'captainamerica', 'email': 'cap@marvel.com', 'team': marvel},
            {'username': 'spiderman', 'email': 'spiderman@marvel.com', 'team': marvel},
            {'username': 'batman', 'email': 'batman@dc.com', 'team': dc},
            {'username': 'superman', 'email': 'superman@dc.com', 'team': dc},
            {'username': 'wonderwoman', 'email': 'wonderwoman@dc.com', 'team': dc},
        ]
        user_objs = []
        for u in users:
            user = OctoUser.objects.create(username=u['username'], email=u['email'], team=u['team'])
            user_objs.append(user)

        # Create Activities
        activities = [
            Activity.objects.create(user=user_objs[0], type='Run', duration=30, calories=300),
            Activity.objects.create(user=user_objs[1], type='Swim', duration=45, calories=400),
            Activity.objects.create(user=user_objs[2], type='Bike', duration=60, calories=500),
            Activity.objects.create(user=user_objs[3], type='Run', duration=25, calories=250),
            Activity.objects.create(user=user_objs[4], type='Swim', duration=50, calories=450),
            Activity.objects.create(user=user_objs[5], type='Bike', duration=70, calories=600),
        ]

        # Create Workouts
        Workout.objects.create(name='Morning Cardio', description='A quick morning cardio routine')
        Workout.objects.create(name='Strength Training', description='Full body strength workout')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
