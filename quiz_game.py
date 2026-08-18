import random
from datetime import datetime
from quiz import Quiz
from data_manager import DataManager


class QuizGame:

    # ==============================
    # 프로그램 초기화
    # ==============================
    def __init__(self):

        # 기본 동물 퀴즈 5개
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
                ["조류", "곤충", "포유류", "파충류"],
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

        # 최고 점수
        self.best_score = None

        # 점수 기록
        self.score_history = []

        # 데이터 저장/불러오기를 담당하는 객체
        self.data_manager = DataManager()

        # 기존 저장 데이터를 불러옴
        self.load_data()


    # ==============================
    # 메뉴 출력
    # ==============================
    def show_menu(self):

        print("\n===== 🐾 동물 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 퀴즈 삭제")
        print("6. 종료")


    # ==============================
    # 프로그램 실행
    # ==============================
    def run(self):

        try:

            while True:

                self.show_menu()

                menu = input("메뉴를 선택하세요: ").strip()

                # 빈 입력 처리
                if menu == "":
                    print("메뉴를 입력해주세요.")
                    continue

                # 숫자가 아닌 입력 처리
                if not menu.isdigit():
                    print("숫자만 입력해주세요.")
                    continue

                # 메뉴 선택
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

        # Ctrl+C 또는 입력 종료 상황 처리
        except (KeyboardInterrupt, EOFError):

            self.save_data()

            print("\n프로그램을 안전하게 종료합니다.")


    # ==============================
    # 퀴즈 풀기
    # ==============================
    def play_quiz(self):

        # 퀴즈가 없는 경우
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("퀴즈를 시작합니다.\n")

        score = 0

        # 기존 퀴즈 목록을 복사한 후 랜덤으로 섞음
        quiz_list = self.quizzes.copy()
        random.shuffle(quiz_list)

        # 문제 수 입력
        while True:

            try:

                count = int(
                    input(
                        f"몇 문제를 푸시겠습니까? "
                        f"(1~{len(quiz_list)}): "
                    )
                )

                if 1 <= count <= len(quiz_list):
                    break

                print("범위 내의 숫자를 입력해주세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        # 선택한 문제만 출제
        for quiz in quiz_list[:count]:

            quiz.display()

            # 정답 입력
            while True:

                answer = input(
                    "정답을 입력하세요 "
                    "(1~4, h: 힌트, q: 메뉴로 돌아가기): "
                ).strip()

                # 힌트
                if answer.lower() == "h":
                    print(f"💡 힌트: {quiz.hint}")
                    continue

                # 퀴즈 중단
                if answer.lower() == "q":
                    print("메뉴로 돌아갑니다.")
                    return

                try:

                    user_answer = int(answer)

                    if 1 <= user_answer <= 4:
                        break

                    print("1~4 사이의 숫자를 입력하세요.\n")

                except ValueError:
                    print("숫자만 입력해주세요.\n")

            # 정답 확인
            if quiz.check_answer(user_answer):

                print("정답입니다!\n")
                score += 1

            else:

                print("오답입니다.\n")

            input("Enter를 누르면 넘어갑니다...🦭 ")
            print()

        # 퀴즈 결과 출력
        print("퀴즈가 끝났습니다!")
        print(f"총 {count}문제 중 {score}문제를 맞혔습니다.")

        # 점수와 날짜/시간을 기록
        self.score_history.append({
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        # 최고 점수 갱신
        if self.best_score is None or score > self.best_score:

            self.best_score = score

            print(
                f"🎉 새로운 최고 점수입니다! "
                f"{self.best_score}점"
            )

        else:

            print(
                f"현재 최고 점수는 "
                f"{self.best_score}점입니다."
            )

        # 변경된 데이터를 저장
        self.save_data()


    # ==============================
    # 퀴즈 추가
    # ==============================
    def add_quiz(self):

        print("퀴즈 추가 기능입니다.\n")

        # 문제 입력
        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("문제는 비워둘 수 없습니다.")


        # 선택지 입력
        choices = []

        for i in range(1, 5):

            while True:

                choice = input(
                    f"{i}번 선택지를 입력하세요: "
                ).strip()

                if choice == "":
                    print("선택지는 비워둘 수 없습니다.")
                    continue

                choices.append(choice)
                break

        # 힌트 입력
        hint = input("힌트를 입력하세요: ").strip()

        # 입력 내용 확인
        print(f"\n입력한 문제: {question}")
        print("\n입력한 선택지")

        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        # 정답 번호 입력
        while True:

            try:

                answer = int(
                    input("정답 번호를 입력하세요 (1~4): ")
                )

                if 1 <= answer <= 4:
                    break

                print("1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        # Quiz 객체 생성
        new_quiz = Quiz(
            question,
            choices,
            answer,
            hint
        )

        # 퀴즈 목록에 추가
        self.quizzes.append(new_quiz)

        # 저장
        self.save_data()

        print("퀴즈가 추가되었습니다.")


    # ==============================
    # 퀴즈 목록 보기
    # ==============================
    def show_quizzes(self):

        if len(self.quizzes) == 0:

            print("등록된 퀴즈가 없습니다.")
            return

        print(
            f"\n📋 등록된 퀴즈 목록 "
            f"(총 {len(self.quizzes)}개)\n"
        )

        for i, quiz in enumerate(self.quizzes, start=1):

            print(
                f"{i}. {quiz.question}"
            )


    # ==============================
    # 최고 점수 및 점수 기록 보기
    # ==============================
    def show_best_score(self):

        if len(self.score_history) == 0:

            print("아직 플레이 기록이 없습니다.")
            return

        # 총점 계산
        total = 0

        for history in self.score_history:
            total += history["score"]

        # 평균 점수 계산
        average = total / len(self.score_history)

        print("\n===== 📊 점수 정보 =====")

        print(
            f"🏆 최고 점수 : "
            f"{self.best_score}점"
        )

        print(
            f"🎮 플레이 횟수 : "
            f"{len(self.score_history)}회"
        )

        print(
            f"📈 평균 점수 : "
            f"{average:.1f}점"
        )

        # 점수 기록 출력
        print("\n===== 📝 점수 기록 =====")

        for i, history in enumerate(
            self.score_history,
            start=1
        ):

            print(
                f"{i}회차 | "
                f"{history['date']} | "
                f"{history['score']}점"
            )


    # ==============================
    # 퀴즈 삭제
    # ==============================
    def delete_quiz(self):

        if len(self.quizzes) == 0:

            print("삭제할 퀴즈가 없습니다.")
            return

        # 현재 퀴즈 목록 출력
        self.show_quizzes()

        while True:

            try:

                answer = input(
                    "삭제할 퀴즈 번호를 입력하세요 "
                    "(q: 취소): "
                ).strip()

                # 삭제 취소
                if answer.lower() == "q":

                    print("삭제를 취소했습니다.")
                    return

                number = int(answer)

                # 번호 범위 확인
                if 1 <= number <= len(self.quizzes):
                    break

                print("범위 내의 번호를 입력해주세요.")

            except ValueError:

                print("숫자만 입력해주세요.")

        # 해당 퀴즈 삭제
        deleted_quiz = self.quizzes.pop(number - 1)

        print(
            f"'{deleted_quiz.question}' "
            f"퀴즈가 삭제되었습니다."
        )

        # 삭제 후 저장
        self.save_data()


    # ==============================
    # 데이터 저장
    # ==============================
    def save_data(self):

        # DataManager에게 저장을 요청
        success = self.data_manager.save_data(
            self.quizzes,
            self.best_score,
            self.score_history
        )

        if success:
            print("데이터를 저장했습니다.")
        else:
            print(
                "⚠️ 데이터 저장에 실패했습니다. "
                "기존 데이터가 유지될 수 있습니다."
            )


    # ==============================
    # 데이터 불러오기
    # ==============================
    def load_data(self):

        # DataManager에서 데이터 불러오기
        data = self.data_manager.load_data()

        # 불러오기 실패 또는 저장 파일이 없는 경우
        if data is None:

            print(
                "저장된 데이터가 없거나 손상되었습니다. "
                "기본 퀴즈를 사용합니다."
            )

            return

        # 저장된 퀴즈를 Quiz 객체로 변환
        self.quizzes = []

        for quiz_data in data.get("quizzes", []):

            quiz = Quiz(
                quiz_data["question"],
                quiz_data["choices"],
                quiz_data["answer"],
                quiz_data["hint"]
            )

            self.quizzes.append(quiz)

        # 최고 점수 불러오기
        self.best_score = data.get(
            "best_score",
            None
        )

        # 점수 기록 불러오기
        self.score_history = data.get(
            "score_history",
            []
        )

        print("데이터를 불러왔습니다.")