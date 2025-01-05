import random

# def game_like(players):
def game_like(players, trigger_player):
    # 유효성 검사 추가
    if trigger_player not in players:
        print("Error: Invalid trigger player")
        return 0
        
    main_player = players[0]
    current_player = trigger_player
    rejection_count = 0
    max_rounds = 20  # 최대 라운드 수 설정
    round_count = 0

    print('''
        ██╗     ██╗██╗  ██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗
        ██║     ██║██║ ██╔╝██╔════╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
        ██║     ██║█████╔╝ █████╗      ██║  ███╗███████║██╔████╔██║█████╗  
        ██║     ██║██╔═██╗ ██╔══╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
        ███████╗██║██║  ██╗███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
        ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    ''')

    print("▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")
    print("술도 마셨는~데~ 좋아 게임 할~까?")
    print("▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱ ▰ ▱")

    while round_count < max_rounds:
        round_count += 1
        
        if current_player == main_player:
            print("\n누가 좋아?")
            available_players = [p for p in players[1:]]
            for index, player in enumerate(available_players, 1):
                print(f"{index}: {player.name}", end="  ")
            print()

            while True:
                try:
                    choice = int(input())
                    if 1 <= choice <= len(available_players):
                        selected_player = available_players[choice-1]
                        break
                    else:
                        print(f"1에서 {len(available_players)} 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
        else:
            # AI 플레이어의 선택
            available_players = [p for p in players if p != current_player]
            selected_player = random.choice(available_players)
            
        print(f"{current_player.name}: {selected_player.name} 좋아!")

        # 응답 처리
        if selected_player == main_player:
            while True:
                try:
                    response = int(input("1: 나도 좋아!  2: 칵, 퉤! "))
                    if response in [1, 2]:
                        break
                    print("1 또는 2를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
            reaction = "나도 좋아!" if response == 1 else "칵, 퉤!"
        else:
            reaction = random.choice(["나도 좋아!", "칵, 퉤!"])
        
        print(f"{selected_player.name}: {reaction}")

        if reaction == "나도 좋아!":
            current_player = selected_player
            rejection_count = 0
        else:
            rejection_count += 1
            if rejection_count >= 3:
                print("\n좋아게임이 종료되었습니다.")
                print(f"{current_player.name}이(가) 패배했습니다!")
                return 1

        # 최대 라운드 도달 시
        if round_count >= max_rounds:
            print("\n최대 라운드에 도달했습니다!")
            print(f"{current_player.name}이(가) 패배했습니다!")
            return 1

    return 0