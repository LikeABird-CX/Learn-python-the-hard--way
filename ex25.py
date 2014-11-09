# coding:utf-8
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')#按照空格分词
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)#返回排序后的词序
	
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)#取出列表中的第一个词
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)#取出列表中最后一个词
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)#从句子中分词
	return sort_words(words)#把分后的词排序
	
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)#从句子中分词
	print_first_word(words)#打印第一个词
	print_last_word(words)#打印最后一个词

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)#调用sort_sentence函数，进行分词排序
	print_first_word(words)#打印排序后的第一个词
	print_last_word(words)#打印排序后的最后一个词