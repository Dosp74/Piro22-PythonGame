import random
import time



def game_like(player, all_players, current_player):
    player=player
    all_players=all_players
    rejection_count = 0

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
    print("3번째 거절당하는 사람은 술을 마셔야 합니다!\n")
    time.sleep(0.5)
    print("준비되셨나요? 그럼 시작합니다~")
    time.sleep(0.5)

    for i in all_players:
        
        available_players = [k for k in all_players if k != i]
        
        if i==player:
            print(f"{i.name}님의 차례입니다.")
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
            time.sleep(0.5)
            print(f"{i.name}: {selected_player.name}님, 저... 좋아합니다...♥")
            time.sleep(0.5)
            reaction = random.choice(["나도 좋아!", "칵, 퉤!"])
            if reaction == "칵, 퉤!":
                rejection_count+=1
                print(reaction)
                print(f"\n💔 {selected_player.name}(이)가 {i.name}의 고백을 거절했습니다!")
                if rejection_count >= 3:
                    print(f"🍺 3번 거절! {i}(이)가 술을 마셔야 합니다!")
                    return [i]
                else:
                    print(f"이번이 {rejection_count}번째 거절입니다.")              
            else:
                print(reaction)
                print(f"\n💕 {i.name}와(과) {selected_player.name}의 짝짓기 성공! 아무도 마시지 않습니다~")
                

        elif i!=player: # AI 플레이어의 차례
            print(f"{i.name}님의 차례입니다.")
            selected_player = random.choice(available_players)
            time.sleep(0.5)
            print(f"{i.name}: {selected_player.name}님, 저... 좋아합니다...♥")
            time.sleep(0.5)

            # 응답 처리
            if selected_player == player:  # 실제 플레이어가 선택되었을 때
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
                print(f"\n💔 {selected_player.name}(이)가 {i.name}의 고백을 거절했습니다!")
                if rejection_count >= 3:
                    print(f"🍺 3번 거절! {i.name}(이)가 술을 마셔야 합니다!")
                    return [i]
                
                else:
                    print(f"이번이 {rejection_count}번째 거절입니다.")  
            else:
                print(f"\n💕 {i.name}와(과) {selected_player.name}의 짝짓기 성공! 아무도 마시지 않습니다~")
            
    
 
    print("게임이 끝났음에도 루저가 정해지지 않았군요~! 게임을 제안한 사람이 마시세요~!")
    return [current_player]