import random
from number_game import 숫자맞추기
from rps_game import 가위바위보하나빼기
from market_game import 시장에가면
from strawberry_game import 딸기게임
from like_game import 좋아게임

# 게임 리스트
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
    
    # 컴퓨터 플레이어 초대
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
        comp_name = random.choice(available_names)
        available_names.remove(comp_name)
        comp_tolerance = random.choice([2, 4, 8])
        opponents.append(Player(comp_name, comp_tolerance))
        print(f"{comp_name}님이 참가했습니다! (주량: {comp_tolerance}잔)")

    all_players = [player] + opponents
    
    current_player_idx = 0
    while True:
        current_player = all_players[current_player_idx]
        print(f"\n=== {current_player.name}의 차례 ===")
        print(f"현재 마신 잔 수: {current_player.drinks}")
        print(f"치사량까지 남은 잔 수: {current_player.tolerance - current_player.drinks}")
        
        if current_player == player:  # 실제 플레이어 차례
            print("\n게임 리스트:")
            for idx, game in enumerate(games, 1):
                print(f"{idx}. {game}")
            print("exit: 게임 종료")
            
            choice = input("게임 번호를 선택하세요: ")
            if choice == "exit":
                gameover()
                break
        else:  # 컴퓨터 플레이어 차례
            choice = str(random.randint(1, len(games)))
            print(f"{current_player.name}이(가) {games[int(choice)-1]}을(를) 선택했습니다!")
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(games):
                result = 0
                if choice == 1:
                    result = 숫자맞추기()
                elif choice == 2:
                    result = 가위바위보하나빼기()
                elif choice == 3:
                    result = 시장에가면()
                elif choice == 4:
                    result = 딸기게임()
                elif choice == 5:
                    result = 좋아게임()
                
                # 게임 결과 반영
                is_dead = current_player.drink(result)
                if is_dead:
                    print(f"\n{current_player.name}이(가) 치사량({current_player.tolerance}잔)에 도달했습니다!")
                    gameover()
                    break
            else:
                print("잘못된 번호입니다. 다시 선택하세요.")
                continue
                
        except ValueError:
            print("유효한 숫자를 입력하거나 'exit'을 입력하세요.")
            continue
            
        # 다음 플레이어로 순서 넘기기
        current_player_idx = (current_player_idx + 1) % len(all_players)

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
