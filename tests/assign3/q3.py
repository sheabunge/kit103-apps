from math import gcd
from kit103_assign3 import q3_coprime
from tests.assign3.random_tests import random_tests

random_tests('coprime', q3_coprime, lambda a, b: gcd(a, b) == 1, n_inputs=2, min=2, max=10e2, print_passed=True)
