import time as t

### test를 위해 설정한 임의의 이름들
name_straw = '경민'
person_straw = ['하연', '수진', '민삭']

def strawberry_game(player, person_list):
    print("\n========================================================\n")
    t.sleep(1)
    print("{}님이 \"딸기게임\" 을 선택하셨습니다!🍓".format(player))
    t.sleep(1)
    print("{0}님, {1}님, {2}님 입장 하실게요~ 🍓"
          .format(person_list[0], person_list[1], person_list[2]))
    t.sleep(2)
    print("\n===================<🕹️  딸기게임의 규칙>==================\n")
    t.sleep(1)
    print("아이엠그라운드 박자 다들 아시죠?")
    t.sleep(1)
    print("딸기게임은 이 박자에 맞춰 \"딸기\"와 \"딸~기\"를 알맞게 말하는 게임인데요~")
    t.sleep(1)
    print("1박에는 짧게 '딸기', 2박에는 길게 '딸~기'를 외치면 됩니다!")
    t.sleep(1)
    print("🔄️ 8박(딸~기 딸~기)에 도달하면 reverse 딸기 게임으로(다시 7박으로~!) 돌아가요 🤠🔄️")
    t.sleep(1)
    print("박자에 맞춰 박수👏 와 딸기🍓 를 신나게 외쳐보아요~ 🎵")
    t.sleep(1)
    print("\n========================================================\n")
    t.sleep(2)
    print("{}: 👏👏👏 딸기".format(person_list[0]))
    t.sleep(1)
    print("{}: 👏👏 딸~기".format(person_list[1]))
    t.sleep(1)
    print("{}: 👏 딸기 딸~기".format(person_list[2]))
    t.sleep(1)
    answer = input('지금이에요!!🫵: ')
    if(answer == '딸~기 딸~기'):
        pass
    else:
        t.sleep(1)
        print("\n========================================================\n")
        print("누가 술을 마셔~ {}님이 마셔~ 원~샷!!".format(player))
        t.sleep(1)
        print("🍓 딸기게임이 종료되었습니다.👏")
        t.sleep(1)
        return player
    print("{}: 딸~기 딸~기 👏👏👏 딸기".format(person_list[0]))
    t.sleep(1)
    print("{}: 딸~기 딸~기 👏👏 딸~기".format(person_list[1]))
    t.sleep(1)
    print("{}: 딸~기 딸~기 👏 딸기 딸~기".format(person_list[2]))
    t.sleep(1)
    answer = input('지금이에요!!🫵: ')
    if(answer == '딸~기 딸~기 딸~기 딸~기'):
        t.sleep(1)
        print("\n========================================================\n")
        t.sleep(1)
        print("🔄️🤩 잘하는데요? 이제 순서도, 딸기도 reverse! 🤩🔄️")
        t.sleep(1)
        print("\n========================================================\n")
    else:
        t.sleep(1)
        print("\n========================================================\n")
        print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(player))
        t.sleep(1)
        print("🍓 딸기게임이 종료되었습니다.👏")
        t.sleep(1)
        return player
    answer = input('지금이에요!!🫵: ')
    if(answer == '딸~기 딸~기 👏 딸기 딸~기'):
        pass
    else: 
        t.sleep(1)
        print("\n========================================================\n")
        print("🍻 누가 술을 마셔~ {}님이 마셔~ 원~샷!! 🍻".format(player))
        t.sleep(1)
        print("🍓 딸기게임이 종료되었습니다.👏")
        t.sleep(1)
        return player
    print("{}: 딸~기 딸~기 👏👏 딸~기".format(person_list[2]))
    t.sleep(1)
    print("{}: 딸~기 딸~기 👏👏👏 딸기".format(person_list[1]))
    t.sleep(1)
    print("{}: 딸~기 딸~기".format(person_list[0]))
    answer = input('지금이에요!!🫵: ')
    if(answer == '👏 딸기 딸~기'):
        pass
    else: 
        t.sleep(1)
        print("\n========================================================\n")
        print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(player))
        t.sleep(1)
        print("🍓 딸기게임이 종료되었습니다.👏")
        t.sleep(1)
        return player
    t.sleep(1)
    print("{}: 👏👏 딸기 딸기..?".format(person_list[2]))
    t.sleep(1)
    print("\n========================================================\n")
    print("🍻 누가 술을 마셔~ {}(이)가 마셔~ 원~샷!! 🍻".format(person_list[2]))
    t.sleep(1)
    print("🍓 딸기게임이 종료되었습니다.👏")
    t.sleep(1)
    return person_list[2]
    
### main.py에서 작성할 코드들
### drunken: 술 마실 사람(주량 깎일 사람)을 받아옴
drunken = strawberry_game(name_straw, person_straw)