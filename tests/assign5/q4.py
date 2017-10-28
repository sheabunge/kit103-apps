from kit103_assign5 import load_words

word_lists, word_sets = load_words()


def verify_anagrams(anagrams_list, word):
	w_sorted = sorted(word)
	print(w_sorted)
	for anagram in anagrams_list:
		print(sorted(anagram))
		if sorted(anagram) != w_sorted:
			print(f'Error: {word} is not an anagram of {anagram}')
		if anagram not in word_lists[len(anagram)]:
			print(f'Error: {anagram} is not a valid word')
	return anagrams_list


def test_all(anagrams):
	for words in word_lists.values():
		for word in words:
			verify_anagrams(word, anagrams(word))
