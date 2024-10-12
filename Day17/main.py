from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_text = data["text"]
    question_answer = data["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

game = QuizBrain(question_bank)

while game.still_has_question():
    game.next_question()

print("You've completed the quiz")
print(f"Your final score is: {game.current_score}/{game.question_number}")