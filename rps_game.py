def 가위바위보하나빼기(current_player,available_names,is_friend):
    import time as t
    import random as r


    rps_list = ["가위", "바위", "보"]
 
    rps_players_name = available_names[:]
    rps_players_name.remove(current_player)

    if not is_friend:
        rps_enemy=input( "본인 제외 한명을 지목하여 이름을 입력해주세요😱 ")
        while rps_enemy== current_player:
            print("혼자서 게임을 할 수는 없어요~")
            t.sleep(1)
            rps_enemy=input( "다시 한명을 지목하여 이름을 입력해주세요~~😱 ")

        while rps_enemy not in rps_players_name:
            print("자리에 없는 사람이에요 다시 입력해주세요😱 ")
            t.sleep(1)
            rps_enemy=input( "다시 한명을 지목하여 이름을 입력해주세요~~😱 ")
 
        t.sleep(1)
        print("===================<🎮게임 시작!>===================")

        t.sleep(1) 
     
        while True:
            t.sleep(1)
            try:
                rps_left, rps_right = input("가위바위보! 'ex) 가위 바위' 형식으로 입력해주세요: ").split()
                if rps_left not in ["가위", "바위", "보"] or rps_right not in ["가위", "바위", "보"]:
                    raise ValueError
                break
            except ValueError:
                t.sleep(1)
                print("입력 형식이 올바르지 않아요! '가위 바위'처럼 두 개의 값을 띄어쓰기로 구분해서 입력해주세요.😊")

        rps_enemy_left, rps_enemy_right=r.sample(rps_list,2)
        print(f"{rps_enemy}는 {rps_enemy_left} {rps_enemy_right}를 냈네요!!")

        t.sleep(1)
        while True:
            t.sleep(1)
            try:
                rps_final=input("하나빼기 1! 님길 손을 선택해주세요 ex)왼손: ")
                if rps_final not in ["왼손","오른손"]:
                    raise ValueError
                break  
            except ValueError:
                t.sleep(1)
                print("입력 형식이 올바르지 않아요! '왼손' 혹은 '오른손'을 입력해주세요😊")

        t.sleep(2)
        print("누가 뭘 냈을까요? 두구두구두구두구구")
        if rps_final=="왼손":
            rps_final=rps_left
        if rps_final=="오른손":
            rps_final=rps_right

        t.sleep(1)
        print(f"{current_player}는 {rps_final}를 냈어요.")
        rps_enemy_final=r.choice([rps_enemy_left, rps_enemy_right])
        print(f"{rps_enemy}는 {rps_enemy_final}를 냈어요.")

        rps_player_win=[("가위","보"),("보","바위"),("바위","가위")]
        rps_enemy_win=[("보","가위"),("바위","보"),("가위","바위")]

        t.sleep(1)
        if rps_final==rps_enemy_final:
            print("무승부입니다! 둘다 반잔씩 마시세요.🍺")  
            return 0.5   

        elif (rps_final,rps_enemy_final) in rps_player_win:
            print(f"{current_player} wins~")
            print(f"{rps_enemy}한잔하세요~")
            return 0
        elif (rps_final,rps_enemy_final) in rps_enemy_win:
            print(f"{rps_enemy} wins~")
            print(f"{current_player}한잔하세요~")
            return 1
        

    elif is_friend:
        rps_enemy=r.choice([available_names])
        print( f"당신의 상대는 {rps_enemy}😱 ")

        t.sleep(1)
        print("===================<🎮게임 시작!>===================")

        t.sleep(1)
        print("가위바위보!")
        rps_left, rps_right=r.sample(rps_list,2)
        print(f"당신은 {rps_left} {rps_right}를 냈네요!!")

        rps_enemy_left, rps_enemy_right=r.sample(rps_list,2)
        print(f"{rps_enemy}는 {rps_enemy_left} {rps_enemy_right}를 냈네요!!")

        t.sleep(1)
  
        rps_final=r.choice([rps_left, rps_right])

        t.sleep(2)
        print("누가 뭘 냈을까요? 두구두구두구두구구")


        t.sleep(1)
        print(f"{current_player}는 {rps_final}를 냈어요.")
        rps_enemy_final=r.choice([rps_enemy_left, rps_enemy_right])
        print(f"{rps_enemy}는 {rps_enemy_final}를 냈어요.")

        rps_player_win=[("가위","보"),("보","바위"),("바위","가위")]
        rps_enemy_win=[("보","가위"),("바위","보"),("가위","바위")]

        t.sleep(1)
        if rps_final==rps_enemy_final:
            print("무승부입니다! 둘다 반잔씩 마시세요.🍺")  
            return 0.5   

        elif (rps_final,rps_enemy_final) in rps_player_win:
            print(f"{current_player} wins~")
 
            return 0
        elif (rps_final,rps_enemy_final) in rps_enemy_win:
            print(f"{rps_enemy} wins~")
            print(f"{current_player}한잔하세요~")
            return 1
