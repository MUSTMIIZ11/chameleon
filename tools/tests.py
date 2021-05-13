from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from signup.models import User
from community.models import Map


class ToolTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='nick', password='123')

    def test_map_create(self):
        Map.objects.create(map_name='map', map_url='', user_id=self.user.id)


