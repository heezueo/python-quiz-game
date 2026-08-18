import json
import os


class DataManager:

    def __init__(self, filename="state.json"):
        self.filename = filename

    # 데이터 저장
    def save_data(self, quizzes, best_score, score_history):

        quiz_list = []

        for quiz in quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": best_score,
            "score_history": score_history
        }

        try:
            with open(
                self.filename,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    data,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

            return True

        except OSError as e:

            print(f"⚠️ 데이터 저장 실패: {e}")
            return False


    # 데이터 불러오기
    def load_data(self):

        try:

            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except FileNotFoundError:

            return None

        except json.JSONDecodeError:

            return None

        except OSError as e:

            print(f"⚠️ 데이터 불러오기 실패: {e}")
            return None