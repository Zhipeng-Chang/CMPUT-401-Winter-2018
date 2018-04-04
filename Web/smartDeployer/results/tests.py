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

		request = 'fake request'
		response = workloada(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'WorkloadA')




	def test_workloadB_page(self):

		request = 'fake request'
		response = workloadb(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'WorkloadB')




	def test_workloadC_page(self):

		request = 'fake request'
		response = workloadc(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'WorkloadC')




	def test_workloadD_page(self):

		request = 'fake request'
		response = workloadd(request)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'WorkloadD')



