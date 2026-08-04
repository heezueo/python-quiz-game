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
                print("퀴즈 추가 기능")

            elif menu == "3":
                print("퀴즈 목록 기능")

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