def is_valid():
   while True:
      n = input('На какой вопрос ты бы хотел узнать ответ?')
      if n.isdigit() or n[-1] != '?':
            print('Введите свой вопрос (он должен содержать буквенно-цифровые символы и вопросительный знак в конце):')
            continue
      break
#title
from random import choice
answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", \
            "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",\
            "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", \
            "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", \
            "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Введите свое имя:')
print(f'Привет, {name}')
while True:
   is_valid()
   print(f'Дай-ка подумать.... {choice(answers)}')
   n = input('Хочешь еще сыграть? ')
   if n.lower() not in ('no','not','не','нет', 'н'):
      continue
   break
print('Возвращайся если возникнут вопросы!')