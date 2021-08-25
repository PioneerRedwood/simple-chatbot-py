from chatterbot.chatterbot import ChatBot

my_bot = ChatBot(name='PyBot', read_only=True,
                logic_adapters=
['chatterbot.logic.MathematicalEvaluation',
                            'chatterbot.logic.BestMatch'])

from chatterbot.trainers import ChatterBotCorpusTrainer

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
# corpus_trainer.train('chatterbot.corpus.english')
corpus_trainer.train('chatterbot.corpus.korean')

kor_questions = [
    "안녕?",
    "잘 지내?"
]

questions = [
    'Hello?',
    'How are you?'
]

# for q in questions:
for q in kor_questions:
    print(my_bot.get_response(q))
