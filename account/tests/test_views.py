from django.test import Client, TestCase

from account.models import CustomUser, SourcePoints


class ListingViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_return_10_users_on_one_page(self):
        for x in range(0, 10):
            CustomUser.objects.create(email=f'test{x}@wp.pl', username=f'{x}')
        response = self.client.get('/')
        self.assertEqual(len(response.context_data["object_list"]), 10)

    def test_should_return_8_users_on_one_page(self):
        for x in range(0, 8):
            CustomUser.objects.create(email=f'test{x}@wp.pl', username=f'{x}')
        response = self.client.get('/')
        self.assertEqual(len(response.context_data["object_list"]), 8)

    def test_should_return_18_users_on_two_pages(self):
        for x in range(0, 18):
            CustomUser.objects.create(email=f'test{x}@wp.pl', username=f'{x}')
        response = self.client.get('/')
        self.assertEqual(len(response.context_data["object_list"]), 10)
        self.assertEqual(response.context_data["paginator"].num_pages, 2)

    def test_should_not_return_any_users(self):
        response = self.client.get('/')
        self.assertEqual(len(response.context_data["object_list"]), 0)
        self.assertEqual(response.status_code, 200)


class ChangBalanceTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_should_return_200_when_user_exist_get_method(self):
        user = CustomUser.objects.create(email='test1@wp.pl',
                                         username='test', id=14)
        response = self.client.get(f'/change-balance/{user.id}')

        self.assertEqual(response.status_code, 200)

    def test_should_return_404_when_user_does_not_exist_get_method(self):
        response = self.client.get('/change-balance/11111')

        self.assertEqual(response.status_code, 404)
