from kit103_assign5 import value_ans


pairs = [
	('q1 a', 'q1 b'),
	('q1 c', 'q1 d'),
	('q2 a', 'q2 b'),
	('q2 c', 'q2 d'),
	('q3 d', 'q3 c'),
]


for a_len, a_sol in pairs:
	if value_ans[a_len] != len(value_ans[a_sol]):
		print(f'Failure: the number in [{a_len}] does not match the number of elements generated in [{a_sol}]')
	else:
		print(f'Success: the number in [{a_len}] matches the number of elements generated in [{a_sol}]')
