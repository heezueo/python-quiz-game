import json


# JSON 파일에 게임 데이터를 저장하는 함수
def save_data(quizzes, best_score, score_history):
    # Quiz 객체를 JSON에 저장할 수 있는 딕셔너리로 변환
    quiz_list = []

    for quiz in quizzes:
        quiz_list.append(quiz.to_dict())

    # 저장할 데이터 구성
    data = {
        "quizzes": quiz_list,
        "best_score": best_score,
        "score_history": score_history
    }

    try:
        # state.json 파일에 데이터 저장
        with open(
            "state.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

        print("데이터를 저장했습니다.")
        return True

    except OSError as error:
        print(f"데이터 저장에 실패했습니다: {error}")
        return False


# JSON 파일에서 게임 데이터를 불러오는 함수
def load_data():

    try:
        # state.json 파일 열기
        with open(
            "state.json",
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data

    except FileNotFoundError:
        print(
            "저장된 데이터가 없습니다. "
            "기본 퀴즈를 사용합니다."
        )
        return None

    except json.JSONDecodeError:
        print(
            "저장된 데이터가 손상되었습니다. "
            "기본 퀴즈를 사용합니다."
        )
        return None

    except (KeyError, TypeError):
        print(
            "저장된 데이터 형식이 올바르지 않습니다. "
            "기본 퀴즈를 사용합니다."
        )
        return None