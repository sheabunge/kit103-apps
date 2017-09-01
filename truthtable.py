from string import ascii_lowercase


class TruthTable:

	def __init__(self, variables, predicate=None):
		self.table = {}

		if isinstance(variables, int):
			self.var_count = variables
			self.var_names = ascii_lowercase[:variables]
		else:
			self.var_names = variables
			self.var_count = len(variables)

		if predicate:
			self.fill(predicate)

	def add_row(self, var_values, result):
		if var_values in self.table:
			raise ValueError(f'row {var_values!r} already exists in table')
		self.table[var_values] = result

	def fill(self, predicate):
		for n in range(2 ** self.var_count):
			bits = bin(n)[2:].zfill(self.var_count)
			variables = tuple(bool(int(bit)) for bit in bits)
			result = predicate(*variables)
			self.add_row(variables, result)

	def __eq__(self, other):
		if self.var_count != other.var_count or len(self.table) != len(other.table):
			return False

		return all(row in other.table and self.table[row] == other.table[row] for row in self.table)

	def format(self):
		rows = [
			'  '.join(self.var_names) + '  | p',
			'-' * 3 * (self.var_count + 1)
		]

		for row in self.table:
			rows.append('  '.join(str(int(b)) for b in row) + '  | ' + str(int(self.table[row])))

		return rows

	def __str__(self):
		return '\n'.join(self.format())

	def print(self, *others, labels=None, padding='    '):
		tables = (self, ) + others
		tables = [table.format() for table in tables]
		lines = max(len(table) for table in tables)

		if labels:
			print(*(label.center(len(tables[i][0])) for i, label in enumerate(labels)), sep=padding)

		for i in range(lines):
			print(*(table[i] for table in tables if i < len(table)), sep=padding)

		print()
