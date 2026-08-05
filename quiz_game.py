import json
import random
from datetime import datetime
from quiz import Quiz
class QuizGame:

    def show_menu(self):
        print("\n===== 🐾 동물 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 퀴즈 삭제")
        print("6. 종료")

    def run(self):

        try:

            while True:

                self.show_menu()
                menu = input("메뉴를 선택하세요: ").strip()

                if menu == "":
                    print("메뉴를 입력해주세요.")
                    continue

                if not menu.isdigit():
                    print("숫자만 입력해주세요.")
                    continue

                if menu == "1":
                    self.play_quiz()

                elif menu == "2":
                    self.add_quiz()

                elif menu == "3":
                    self.show_quizzes()

                elif menu == "4":
                    self.show_best_score()

                elif menu == "5":
                    self.delete_quiz()

                elif menu == "6":
                    self.save_data()
                    print("프로그램을 종료합니다.")
                    break

                else:
                    print("1~6 사이의 숫자를 입력해주세요.")

        except (KeyboardInterrupt, EOFError):
            self.save_data()
            print("\n프로그램을 안전하게 종료합니다.")

    def play_quiz(self):

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("퀴즈를 시작합니다.\n")

        score = 0

        quiz_list = self.quizzes.copy()
        random.shuffle(quiz_list)

        while True:
            try:
                count = int(input(f"몇 문제를 푸시겠습니까? (1~{len(quiz_list)}): "))

                if 1<= count <= len(quiz_list):
                    break
                else:
                    print("범위 내의 숫자를 입력해주세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        for quiz in quiz_list[:count]:

            quiz.display()

            while True:

                answer = input("정답을 입력하세요 (1~4, h: 힌트, q: 메뉴로 돌아가기): ").strip()

                if answer.lower() == "h":
                    print(f"💡 힌트: {quiz.hint}")
                    continue

                if answer.lower() == "q":
                    print("메뉴로 돌아갑니다.")
                    return
                
                try:
                    user_answer = int(answer)

                    if 1 <= user_answer <= 4:
                        break

                    else:
                        print("1~4 사이의 숫자를 입력하세요.\n")

                except ValueError:
                    print("숫자만 입력해주세요.\n")

            if quiz.check_answer(user_answer):
                print("정답입니다!\n")
                score += 1

            else:
                print("오답입니다.\n")

            input("Enter를 누르면 넘어갑니다...🦭 ")
            print()

        print("퀴즈가 끝났습니다!")
        print(f"총 {count}문제 중 {score}문제를 맞혔습니다.")
        self.score_history.append({
            "score" : score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print(f"🎉 새로운 최고 점수입니다! {self.best_score}점")

        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

        self.save_data()
    

    def __init__(self):
        self.quizzes = [
            Quiz(
                "판다가 주로 먹는 음식은 무엇일까요?",
                ["사과", "대나무", "고기", "옥수수"],
                2,
                "🐼 대나무를 먹는 동물이에요."
            ),

            Quiz(
                "바다에서 가장 큰 동물은 무엇일까요?",
                ["상어", "돌고래", "대왕오징어", "대왕고래"],
                4,
                "🐳 포유류이며 매우 커요."
            ),

            Quiz(
                "캥거루가 새끼를 키우는 곳은 어디일까요?",
                ["둥지", "굴", "주머니", "나무 위"],
                3,
                "🦘 배 앞쪽에 있는 곳이에요."
            ),

            Quiz(
                "박쥐는 어떤 동물일까요?",
                ["조류","곤충","포유류","파충류"],
                3,
                "🦇 하늘을 날지만 새는 아니에요."
            ),

            Quiz(
                "코알라가 주로 먹는 것은 무엇일까요?",
                ["대나무", "유칼립투스 잎", "바나나", "도토리"],
                2,
                "🌿 호주에 사는 동물이에요."
            )
        ]
        self.best_score = None
        self.score_history = []

        self.load_data()

    def add_quiz(self):
        print("퀴즈 추가 기능입니다.\n")

        question = input("문제를 입력하세요: ")

        choice1 = input("1번 선택지를 입력하세요: ")
        choice2 = input("2번 선택지를 입력하세요: ")
        choice3 = input("3번 선택지를 입력하세요: ")
        choice4 = input("4번 선택지를 입력하세요: ")
        choices = [choice1, choice2, choice3, choice4]

        hint = input("힌트를 입력하세요: ")

        print(f"입력한 문제: {question}")
        print("\n입력한 선택지")

        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        while True:

            try:
                answer = int(input("정답 번호를 입력하세요 (1~4): "))
                if 1 <= answer <= 4:
                    break

                else:
                    print("1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        new_quiz = Quiz(question, choices, answer, hint)

        self.quizzes.append(new_quiz)

        self.save_data()

        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self):

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n") 

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")


    def show_best_score(self):
        if len(self.score_history) == 0:
            print("아직 플레이 기록이 없습니다.")
            return

        total = 0

        for history in self.score_history:
            total += history["score"]

        average = total / len(self.score_history)

        print("\n===== 📊 점수 정보 =====")
        print(f"🏆 최고 점수 : {self.best_score}점")
        print(f"🎮 플레이 횟수 : {len(self.score_history)}회")
        print(f"📈 평균 점수 : {average:.1f}점")

        print("\n===== 📝 점수 기록 =====")

        for i, history in enumerate(self.score_history, start=1):
            print(f"{i}회차 | {history['date']} | {history['score']}점")

    def delete_quiz(self):
        if len(self.quizzes) == 0:
            print("삭제할 퀴즈가 없습니다.")
            return

        self.show_quizzes()

        while True:
            try:
                answer = input("삭제할 퀴즈 번호를 입력하세요 (q: 취소): ").strip()

                if answer.lower() == "q":
                    print ("삭제를 취소했습니다.")
                    return

                number = int(answer)

                if 1 <= number <= len(self.quizzes):
                    break
                else:
                    print("범위 내의 번호를 입력해주세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        deleted_quiz = self.quizzes.pop(number-1)
        print(f"'{deleted_quiz.question}' 퀴즈가 삭제되었습니다.")
        self.save_data()
    

    def save_data(self):

        quiz_list = []

        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes" : quiz_list,
            "best_score" : self.best_score,
            "score_history": self.score_history
        }

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("데이터를 저장했습니다.")


    def load_data(self):

        try:

            with open("state.json","r",encoding="utf-8") as file:
                data = json.load(file)

            self.quizzes = []

            for quiz_data in data["quizzes"]:

                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"],
                    quiz_data["hint"]
                )

                self.quizzes.append(quiz)

            self.best_score = data["best_score"]
            self.score_history = data.get("score_history", [])

            print("데이터를 불러왔습니다.")

        except (FileNotFoundError, json.JSONDecodeError) :
            self.best_score = None
            print("저장된 데이터가 없거나 손상되었습니다. 기본 퀴즈를 사용합니다.")