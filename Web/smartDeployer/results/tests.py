from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from .views import *

class MyTests(TestCase):
	def setUp(self):
		self.client = Client()
	def test_main_page(self):
		url = reverse('index')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Results')


	def test_team_page(self):
		request = 'fake request'
		response = team(request)
		self.assertEqual(response.status_code, 200)


	def test_about_page(self):
		request = 'fake request'
		response = about(request)
		self.assertEqual(response.status_code, 200)

	def test_help_page(self):
		request = 'fake request'
		response = help(request)
		self.assertEqual(response.status_code, 200)
