# Piro22_PythonGame_4

## 과제 협의사항

### 1. Commit Type

| Keyword | When to use |
| --- | --- |
| `feat`  | 기능 관련 커밋 |
| `fix` | 버그 수정 |
| `add` | 내용을 추가하였을 때 |
| `chore` | 기타 변경 사항 |

- 기능을 추가하거나 코드 수정하기 전 자주 커밋하기
- 주요 부분 완성할 때 마다 main에 merge 하여 자주 동기화
- Merge 할 때 마다 팀원들에게 전파하기

### 2. Branch

| Branch 종류 | 설명 |
| --- | --- |
| `main` | 메인 브랜치 |
| `member's name` | 담당 부분별 분업화 |

## 개발 규칙
1. 글로벌 변수 사용 시 팀원들에게 미리 알리기
2. 글로벌 변수명 규칙: 함수명_변수명
3. 각자 구현할 기능을 .py 파일에 함수로 구현 후 push
4. 함수명과 파일명 일치시키기
   - 예시: 
     - 함수명: `whaleGame()`
     - 파일명: `whaleGame.py`

## 프로젝트 소개
🍺 Pythond으로 즐기는 술게임 파티
실제 플레이어와 AI 친구들이 함께 즐기는 5가지 미니게임을 즐겨보세요. 게임에서 패배한 플레이어는 술을 마시게 되며, 자신의 주량에 도달하면 게임이 종료됩니다.

## Contributors

| 이름 | 담당 게임 |
|------|-----------|
| 홍다오 | 초기 프롬프트 & 숫자맞추기 |
| 박서정 | 가위바위보 하나빼기 |
| 한종서 | 시장에 가면 |
| 남경민 | 딸기 게임 |
| 조주영 | 좋아게임 |

## 모듈 기능 명세
```
📦 drinking-game
├── 📄 main.py
└── 📂 feature/
    ├── 📄 game.py
    ├── 📄 market_game.py
    ├── 📄 number_game.py
    ├── 📄 like_game2.py
    ├── 📄 rps_game.py
    └── 📄 strawberry_game.py 
```

## game.py
### 게임 진행 로직
1. 게임 선택 & 실행
   - 플레이어가 게임 선택
   - 선택된 게임 실행
   - 결과에 따라 `drink_players` 리스트 업데이트

2. 음주 처리
   - `drink_players`가 1명인 경우:
     - 해당 플레이어의 `drink()` 메서드 호출
     - 치사량 초과 시 → `gameover()`
   - 치사량 미도달 시:
     - 다음 게임 선택자로 지정
   - `drink_players`가 비어있는 경우:
     - 최다 음주자를 다음 선택자로 지정

### 함수 규격
- 반환 형식
- 모든 게임은 `[Player]` 형식의 결과를 반환
- `Player`: 벌주를 마셔야 하는 플레이어 객체
- 반환된 결과를 통해 `drink(amount)` 메서드를 호출하여 벌주 적용
  ```python
  [Player]  # 마실 플레이어 리스트 (1명 이상)
  []        # 마실 플레이어 없음
  ```

### 게임 종료 조건
1. 치사량 도달
   - 플레이어가 치사량 도달 시
   - `gameover()` 호출 후 프로그램 종료

2. 다음 턴 진행
   - 치사량 미도달 & `drink_players` 비어있음
   - 최다 음주자가 다음 게임 진행

## number_game.py
### `number_game(current_player, flag, is_real_player=False)`
숫자를 맞추는 업다운 게임
- 매개변수
  ```python
  current_player: Player  # 현재 플레이어 객체
  flag: int             # 게임 설명 출력 여부 (0: 출력)
  is_real_player: bool  # 실제 플레이어 여부 (기본값: False)
  ```

- 반환값
  ```python
  []                    # 성공: 아무도 마시지 않음
  [current_player]      # 실패: 현재 플레이어가 마심
  ```

### 게임 규칙
- 숫자 범위: 1-10
- 시도 기회: 5번
- 힌트 제공: Up/Down

## rps_game.py
### `rps_game(current_player,available_names, is_friend)`
가위바위보에서 승자를 제외한 패자들이 벌주를 마시는 게임
- 매개변수
  ```python
  current_player: Player     # 현재 플레이어 객체
  available_names: list[Player] # 지목 가능한 플레이어 목록
  is_friend: bool           # AI 플레이어 여부 (기본값: False)
  ```
- 반환값
  ```python
  [Player] or int: 현재플레이어만 루저이면 마셔야할 잔 수를 int로 반환, 이외의 경우 마셔야할 플레이어 리스트 반환
  ```


## market_game.py
### `market_game(me, name, players)`
"시장에 가면~" 순서 기억 게임
- 매개변수
  ```python
  me: str              # 현재 플레이어 이름
  name: str            # 게임 시작 플레이어 이름
  players: list[Player] # 게임 참여자 목록
  ```

- 반환값
  ```python
  [player]  # 실패: 실패한 플레이어가 마심
  ```

### 게임 규칙
- 이전 물건들을 순서대로 모두 말하기
- 새로운 물건 한 개 추가하기
- 순서가 틀리거나 물건을 뺴먹으면 실패

## strawberry_game.py
### `strawberry_game(straw_player_object, friend_list, is_friend=False)`
박자에 맞춰 '딸기'를 외치는 리듬 게임
- 매개변수
  ```python
  straw_player_object: Player    # 현재 플레이어 객체
  friend_list: list[Player]      # 게임 참여 가능한 다른 플레이어 목록
  is_friend: bool               # AI 플레이어 여부 (기본값: False)
  ```

- 반환값
  ```python
  [straw_player_object]     # 실패: 현재 플레이어가 마심
  [friend_list[ran_dead]]   # 성공: 랜덤으로 선택된 다른 플레이어가 마심
  ```

### 게임 규칙
- 박자에 맞춰 "딸기" 외치기
- Reverse 패턴 시 순서 역순 변경
- 패턴 실수 시 즉시 실패


## like_game2.py
### `game_like(player, all_players, current_player)`
플레이어들이 돌아가며 서로에게 고백하는 게임
- 매개변수
  ```python
  player: Player         # 실제 플레이어 객체
  all_players: list[Player] # 전체 플레이어 목록
  current_player: Player # 게임을 시작한 플레이어 객체
  ```

- 반환값
  ```python
  [rejected_player]   # 3번 거절: 거절당한 플레이어가 마심
  [current_player]    # 게임 종료: 게임 제안자가 마심
  ```

### 게임 규칙
- 기본 설정
  - 순서대로 고백 진행
  - 거절 3번 시 실패
  - 전체 턴 종료까지 실패자 없으면 제안자가 마심


## 회의 일정
- 01-05 23:00
- 01-06 21:00

## 마감일
- 01-07 10:00 (마지막 커밋 시간 기준)
