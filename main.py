from utils import load_random_word
from classes.player import Player


def main():
	main_word = load_random_word()

	word = main_word.word
	wordcount = main_word.count_subwords()

	user_name = input('Введите имя игрока:\n')
	print(f'Привет, {user_name}!')

	this_player = Player(user_name)

	print(f'Составьте {wordcount} слов из слова {word}')
	print('Слова должны быть не короче трех букв.\n')
	print('Чтобы закончить игру, угадайте все слова и напишите "stop".')
	print('Поехали, ваше первое слово?')

	answer_counter = 0

	while answer_counter != wordcount:
		print("Введите слово:")
		user_input = input()

		if user_input == 'stop':
			break

		elif len(user_input) < 3:
			print('Слишком короткое слово.\n')

		elif this_player.has_uses(user_input):
			print('Уже использовано.\n')

		elif main_word.has_subword(user_input):
			print("Слово есть.\n")
			answer_counter += 1
			this_player.add_word(user_input)

		else:
			print("Неверно.\n")
			answer_counter += 1

	print(f'\nИгра завершена, вы угадали {this_player.count_words()} слов!')


main()
