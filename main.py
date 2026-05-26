import json
import random
import os

def load_data():
    # 데이터 파일 경로 (data 폴더 안의 json 읽기)
    data_path = os.path.join('data', 'event_contents.json')
    if not os.path.exists(data_path):
        return None
    with open(data_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def run_event_helper():
    print("="*50)
    print("Welcome to YOUTH-EVENT-HUB Automation Tool")
    print("="*50)

    data = load_data()
    if not data:
        print("Error: Data file not found. Please check data/event_contents.json")
        return

    # 1. 참가자 입력받기 (예시 입력 제공)
    print("\n[Step 1] Enter participant names (separated by commas)")
    print("Example: Kim, Lee, Park, Choi")
    names_input = input("Names: ")
    participants = [name.strip() for name in names_input.split(',') if name.strip()]
    
    if not participants:
        print("No participants entered. Using sample data for demo...")
        participants = ["Student A", "Student B", "Student C", "Student D"]

    # 2. 조 개수 입력받기
    try:
        num_groups = int(input(f"\n[Step 2] How many groups? (1-{len(participants)}): "))
    except ValueError:
        num_groups = 2

    # 3. 랜덤 조 편성
    random.shuffle(participants)
    groups = [[] for _ in range(num_groups)]
    for i, name in enumerate(participants):
        groups[i % num_groups].append(name)

    # 4. 결과 출력 및 밸런스 게임 매칭
    print("\n" + "="*20 + " RESULTS " + "="*20)
    questions = data['balance_games']
    random.shuffle(questions)

    for i, group in enumerate(groups):
        question = questions[i % len(questions)]
        print(f"\n[Group {i+1}]")
        print(f" - Members: {', '.join(group)}")
        print(f" - Topic: {question['topic_ko']}")
    print("\n" + "="*49)

if __name__ == "__main__":
    run_event_helper()
