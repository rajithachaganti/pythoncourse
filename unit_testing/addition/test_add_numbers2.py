
from unittest import TestCase
from addition.add_numbers2 import Addition

class TestAddition(TestCase):

    def setUp(self) -> None:
        print("----Setup method-----")
        self.obj = Addition()  # 1. object creation

    # unit test case
    def test_add(self):
        print("----test_add method-----")
        # 2. Prepare arguments
        n1 = 10
        n2 = 20
        act_res = self.obj.add(n1, n2)  # 3
        exp_res = 32  # our assumption in mind
        self.assertEqual(exp_res, act_res, 'Both should be equal')


'''
unittest framework 
When you execute TestAddition class 
  - 1. Python will create object for TestAddition i.e, TestAddition()
    2. TestAddition().setUp()
    3. TestAddition().test_add()
    
'''





