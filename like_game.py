import random

def game_like(players):
    main_player = players[0]
    current_player = players[0]  # 항상 첫 번째 플레이어로 시작
    rejection_count = 0

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

    while True:
        if current_player == main_player:
            print("누가 좋아?")
            for index, player in enumerate(players[1:], 1):
                print(f"{index}: {player.name}", end="  ")
            print()

            while True:
                try:
                    choice = int(input())
                    if 1 <= choice < len(players):
                        selected_player = players[choice]
                        break
                    else:
                        print(f"1에서 {len(players) - 1} 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
            print(f"{current_player.name}: {selected_player.name} 좋아!")
        else:
            selected_player = random.choice([p for p in players if p != current_player])
            print(f"{current_player.name}: {selected_player.name} 좋아!")

        if selected_player == main_player:
            while True:
                try:
                    response = int(input("1: 나도 좋아!  2: 칵, 퉤! "))
                    if response in [1, 2]:
                        break
                    else:
                        print("1 또는 2를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
            reaction = "나도 좋아" if response == 1 else "칵, 퉤!"
        else:
            reaction = random.choice(["나도 좋아!", "칵, 퉤!"])
        
        print(f"{selected_player.name}: {reaction}")

        if reaction == "나도 좋아!":
            current_player = selected_player
            rejection_count = 0
        else:
            rejection_count += 1
            if rejection_count >= 3:
                print("좋아게임이 종료되었습니다.")
                return players.index(current_player)