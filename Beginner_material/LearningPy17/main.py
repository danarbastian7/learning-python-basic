# # BUILD WITH OOP
#
# class User:
#     # Constructor
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
#
#
#
# user_1 = User("001", "Angle")
# user_2 = User("002", "Jack")
# # user_1.id = "001"
# # user_1.username = "Angela"
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
#
# # user_1 = User()
# # user_1.id = "001"
# # user_1.username = "Angela"

# ===================================
# Quiz Game Start

from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

