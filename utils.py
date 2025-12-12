import random
import requests
from config import WORDS_ON_JSON_KEEPER
from classes.basic_word import BasicWord


def load_random_word():
	"""
	Получает список слов с внешнего ресурса,
	выбирает случайное слово,
	создает экземпляр класса BasicWord

	:return: экземпляр класса BasicWord
	"""

	path = WORDS_ON_JSON_KEEPER
	response = requests.get(path)
	words = response.json()

	random_word = random.choice(words)

	basic_word = BasicWord(random_word['word'], random_word['subwords'])
	return basic_word
