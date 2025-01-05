import random
import time

# 현재 진행 중인 게임 세션을 추적하는 변수
_current_game_session = None

def game_like(current_name: str, players: list, is_ai: bool) -> list:
    global _current_game_session
    
    # 현재 플레이어 찾기
    current_player = next(p for p in players if p.name == current_name)
    rejection_count = 0

    # 새로운 게임 세션인지 확인
    if _current_game_session != id(players):
        _current_game_session = id(players)
        # 새로운 게임 세션이면 ASCII 아트 출력
        print('''
            ██╗     ██╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
            ██║     ██║██║ ██╔╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
            ██║     ██║█████╔╝ █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
            ██║     ██║██╔═██╗ ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
            ███████╗██║██║  ██╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
            ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        ''')
        print("\n===================<🕹  좋아게임의 규칙>===================\n")
        print("\n▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")
        print("술도 마셨는~데~ 좋아 게임 할~까?")
        print("▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")
        
    time.sleep(0.5)
    print("좋아게임의 규칙을 소개합니다!")
    print("1. 한 명씩 돌아가며 '누가 좋아?'를 외칩니다.")
    print("2. 좋아하는 사람을 선택해 'OOO 좋아!'라고 말합니다.")
    print("3. 선택받은 사람은 '나도 좋아!' 또는 '칵, 퉤!' 중 하나를 응답합니다.")
    print("4. 응답에서 '칵, 퉤!'가 세 번 연속 나오면 해당 플레이어가 게임에서 패배합니다.")
    time.sleep(0.5)
    if not is_ai:
        print("누가 좋아?")
        other_players = [p for p in players if p != current_player]
        if not other_players:
            print("Error: 선택할 수 있는 다른 플레이어가 없습니다.")
            return []
        
        for index, player in enumerate(other_players, 1):
            print(f"{index}: {player.name}", end="  ")
        while True:
            try:
                choice = int(input("\n선택할 플레이어 번호를 입력하세요: "))
                if 1 <= choice <= len(other_players):
                    selected_player = other_players[choice-1]
                    break
                else:
                    print(f"1에서 {len(other_players)} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
        time.sleep(0.5)  # 두 번째 breakpoint: 고백 순간
        print(f"{current_player.name}: {selected_player.name} 좋아!")
    else:
        selected_player = random.choice([p for p in players if p != current_player])
        time.sleep(0.5)  # 두 번째 breakpoint: 고백 순간
        print(f"{current_player.name}: {selected_player.name} 좋아!")

    # 응답 처리
    if not is_ai and selected_player == players[0]:  # 실제 플레이어가 선택되었을 때
        while True:
            try:
                response = int(input("1: 나도 좋아!  2: 칵, 퉤! "))
                if response in [1, 2]:
                    break
                else:
                    print("1 또는 2를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
        reaction = "나도 좋아!" if response == 1 else "칵, 퉤!"
    else:  # AI가 응답할 때
        reaction = random.choice(["나도 좋아!", "칵, 퉤!"])
    
    time.sleep(0.5)  # 세 번째 breakpoint: 응답 순간
    print(f"{selected_player.name}: {reaction}")

    if reaction == "나도 좋아!":
        print(f"\n💕 {current_player.name}와(과) {selected_player.name}의 짝짓기 성공! 아무도 마시지 않습니다~")
        return []  # 성공: 아무도 마시지 않음
    else:
        print(f"\n💔 {selected_player.name}(이)가 {current_player.name}의 고백을 거절했습니다!")
        print(f"🍺 벌칙: {current_player.name}(이)가 술 1잔을 마셔야 합니다!")
        return [current_player]  # 실패: 현재 플레이어만 마심