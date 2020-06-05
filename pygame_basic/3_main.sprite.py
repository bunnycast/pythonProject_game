import pygame

pygame.init() # 반드시 초기화

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game") # 게임이름

# 배경이미지 불러오기
background = pygame.image.load("pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터의 가로크기
character_height = character_size[1] # 캐릭터의 세로크기
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프
running = True # 게임이 돌고 있다
while running:
    for event in pygame.event.get():   # 이벤트 발생 체크
        if event.type == pygame.QUIT: # X버튼 눌러 창을 끄는 이벤트 발생
            running = False # 게임이 진행중이 아님
    
    screen.blit(background, (0, 0)) # 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))
 
    pygame.display.update() # 게임화면 다시 그리기
    
# pygame 종료
pygame.quit()