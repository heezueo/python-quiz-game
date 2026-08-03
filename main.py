from quiz import Quiz

quiz1 = Quiz(
    "판다가 주로 먹는 음식은 무엇일까요?",
    ["사과", "대나무", "고기", "옥수수"],
    2
)

quiz2 = Quiz(
    "바다에서 가장 큰 동물은 무엇일까요?",
    ["상어", "돌고래", "대왕오징어", "대왕고래"],
    4
)

quiz3 = Quiz(
    "캥거루가 새끼를 키우는 곳은 어디일까요?",
    ["둥지", "굴", "주머니", "나무 위"],
    3
)

quiz4 = Quiz(
    "박쥐는 어떤 동물일까요?",
    ["새", "곤충", "포유류", "파충류"],
    3
)

quiz5 = Quiz(
    "코알라가 주로 먹는 것은 무엇일까요?",
    ["대나무", "유칼립투스 잎", "바나나", "도토리"],
    2
)

quizzes = [quiz1, quiz2, quiz3, quiz4, quiz5]

for quiz in quizzes:
    quiz.display()
    print()