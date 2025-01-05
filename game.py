import random
import time
from number_game import number_game
from rps_game import 가위바위보하나빼기
from market_game import 시장에가면
from strawberry_game import 딸기게임
from like_game import game_like
import time

'''
    A[게임 시작] --> B[플레이어 정보 입력]
    B --> C[AI 플레이어 생성]
    C --> D{게임 선택}
    
    D -->|숫자 맞추기| E[숫자맞추기 게임]
    D -->|가위바위보| F[가위바위보 게임]
    D -->|시장에 가면| G[시장에가면 게임]
    D -->|딸기 게임| H[딸기 게임]
    D -->|좋아 게임| I[좋아 게임]
    D -->|exit| J[게임 종료]

    E --> K{게임 결과}
    F --> K
    G --> K
    H --> K
    I --> K

    K -->|실패| L[음주량 증가]
    K -->|성공| M[다음 플레이어]
    
    L --> N{치사량 체크}
    M --> D
    
    N -->|치사량 도달| J
    N -->|계속 진행| D
'''

# 게임 리스트
global games
global players_name
games = ["숫자 맞추기", "가위바위보 하나빼기", "시장에 가면", "딸기 게임", "좋아 게임"]
players_name = ["다오", "경민", "서정", "종서", "주영"]

class Player:
    def __init__(self, name, tolerance):
        self.name = name
        self.tolerance = tolerance  # 주량
        self.drinks = 0  # 현재까지 마신 잔 수

    def drink(self, amount):
        self.drinks += amount
        return self.drinks >= self.tolerance

def gamestart():
    print("=" * 60)
    print("★" * 60)
    print("=" * 60)
    print("▒" * 20 + "【 술게임 파티! 】" + "▒" * 20)
    print("=" * 60)
    print("▓" * 15 + "혼자서도 즐기는 Python 술게임" + "▓" * 15)
    print("=" * 60)

    # 사용자 정보 입력
    name = input("당신의 이름을 입력하세요: ")
    while True:
        try:
            print("\n주량을 선택하세요:")
            print("1. 소주 반병 (2잔)")
            print("2. 소주 한병 (4잔)")
            print("3. 소주 두병 (8잔)")
            tolerance = int(input("선택: "))
            if 1 <= tolerance <= 3:
                tolerance = [2, 4, 8][tolerance-1]
                break
            print("1-3 사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    player = Player(name, tolerance)
    
    # 다른 플레이어 초대
    while True:
        try:
            num_opponents = int(input("\n함께 플레이할 인원 수를 입력하세요 (최대 3명): "))
            if 1 <= num_opponents <= 3:
                break
            print("1-3 사이의 숫자를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

    opponents = []
    available_names = players_name.copy()
    available_names.remove(name) if name in available_names else None
    
    for _ in range(num_opponents):
        friend_name = random.choice(available_names)
        available_names.remove(friend_name)
        friend_tolerance = random.choice([2, 4, 8])
        opponents.append(Player(friend_name, friend_tolerance))
        print(f"{friend_name}님이 참가했습니다! (주량: {friend_tolerance}잔)")

    all_players = [player] + opponents
    current_player = player  # 게임 선택자

    while True:
        print("\n=== 현재 상태 ===")
        for p in all_players:
            print(f"{p.name}: {p.drinks}잔 / {p.tolerance}잔")
        
        print(f"\n=== {current_player.name}의 게임 선택 ===")
        
        if current_player == player:  # 실제 플레이어 차례
            print("\n게임 리스트:")
            for idx, game in enumerate(games, 1):
                print(f"{idx}. {game}")
            print("exit: 게임 종료")
            
            choice = input("게임 번호를 선택하세요: ")
            if choice == "exit":
                gameover()
                break
        else:  # 다른 플레이어 차례
            time.sleep(1)
            print(f"\n{current_player.name}(이)가 고민중...")
            time.sleep(0.5)
            choice = str(random.randint(1, len(games)))  # 랜덤으로 게임 선택
            print(f"{current_player.name}(이)가 {games[int(choice)-1]}을(를) 선택했습니다!")
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(games):
                print(f"\n=== {games[choice-1]} 시작! ===")
                drink_players = []  # 술을 마셔야 하는 플레이어들의 리스트
                
                for p in all_players:
                    print(f"\n{p.name}의 차례!")
                    if choice == 1:
                        result = number_game(all_players, p != player)
                    elif choice == 2:
                        friend_list = [fr for fr in all_players if fr!=p]
                        result = 가위바위보하나빼기(p.name, friend_list, p != player)
                    elif choice == 3:
                        result = 시장에가면(p.name, all_players, p != player)
                    elif choice == 4:
                        friend_list = [fr for fr in all_players if fr!=p]
                        result = 딸기게임(p.name, friend_list, p != player)
                    elif choice == 5:
                        result = game_like(p.name, all_players, p != player)
                    
                    # 게임 결과에 따라 마실 사람 리스트에 추가
                    if isinstance(result, list):
                        drink_players.extend(result)
                    else:  # 숫자로 반환된 경우
                        if result > 0:
                            drink_players.append(p)
                    
                    # 마실 사람이 있으면 게임 종료하고 다음 플레이어로
                    if drink_players:
                        break
                
                # 게임 결과 반영 및 치사량 체크
                dead_players = []
                for p in drink_players:
                    # 마시기 전에 치사량 체크
                    if p.drinks + 1 >= p.tolerance:
                        dead_players.append(p)
                
                if dead_players:  # 치사량 도달할 플레이어가 있다면
                    if len(dead_players) == 1:
                        print(f"\n💀 {dead_players[0].name}이(가) 치사량({dead_players[0].tolerance}잔)에 도달했습니다!")
                    else:
                        names = ", ".join(p.name for p in dead_players)
                        print(f"\n💀 {names}이(가) 치사량에 도달했습니다!")
                    gameover()
                    return
                
                # 치사량에 도달하지 않았다면 실제로 마시기
                for p in drink_players:
                    p.drink(1)
                
                # 이번 게임에서 마신 사람이 다음 게임 선택자가 됨
                if drink_players:
                    current_player = random.choice(drink_players)
                else:
                    # 아무도 마시지 않았다면 가장 많이 마신 사람 중에서 선택
                    max_drinks = max(p.drinks for p in all_players)
                    next_players = [p for p in all_players if p.drinks == max_drinks]
                    current_player = random.choice(next_players)
                
            else:
                print("잘못된 번호입니다. 다시 선택하세요.")
                continue
                
        except ValueError:
            print("유효한 숫자를 입력하거나 'exit'을 입력하세요.")
            continue

def gameover():
    print("""
    ######     #    #     # #######    ####### #     # ####### ######  
    #     #   # #   ##   ## #          #     # #     # #       #     # 
    #     #  #   #  # # # # #          #     # #     # #       #     # 
    ######  #     # #  #  # #####      #     # #     # #####   ######  
    #     # ####### #     # #          #     #  #   #  #       #   #   
    #     # #     # #     # #          #     #   # #   #       #    #  
    ######  #     # #     # #######    #######    #    ####### #     # 
    """)
    print("즐겁게 플레이해주셔서 감사합니다!")

if __name__ == "__main__":
    gamestart()