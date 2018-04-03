from django.test import TestCase
from .models import WorkloadA,WorkloadB,WorkloadC,WorkloadD

class WorkloadATest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_workloadA_entry(self):
        workloadA = WorkloadA(workload=10)
        self.assertEqual(workloadA.workload, 10)

    def test_workloadB_entry(self):
        workloadB = WorkloadB(workload=10)
        self.assertEqual(workloadB.workload, 10)

    def test_workloadC_entry(self):
        workloadC = WorkloadC(workload=10)
        self.assertEqual(workloadC.workload, 10)

    def test_workloadD_entry(self):
        workloadD = WorkloadD(workload=10)
        self.assertEqual(workloadD.workload, 10)
