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
                print("퀴즈 풀기 기능")

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