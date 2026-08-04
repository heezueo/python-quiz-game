from quiz import Quiz
class QuizGame:

    def show_menu(self):
        print("\n===== 🐾 동물 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 종료")

    def run(self):

        while True:

            self.show_menu()
            menu = input("메뉴를 선택하세요: ")

            if menu == "1":
                self.play_quiz()

            elif menu == "2":
                self.add_quiz()

            elif menu == "3":
                self.show_quizzes()

            elif menu == "4":
                print("최고 점수 기능")

            elif menu == "5":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다.")

    def play_quiz(self):
        print("퀴즈를 시작합니다.\n")

        score = 0

        for quiz in self.quizzes:

            quiz.display()

            while True:

                answer = input("정답을 입력하세요 (1~4, q: 메뉴로 돌아가기): ").strip()

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

            input("Enter를 누르면 다음 문제로 넘어갑니다...🦭 ")
            print()

        print("퀴즈가 끝났습니다!")
        print(f"총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다.")


    def __init__(self):
        self.quizzes = [
            Quiz(
                "판다가 주로 먹는 음식은 무엇일까요?",
                ["사과", "대나무", "고기", "옥수수"],
                2
            ),

            Quiz(
                "바다에서 가장 큰 동물은 무엇일까요?",
                ["상어", "돌고래", "대왕오징어", "대왕고래"],
                4
            ),

            Quiz(
                "캥거루가 새끼를 키우는 곳은 어디일까요?",
                ["둥지", "굴", "주머니", "나무 위"],
                3
            ),

            Quiz(
                "박쥐는 어떤 동물일까요?",
                ["조류","곤충","포유류","파충류"],
                3
            ),

            Quiz(
                "코알라가 주로 먹는 것은 무엇일까요?",
                ["대나무", "유칼립투스 잎", "바나나", "도토리"],
                2
            )
        ]

    def add_quiz(self):
        print("퀴즈 추가 기능입니다.\n")

        question = input("문제를 입력하세요: ")

        choice1 = input("1번 선택지를 입력하세요: ")
        choice2 = input("2번 선택지를 입력하세요: ")
        choice3 = input("3번 선택지를 입력하세요: ")
        choice4 = input("4번 선택지를 입력하세요: ")
        choices = [choice1, choice2, choice3, choice4]

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

        new_quiz = Quiz(question, choices, answer)

        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다.")

    def show_quizzes(self):

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n") 

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")