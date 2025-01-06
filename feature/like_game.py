import random
import time

# 게임 세션 관리를 위한 전역 변수
_game_session_id = None

def game_like(current_player_name: str, real_player_name: str, all_players: list) -> list:
    global _game_session_id
    rejection_count = 0
    # 현재 게임 세션 확인 (all_players 리스트의 ID를 사용)
    current_session = id(all_players)
    
    # 새로운 게임 세션인 경우에만 설명 출력
    if _game_session_id != current_session:
        _game_session_id = current_session
        print("===========================================")
        print('''
        ██╗     ██╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
        ██║     ██║██║ ██╔╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
        ██║     ██║█████╔╝ █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
        ██║     ██║██╔═██╗ ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
        ███████╗██║██║  ██╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
        ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        ''')
        print("===========================================")
        time.sleep(0.5)
        print("좋아 게임은 ", end="")
        time.sleep(0.5)
        print("상대방에게 고백하는 게임입니다.")
        time.sleep(0.5)
        print("3번 연속으로 거절당하면 술을 마셔야 합니다!\n")
        time.sleep(0.5)
        print("준비되셨나요? 그럼 시작합니다~")
        time.sleep(0.5)

    # 현재 플레이어 찾기 (Player 객체만 필터링)
    current_player = next(p for p in all_players if hasattr(p, 'name') and p.name == current_player_name)
   

    # 현재 플레이어가 실제 플레이어인지 확인
    is_real_player = current_player_name == real_player_name
    
    # 고백 대상 선택
    available_players = [p for p in all_players if hasattr(p, 'name') and p != current_player]
    
    if is_real_player:  # 실제 플레이어의 차례
        print("\n누구에게 고백하시겠습니까?")
        for idx, p in enumerate(available_players, 1):
            print(f"{idx}: {p.name}", end="  ")
        print()
        
        while True:
            try:
                choice = int(input("선택: "))
                if 1 <= choice <= len(available_players):
                    selected_player = available_players[choice-1]
                    break
                else:
                    print(f"1에서 {len(available_players)} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("숫자를 입력하세요.")
    else:  # AI 플레이어의 차례
        selected_player = random.choice(available_players)
    
    print(f"\n{current_player.name}님의 차례입니다!")
    time.sleep(0.5)
    print(f"{current_player.name}: {selected_player.name}님, 저... 좋아합니다...♥")
    time.sleep(0.5)

    # 응답 처리
    if selected_player.name == real_player_name:  # 실제 플레이어가 선택되었을 때
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
    
    time.sleep(0.5)
    print(f"{selected_player.name}: {reaction}")

    if reaction == "칵, 퉤!":
        rejection_count = rejection_count +1
        print(f"\n💔 {selected_player.name}(이)가 {current_player.name}의 고백을 거절했습니다!")
        if rejection_count >= 3:
            print(f"🍺 3번 거절! {current_player.name}(이)가 술을 마셔야 합니다!")
            return [current_player]
        else:
            print(f"이번이 {rejection_count}번째 거절입니다.")  
            return 0       
    else:
        print(f"\n💕 {current_player.name}와(과) {selected_player.name}의 짝짓기 성공! 아무도 마시지 않습니다~")
        return 0 
    
    if current_session==len(all_players):
        if rejection_count<3:
            print("게임이 끝났음에도 루저가 정해지지 않았군요~! 게임을 제안한 사람이 마시세요")
            return [current_player_name]