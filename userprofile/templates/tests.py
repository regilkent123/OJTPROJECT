from django.test import TestCase
from django.contrib.auth.models import User


class CreateProfileTestCase(TestCase):

    def test_create(self):
        user = User.objects.create_user(username='asd', password='asd')
        print(user.userprofile)
