from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
import unittest
from .views import *
from django.test import SimpleTestCase
from django.template import Context, Template



class MainTests(TestCase):
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
		self.assertContains(response, 'Zhipeng')


	def test_about_page(self):
		request = 'fake request'
		response = about(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Cassandra')

	def test_help_page(self):
		request = 'fake request'
		response = help(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'components')


	def test_workloadA_page(self):
		response = self.client.get('http://127.0.0.1:8000/results/workloada')
		self.assertContains(response, '', status_code=301)

	def test_workloadB_page(self):
		response = self.client.get('http://127.0.0.1:8000/results/workloadb')
		self.assertContains(response, '', status_code=301)

	def test_workloadC_page(self):
		response = self.client.get('http://127.0.0.1:8000/results/workloadc')
		self.assertContains(response, '', status_code=301)

	def test_workloadD_page(self):
		response = self.client.get('http://127.0.0.1:8000/results/workloadd')
		self.assertContains(response, '', status_code=301)



