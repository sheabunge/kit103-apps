from math import gcd as real_gcd
from kit103_assign3 import q2_factor_gcd as gcd
from tests.assign3.random_tests import random_tests


random_tests('gcd', gcd, real_gcd, n_inputs=2, min=2, max=10e5, print_passed=True)
