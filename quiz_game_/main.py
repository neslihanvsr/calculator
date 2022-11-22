# attributes: question number=0, question_list, score=0
# methods: next_questions(), still_has_questions(), check_answer()


from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  #if quiz still has questions remaining:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number})")
# or --  print(f"Your final score was: {{self.score}/{len(question_bank)}")

