import pygame

pygame.init()#초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_height=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#배경 이미지 불러오기
background=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//background.png")

#캐릭터 불러오기
character=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//character.png")
character_size=character.get_rect().size#이미지의 크기를 구해옴
character_width=character_size[0]#캐릭터의 가로사이즈
character_height=character_size[1]#캐릭터의 세로사이즈
character_x_pos=(screen_width-character_width)/2#화면의 가로길이의 절반에 해당하는 곳에 위치
character_y_pos=screen_height-character_height#화면의 세로길이의 맨 밑에 해당하는 곳에 위치

#이벤트 루프
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT:#게임 닫기
            running=False
    
    screen.blit(background,(0,0))#배경 그리기    
    
    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update()#게임화면을 다시 그리기

#pygame 종료
pygame.quit()