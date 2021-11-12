import pygame

pygame.init()#pygame 초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_hight=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#이벤트 루프
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT:#게임 닫기
            running=False

#pygame 종료
pygame.quit()