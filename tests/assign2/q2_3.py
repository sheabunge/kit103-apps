import kit103_assign2 as assign2
from truthtable import TruthTable

questions = {'a': 2, 'b': 4, 'c': 3, 'd': 1}

for q, var_count in questions.items():
	print()

	predicate1 = getattr(assign2, 'q2_' + q)
	predicate2 = getattr(assign2, 'q3_' + q)

	result1 = TruthTable(var_count, predicate1)
	result2 = TruthTable(var_count, predicate2)

	result1.print(result2, labels=('2.' + q, '3.' + q))

	out1, out2 = ('Pass', 'identical') if result1 == result2 else ('Fail', 'different')
	print(f'{out1}ed: Question {q.upper()} has {out2} results for the two predicates.')
	print()
