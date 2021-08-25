from chatterbot.chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot(name='PyBot', read_only=True,
                logic_adapters=
['chatterbot.logic.MathematicalEvaluation',
                            'chatterbot.logic.BestMatch'])

small_talk = [
    'Hi there!',
    'Hi!',
    'How do you do?',
    'How are you?',
    'I\'m cool.',
    'Fine, you?',
    'Always cool.',
    'Glad to hear that.',
    'I\'m fine.',
    'I feel awesome!',
    'Excellent, glad to hear that.',
    'Not so good.',
    'Sorry to hear that.',
    'what\s your name?',
    'I\'m pybot. Ask me a math question, please.'
    ]

math_talk1 = ['pythagorean theorem',
            'a squared plus b squared equals c squared.']

math_talk2 = ['law of cosines',
            'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']

list_trainer = ListTrainer(my_bot)

for item in (small_talk, math_talk1, math_talk2):
    list_trainer.train(item)

print(my_bot.get_response('Do you know pytahgorean theorem?'))
# c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)