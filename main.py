from quiz import Quiz
from quiz_game import QuizGame

quiz1 = Quiz(
    "대한민국의 수도는?",
    ["부산", "서울", "대전", "광주"],
    2
)

quiz1.display()

user_answer = int(input("정답 번호를 입력하세요: "))

if quiz1.check_answer(user_answer):
    print("정답입니다!")
else:
    print("오답입니다.")