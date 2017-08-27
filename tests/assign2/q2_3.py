import kit103_assign2 as assign2
from truthtable import TruthTable

questions = {'a': 2, 'b': 4, 'c': 3, 'd': 1}

for q, var_count in questions.items():
	predicate1 = getattr(assign2, 'q2_' + q)
	predicate2 = getattr(assign2, 'q3_' + q)

	result1 = TruthTable(var_count, predicate1)
	result2 = TruthTable(var_count, predicate2)

	result1.print(result2)

	if result1 == result1:
		print(f'Passed: question {q} has the same result for the two predicates.')
	else:
		print(f'Failed: question {q} has different results for the two predicates.')

	print()
