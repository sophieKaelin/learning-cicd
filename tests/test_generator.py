import unittest

from buzz import generator

def test_randomGenerator_single_word():
	_list = ('foo', 'bar', 'foobar')
	word = generator.selectRandom(_list)
	assert word in _list

def test_randomGenerator_multiple_words():
	_list = ('foo', 'bar', 'foobar')
	words = generator.selectRandom(_list, 2)
	assert len(words) == 2
	assert words[0] in _list, "hello"
	assert words[1] in _list
	assert words[0] is not words[1]

def test_generate_buzz_of_at_least_five_words():
	phrase = generator.generate_buzz()
	assert len(phrase.split()) >= 5

if __name__ == "__main__":
	test_randomGenerator_single_word()