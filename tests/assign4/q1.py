from kit103_assign4 import q1


def print_result(question, answer, expected):
	if answer == expected:
		print(f"Answer to q1['{question}'] is correct: {answer}")
	else:
		print(f"Answer to q1['{question}'] is incorrect; should be {expected} instead of {answer}")


for part in 'ab':
	oct_key = 'file ' + part.upper()
	bin_key = f'{part.lower()}-1 bitset'

	oct_val = int(q1[oct_key], 8)

	print_result(
		question=bin_key,
		expected=bin(q1[bin_key]),
		answer=bin(oct_val)
	)

print()

perm_checks = [
	('a-2 g+w?', 0b000010000),
	('a-3 g+x?', 0b000001000),
	('a-4 o+r?', 0b000000100),
	('b-2 u+w?', 0b010000000),
	('b-3 g+r?', 0b000100000),
	('b-4 o+r?', 0b000000100),
]

for question, check in perm_checks:
	bitset = q1[question[0] + '-1 bitset']

	print_result(
		question=question,
		expected=bitset & check > 0,
		answer=q1[question]
	)