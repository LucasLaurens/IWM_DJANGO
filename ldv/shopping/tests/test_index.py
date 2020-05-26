from django.test import TestCase, Client

from shopping.models import Clothes, User
from . import STATUS_CODE

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/shopping/"
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        Clothes.objects.create(name="name", description="description", price=50)

    def test_get_not_logged(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)

    def test_get_logged(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.OK)

        clothes = response.context['clothes']
        self.assertEqual(len(clothes), 1)

    def test_post(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)