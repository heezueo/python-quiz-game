import json
import random
from datetime import datetime
from quiz import Quiz


class QuizGame:

    # 프로그램의 메인 메뉴를 출력하는 메서드
    def show_menu(self):
        print("\n===== 🐾 동물 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수")
        print("5. 퀴즈 삭제")
        print("6. 종료")

    # 프로그램 전체 실행 흐름을 담당하는 메서드
    def run(self):

        try:
            while True:

                self.show_menu()

                # 사용자에게 메뉴 번호를 입력받음
                menu = input("메뉴를 선택하세요: ").strip()

                # 빈 입력 처리
                if menu == "":
                    print("메뉴를 입력해주세요.")
                    continue

                # 숫자가 아닌 입력 처리
                if not menu.isdigit():
                    print("숫자만 입력해주세요.")
                    continue

                # 입력한 메뉴에 따라 해당 기능 실행
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
                    # 프로그램 종료 전에 데이터 저장
                    self.save_data()
                    print("프로그램을 종료합니다.")
                    break

                else:
                    print("1~6 사이의 숫자를 입력해주세요.")

        # Ctrl+C 또는 입력 종료(EOF) 발생 시 데이터 저장 후 안전하게 종료
        except (KeyboardInterrupt, EOFError):
            self.save_data()
            print("\n프로그램을 안전하게 종료합니다.")

    # 퀴즈를 실제로 진행하는 메서드
    def play_quiz(self):

        # 등록된 퀴즈가 없는 경우 실행하지 않음
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print("퀴즈를 시작합니다.\n")

        # 현재 게임의 점수
        score = 0

        # 기존 퀴즈 목록을 복사하여 원본 순서를 유지
        quiz_list = self.quizzes.copy()

        # 퀴즈 순서를 무작위로 섞음
        random.shuffle(quiz_list)

        # 출제할 문제 수를 입력받음
        while True:
            try:
                count = int(
                    input(f"몇 문제를 푸시겠습니까? (1~{len(quiz_list)}): ")
                )

                # 등록된 문제 수 범위 안인지 확인
                if 1 <= count <= len(quiz_list):
                    break
                else:
                    print("범위 내의 숫자를 입력해주세요.")

            except ValueError:
                # 숫자가 아닌 입력 처리
                print("숫자만 입력해주세요.")

        # 선택한 문제 수만큼 퀴즈 진행
        for quiz in quiz_list[:count]:

            # Quiz 객체의 display 메서드를 이용해 문제 출력
            quiz.display()

            # 정답을 입력받을 때까지 반복
            while True:

                answer = input(
                    "정답을 입력하세요 "
                    "(1~4, h: 힌트, q: 메뉴로 돌아가기): "
                ).strip()

                # h 입력 시 힌트 출력
                if answer.lower() == "h":
                    print(f"💡 힌트: {quiz.hint}")
                    continue

                # q 입력 시 현재 퀴즈를 종료하고 메뉴로 돌아감
                if answer.lower() == "q":
                    print("메뉴로 돌아갑니다.")
                    return

                try:
                    user_answer = int(answer)

                    # 정답 번호가 1~4인지 확인
                    if 1 <= user_answer <= 4:
                        break
                    else:
                        print("1~4 사이의 숫자를 입력하세요.\n")

                except ValueError:
                    # 숫자가 아닌 입력 처리
                    print("숫자만 입력해주세요.\n")

            # Quiz 클래스의 정답 확인 메서드 사용
            if quiz.check_answer(user_answer):
                print("정답입니다!\n")
                score += 1
            else:
                print("오답입니다.\n")

            # 다음 문제로 넘어가기 전 대기
            input("Enter를 누르면 넘어갑니다...🦭 ")
            print()

        # 모든 문제를 풀었을 때 결과 출력
        print("퀴즈가 끝났습니다!")
        print(f"총 {count}문제 중 {score}문제를 맞혔습니다.")

        # 점수와 플레이 날짜/시간을 기록
        self.score_history.append({
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

        # 최고 점수 갱신
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print(f"🎉 새로운 최고 점수입니다! {self.best_score}점")
        else:
            print(f"현재 최고 점수는 {self.best_score}점입니다.")

        # 게임 결과를 JSON 파일에 저장
        self.save_data()

    # QuizGame 객체가 생성될 때 실행되는 초기화 메서드
    def __init__(self):

        # 프로그램에서 사용할 기본 퀴즈 5개
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

        # 최고 점수 초기화
        self.best_score = None

        # 점수 기록을 저장할 리스트
        self.score_history = []

        # 저장된 JSON 데이터가 있으면 불러옴
        self.load_data()

    # 새로운 퀴즈를 추가하는 메서드
    def add_quiz(self):
        print("퀴즈 추가 기능입니다.\n")

        # 문제 입력
        question = input("문제를 입력하세요: ")

        # 4개의 선택지 입력
        choice1 = input("1번 선택지를 입력하세요: ")
        choice2 = input("2번 선택지를 입력하세요: ")
        choice3 = input("3번 선택지를 입력하세요: ")
        choice4 = input("4번 선택지를 입력하세요: ")

        choices = [choice1, choice2, choice3, choice4]

        # 힌트 입력
        hint = input("힌트를 입력하세요: ")

        # 입력한 내용을 다시 보여줌
        print(f"입력한 문제: {question}")
        print("\n입력한 선택지")

        for i, choice in enumerate(choices, start=1):
            print(f"{i}. {choice}")

        # 정답 번호 입력
        while True:

            try:
                answer = int(input("정답 번호를 입력하세요 (1~4): "))

                if 1 <= answer <= 4:
                    break
                else:
                    print("1~4 사이의 숫자를 입력하세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        # 입력받은 정보를 이용해 새로운 Quiz 객체 생성
        new_quiz = Quiz(question, choices, answer, hint)

        # 퀴즈 목록에 추가
        self.quizzes.append(new_quiz)

        # 변경된 데이터를 JSON에 저장
        self.save_data()

        print("퀴즈가 추가되었습니다.")

    # 등록된 퀴즈 목록을 출력하는 메서드
    def show_quizzes(self):

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(
            f"\n📋 등록된 퀴즈 목록 "
            f"(총 {len(self.quizzes)}개)\n"
        )

        # 번호와 함께 모든 퀴즈 출력
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

    # 최고 점수와 점수 기록을 보여주는 메서드
    def show_best_score(self):

        # 플레이 기록이 없는 경우
        if len(self.score_history) == 0:
            print("아직 플레이 기록이 없습니다.")
            return

        # 모든 플레이 점수의 합계 계산
        total = 0

        for history in self.score_history:
            total += history["score"]

        # 평균 점수 계산
        average = total / len(self.score_history)

        print("\n===== 📊 점수 정보 =====")
        print(f"🏆 최고 점수 : {self.best_score}점")
        print(f"🎮 플레이 횟수 : {len(self.score_history)}회")
        print(f"📈 평균 점수 : {average:.1f}점")

        print("\n===== 📝 점수 기록 =====")

        # 각 플레이의 날짜, 점수를 출력
        for i, history in enumerate(self.score_history, start=1):
            print(
                f"{i}회차 | "
                f"{history['date']} | "
                f"{history['score']}점"
            )

    # 퀴즈를 삭제하는 메서드
    def delete_quiz(self):

        if len(self.quizzes) == 0:
            print("삭제할 퀴즈가 없습니다.")
            return

        # 삭제할 퀴즈를 선택하기 위해 목록 출력
        self.show_quizzes()

        while True:
            try:
                answer = input(
                    "삭제할 퀴즈 번호를 입력하세요 (q: 취소): "
                ).strip()

                # q 입력 시 삭제 취소
                if answer.lower() == "q":
                    print("삭제를 취소했습니다.")
                    return

                number = int(answer)

                # 올바른 퀴즈 번호인지 확인
                if 1 <= number <= len(self.quizzes):
                    break
                else:
                    print("범위 내의 번호를 입력해주세요.")

            except ValueError:
                print("숫자만 입력해주세요.")

        # 선택한 퀴즈를 목록에서 삭제
        deleted_quiz = self.quizzes.pop(number - 1)

        print(f"'{deleted_quiz.question}' 퀴즈가 삭제되었습니다.")

        # 변경된 데이터를 저장
        self.save_data()

    # 현재 프로그램의 데이터를 JSON 파일에 저장하는 메서드
    def save_data(self):

        # Quiz 객체들을 JSON에 저장할 수 있는 딕셔너리로 변환
        quiz_list = []

        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        # 저장할 전체 데이터 구성
        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
            "score_history": self.score_history
        }

        # state.json 파일에 데이터 저장
        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print("데이터를 저장했습니다.")

    # JSON 파일의 데이터를 불러오는 메서드
    def load_data(self):

        try:
            # state.json 파일 열기
            with open(
                "state.json",
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            # JSON에서 퀴즈 데이터를 불러옴
            self.quizzes = []

            for quiz_data in data["quizzes"]:

                # JSON 데이터를 Quiz 객체로 변환
                quiz = Quiz(
                    quiz_data["question"],
                    quiz_data["choices"],
                    quiz_data["answer"],
                    quiz_data["hint"]
                )

                self.quizzes.append(quiz)

            # 최고 점수와 점수 기록 불러오기
            self.best_score = data["best_score"]
            self.score_history = data.get("score_history", [])

            print("데이터를 불러왔습니다.")

        # 파일이 없거나 JSON 데이터가 손상된 경우
        except (FileNotFoundError, json.JSONDecodeError):
            self.best_score = None

            print(
                "저장된 데이터가 없거나 손상되었습니다. "
                "기본 퀴즈를 사용합니다."
            )