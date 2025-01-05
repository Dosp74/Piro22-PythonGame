import random
import time

def 시장에가면(name, players, is_human):
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

    print("\n===== 시장에 가면~ =====")
    time.sleep(1)
    print("\n===== 시장에 가면~ =====\n")
    time.sleep(1)

    count = 1
    gameItemList = []
    while True:
        for player in players:
            print(player.name + " : 시장에 가면~ ", end="")
            if is_human: # is_human이 참일 때, 즉 나일 때
                is_human = False
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
                        return {player.name: 1}
                count += 1
            else:
                is_human = True
                time.sleep(1)
                for i in range(count): # 현재 로직: 봇은 무조건 게임 통과
                    gameItemListLength = len(gameItemList)
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

#시장에가면(players) # end=""로 가로 출력 시 출력 후 딜레이, 출력 후 딜레이 이런 식으로 생동감 있게 구현하려고 했으나 안 됨(뭐가 문제일까?)
