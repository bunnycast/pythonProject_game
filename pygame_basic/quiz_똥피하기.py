import random
import pygame
################################################################################################
# 기본 초기화 (필수)
pygame.init() 

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥피하기") 

# FPS
clock = pygame.time.Clock()
################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경이미지 불러오기
background = pygame.image.load("pygame_basic/bg.jpg")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("pygame_basic/dog.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1] 
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height 

# 이동할 좌표 
to_x = 0
character_speed = 10

#  적 캐릭터
enemy = pygame.image.load("pygame_basic/poop.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0] 
enemy_height = enemy_size[1] 
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 20

# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30) 

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():   
        if event.type == pygame.QUIT: 
            running = False 

    # 3. 게임 캐릭터 위치 정의        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

            
    character_x_pos += to_x
    
    #  가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    # 4. 충돌 처리
    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌각!")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0)) 
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    pygame.display.update() 

pygame.quit()