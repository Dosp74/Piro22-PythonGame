import random
import time

<<<<<<< HEAD
def 시장에가면(name, players, is_human,me):
=======
def 시장에가면(me, name, players):
>>>>>>> f377f01aeb8b6c2807e3acc0ff168cc2ee2c06a9
    itemList = ["사과", "고등어", "소주", "맥주", "문어", "갈치", "휴대폰", "TV", 
                "노트북", "컵", "휴지", "물티슈", "바나나", "커피", "콜라", "초콜릿", 
                "우유", "빵", "계란", "치킨", "피자", "햄버거", "케이크", "컵라면", 
                "떡", "오이", "배추", "당근", "감자", "고구마", "양파", "마늘", "생강", 
                "고추", "피망", "파프리카", "토마토", "김치", "된장", "고추장", "간장", 
                "블랙타이거새우", "홈런볼", "포카칩", "새우깡", "초코파이", "츄러스", 
                "포도", "참외", "메론", "와인", "막걸리", "사이다", "초코우유", "껌", 
                "참이슬", "별빛청하", "매화수", "오렌지주스", "떡볶이", "순대", "튀김", 
                "냉면", "순두부찌개", "초밥", "김밥", "감", "샤인머스캣", "오리고기", 
                "전복", "방어", "광어", "참치", "연어", "보조배터리", "헤드셋", "의자", 
                "책상", "프린터", "이어폰", "휴대폰케이스", "망치", "톱", "나사", "드라이버", 
                "노트", "자석", "테이프", "편지지", "봉투", "엽서", "스티커", "볼펜", 
                "야구공", "축구공", "볼링공", "장갑", "모자", "양말", "바지", "청바지", 
                "치마", "원피스", "코트", "패딩", "맨투맨", "우럭", "핸드크림", "락스", 
                "세제", "수건", "면도기", "영양제", "빗", "립밤", "선크림", "라이터"]

    print("===========================================================================================")
    print('''
    ███    ███  █████  ██████  ██   ██ ███████ ████████      ██████   █████  ███    ███ ███████ 
    ████  ████ ██   ██ ██   ██ ██   ██ ██         ██        ██       ██   ██ ████  ████ ██      
    ██ ████ ██ ███████ ██████  ███████ █████      ██        ██   ███ ███████ ██ ████ ██ █████   
    ██  ██  ██ ██   ██ ██   ██ ██   ██ ██         ██        ██    ██ ██   ██ ██  ██  ██ ██      
    ██      ██ ██   ██ ██   ██ ██   ██ ███████    ██         ██████  ██   ██ ██      ██ ███████ 
    ''')
    print("===========================================================================================")
    time.sleep(1)
    print("시장에 가면 게임은 ", end="")
    time.sleep(1)
    print("시장에 있는 물건을 말하는 게임으로,")
    time.sleep(1)
    print("중복되면 안 되며 말한 순서대로 말해야 합니다!\n")
    time.sleep(1)
    print("콘솔에는 물건의 이름만 입력하면 됩니다!\n")
    time.sleep(1)
    print("준비되셨나요? 그럼 시작합니다~")
    time.sleep(1)

    print("\n===== 시장에 가면~ =====")
    time.sleep(1)
    print("\n===== 시장에 가면~ =====\n")
    time.sleep(1)

    count = 1
    gameItemList = []
    randomCeil = random.randint(13, 18)
    start_index = next((i for i, player in enumerate(players) if player.name == name), 0)
    players = players[start_index:] + players[:start_index]
    randomCount = random.randint(8, 12)
    while True:
        for player in players:
            if player.name == me:
                print(player.name + " : 시장에 가면~ ", end="")
                time.sleep(1)
                for i in range(count):
                    gameItemListLength = len(gameItemList)
                    myItem = input("")
                    if i >= gameItemListLength:
                        gameItemList.append(myItem)
                        print(gameItemList[i] + "도 있고 ~ ", end="")
                        #time.sleep(1)
                    elif myItem == gameItemList[i]:
                        print(gameItemList[i] + "도 있고 ~ ", end="")
                        #time.sleep(1)
                    else:
                        time.sleep(1)
                        print("아~ 순서가 틀렸어요😂")
                        return [player]
                count += 1
            else:
                print(player.name + " : 시장에 가면~ ", end="")
                time.sleep(1)
                for i in range(count): # 현재 로직: 봇은 무조건 게임 통과
                    gameItemListLength = len(gameItemList)
                    if randomCount <= count:
                        print("어...")
                        time.sleep(1)
                        print("아~ 순서가 틀렸어요😂")
                        return [player]
                    if randomCeil <= count:
                        print("애썼다! 다음 게임하자~")
                        time.sleep(1)
                        print("승부가 안 나니까 무효...")
                        return []
                    if i >= gameItemListLength:
                        item = random.choice(itemList)
                        while item in gameItemList:
                            item = random.choice(itemList)
<<<<<<< HEAD
                            while item in gameItemList:
                                item = random.choice(itemList)
                            gameItemList.append(item)
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                            continue
                        item = gameItemList[i]
                        if item == gameItemList[i]:
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                    count += 1
                print("\n")
    else: # 봇이 게임 선택자인 경우, 게임 자동 진행
        randomCount = random.randint(8, 12)
        while True:
            for player in players:
                if player.name == name:
                    print(player.name + " : 시장에 가면~ ", end="")
                    time.sleep(1)
                    for i in range(count):
                        gameItemListLength = len(gameItemList)
                        if randomCount <= count:
                            print("어...")
                            time.sleep(1)
                            print("아~ 순서가 틀렸어요😂")
                            return [player]
                        if randomCeil <= count:
                            print("애썼다! 다음 게임하자~")
                            time.sleep(1)
                            print("승부가 안 나니까 무효...")
                            return []
                        if i >= gameItemListLength:
                            item = random.choice(itemList)
                            while item in gameItemList:
                                item = random.choice(itemList)
                            gameItemList.append(item)
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                            continue
                        item = gameItemList[i]
                        if item == gameItemList[i]:
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                    count += 1
                else:
                    print(player.name + " : 시장에 가면~ ", end="")
                    time.sleep(1)
                    for i in range(count): # 현재 로직: 봇은 무조건 게임 통과
                        gameItemListLength = len(gameItemList)
                        if randomCount <= count:
                            print("어...")
                            time.sleep(1)
                            print("아~ 순서가 틀렸어요😂")
                            return [player]
                        if randomCeil <= count:
                            print("애썼다! 다음 게임하자~")
                            time.sleep(1)
                            print("승부가 안 나니까 무효...")
                            return []
                        if i >= gameItemListLength:
                            item = random.choice(itemList)
                            while item in gameItemList:
                                item = random.choice(itemList)
                             gameItemList.append(item)
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                            continue
                        item = gameItemList[i]
                        if item == gameItemList[i]:
                            print(gameItemList[i] + "도 있고 ~ ", end="")
                            #time.sleep(1)
                    count += 1
                print("\n")
=======
                        gameItemList.append(item)
                        print(gameItemList[i] + "도 있고 ~ ", end="")
                        #time.sleep(1)
                        continue
                    item = gameItemList[i]
                    if item == gameItemList[i]:
                        print(gameItemList[i] + "도 있고 ~ ", end="")
                        #time.sleep(1)
                count += 1
            print("\n")
>>>>>>> f377f01aeb8b6c2807e3acc0ff168cc2ee2c06a9
