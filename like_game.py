import random

def game_like(players_like, start_index):
    main_player_like = players_like[0]
    current_player_like = players_like[start_index]
    rejection_count_like = 0

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
        if current_player_like == main_player_like:   ### 현재 플레이어가 나일 때
            print("누가 좋아?")
            for index, player_like in enumerate(players_like[1:], 1):
                print(f"{index}: {player_like.name}", end="  ")
            print()

            while True:
                try:
                    choice = int(input())
                    if 1 <= choice < len(players_like):
                        selected_player_like = players_like[choice]
                        break
                    else:
                        print(f"1에서 {len(players_like) - 1} 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
            print(f"{current_player_like.name}: {selected_player_like.name} 좋아!")
        else:   ### 현재 플레이어가 다른 사람일 때
            selected_player_like = random.choice([p for p in players_like if p != current_player_like])
            print(f"{current_player_like.name}: {selected_player_like.name} 좋아!")

        ### 선택된 사람이 나일 때 반응
        if selected_player_like == main_player_like:
            while True:
                try:
                    response_like = int(input("1: 나도 좋아!  2: 칵, 퉤! "))
                    if response_like in [1, 2]:
                        break
                    else:
                        print("1 또는 2를 입력하세요.")
                except ValueError:
                    print("숫자를 입력하세요.")
            reaction_like = "나도 좋아" if response_like == 1 else "칵, 퉤!"
        else:   ### 선택된 사람이 내가 아닐 때
            reaction_like = random.choice(["나도 좋아!", "칵, 퉤!"])
        
        print(f"{selected_player_like.name}: {reaction_like}")

        if reaction_like == "나도 좋아!":
            current_player_like = selected_player_like
            rejection_count_like = 0
        else:
            rejection_count_like += 1
            if rejection_count_like >= 3:
                like_game_loser=selected_player_like
                print("좋아게임이 종료되었습니다.")
                return players_like.index(current_player_like)