from django.test import TestCase, Client

from shopping.models import Clothes, User
from . import STATUS_CODE

class DetailTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/shopping/{id}"
        self.username = "user"
        self.password = "password"
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.clothe = Clothes.objects.create(name="name", description="description", price=50)

    def test_get_not_logged(self):
        response = self.client.get(self.url.format(id=self.clothe.id))

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)
        self.assertEqual(self.user.items.count(), 0)

    def test_get_logged(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url.format(id=self.clothe.id))

        self.assertEqual(response.status_code, STATUS_CODE.OK)
        self.assertEqual(response.context['clothe'], self.clothe)

        self.assertEqual(self.user.items.count(), 1)
        self.assertEqual(self.user.items.first().clothe, self.clothe)

    def test_get_logged_invalid_id(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url.format(id=42))

        self.assertEqual(response.status_code, STATUS_CODE.NOT_FOUND)
        self.assertFalse(response.context.get('clothe', False))

        self.assertEqual(self.user.items.count(), 0)

    def test_post(self):
        response = self.client.post(self.url.format(id=42))

        self.assertEqual(response.status_code, STATUS_CODE.REDIRECTED)