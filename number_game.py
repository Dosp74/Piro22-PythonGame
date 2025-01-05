import random
import time

'''
   숫자맞추기(is_friend=False)
   ├── 1-10 사이 랜덤 숫자 생성
   ├── 최대 5번의 시도 기회
   │   ├── 실제 플레이어: 직접 숫자 입력
   │   └── AI 플레이어: 이전 결과 기반 추측
   └── 결과 반환
       ├── 성공: 0잔
       └── 실패: 1잔
'''

def 숫자맞추기(players, is_real_player=False):
    """
    1~10 사이의 숫자를 맞추는 게임
    Args:
        players (list): 참여하는 플레이어 목록
        is_real_player (bool): 실제 플레이어의 턴인지 여부
    Returns:
        dict: 각 플레이어별 마셔야 하는 잔 수
    """
    target = random.randint(1, 10)
    result = {}  # 각 플레이어별 마셔야 하는 잔 수
    
    print("\n=== 숫자 맞추기 게임 ===")
    print("1부터 10 사이의 숫자를 맞춰보세요!")
    print("기회는 5번 있습니다.")
    print("기회를 모두 사용하면 1잔을 마셔야 합니다!")
    
    for player in players:
        print(f"\n{player.name}의 차례!")
        attempts = 0
        max_attempts = 5
        previous_guesses = []
        
        while attempts < max_attempts:
            # if player != players[0]:  # AI 플레이어
            if is_real_player == True:
                time.sleep(1)
                if not previous_guesses:
                    guess = random.randint(1, 10)
                else:
                    min_val = max([g for g, r in previous_guesses if r == "Up"] + [1])
                    max_val = min([g for g, r in previous_guesses if r == "Down"] + [10])
                    guess = random.randint(min_val, max_val)
                print(f"\n{attempts + 1}번째 시도 - ", end="")
                time.sleep(0.5)
                print(f"{guess}!")
            else:  # 실제 플레이어
                try:
                    guess = int(input(f"\n{attempts + 1}번째 시도 - 숫자를 입력하세요: "))
                    if not 1 <= guess <= 10:
                        print("1부터 10 사이의 숫자를 입력해주세요!")
                        continue
                except ValueError:
                    print("올바른 숫자를 입력해주세요!")
                    continue
            
            attempts += 1
            
            if guess == target:
                print(f"정답입니다! {attempts}번 만에 맞추셨네요!")
                # result[player] = 0
                return 0
                break
            elif guess < target:
                result = "Up"
                print("Up! 더 큰 숫자입니다.")
            else:
                result = "Down"
                print("Down! 더 작은 숫자입니다.")
                
            if player != players[0]:
                previous_guesses.append((guess, result))
                
            if attempts == max_attempts:
                print(f"\n기회를 모두 소진했습니다. 정답은 {target}였습니다!")
                # result[player] = 1
                return 1
    
    # return result[player]
    return 0
