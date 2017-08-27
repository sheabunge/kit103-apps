from kit103_assign2 import q4_acme_letter_detector
from truthtable import TruthTable


def q4_original(a, b, c, d):
	return \
		(not a and not b and not c and d) or \
		(not a and not b and c and d) or \
		(not a and b and not c and not d) or \
		(not a and b and c and d) or \
		(a and not b and c and d) or \
		(a and b and c and d)

original = TruthTable(4, q4_original)
answer = TruthTable(4, q4_acme_letter_detector)

original.print(answer, labels=('original', 'optimised'))

if original == answer:
	print('Success! The answer matches the original predicate.')
else:
	print('Whoops! The answer does not match the original predicate.')
