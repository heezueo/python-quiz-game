class Quiz:

    # 하나의 퀴즈 객체를 생성할 때 필요한 정보를 초기화
    def __init__(self, question, choices, answer, hint):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    # 문제와 선택지를 화면에 출력
    def display(self):
        print(f"문제: {self.question}")

        # 선택지에 1번부터 번호를 붙여 출력
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    # 사용자의 답과 실제 정답을 비교
    def check_answer(self, user_answer):
        return user_answer == self.answer

    # Quiz 객체를 JSON으로 저장할 수 있는 딕셔너리 형태로 변환
    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }