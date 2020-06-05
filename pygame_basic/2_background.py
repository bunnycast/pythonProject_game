import pygame

pygame.init() # 반드시 초기화

# 화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("My Game") # 게임이름

# # 배경이미지 불러오기
# background = pygame.image.load("pygame_basic/background.001.png")


# # 이벤트 루프
# running = True # 게임이 돌고 있다
# while running:
#     for event in pygame.event.get():   # 이벤트 발생 체크
#         if event.type == pygame.QUIT: # X버튼 눌러 창을 끄는 이벤트 발생
#             running = False # 게임이 진행중이 아님
    
#     # screen.fill((0, 0, 255))
#     screen.blit(background, (0, 0)) # 배경그리기
 
#     pygame.display.update() # 게임화면 다시 그리기
    
# # pygame 종료
# pygame.quit()