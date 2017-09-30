from kit103_assign4 import select_key, decrypt


def print_result(function_name, params, expected, actual):
	function_name += f"({', '.join(map(repr, params))})"

	if expected == actual:
		print(f'Success: {function_name} returns {expected!r}')
	else:
		print(f'Failure: {function_name} should return {expected!r} instead of {actual!r}')


tests = [
	('123456789', 10),
	('HELP', 26),
	('ATOZ', 36),
	('ZTOA', 36),
]

for message, base in tests:
	print_result(
		'select_key',
		[message], base,
		select_key(message)
	)

print()

tests = [
	(123456789, 10, '123456789'),
	(308827, 26, 'HELP'),
	(505043, 36, 'ATOZ'),
	(606045923, 36, 'A TO Z'),
]

for encrypted, base, decrypted in tests:
	print_result(
		'decrypt',
		(encrypted, base), decrypted,
		decrypt(encrypted, base)
	)
