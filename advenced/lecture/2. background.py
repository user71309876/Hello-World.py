import pygame

pygame.init()#초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_hight=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#배경 이미지 불러오기
background=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//background.png")

#이벤트 루프
running=True
while running:
    for event in pygame.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT:#게임 닫기
            running=False
    
    screen.blit(background,(0,0))#배경 그리기
    #screen.fill((0,0,255))#rgb값을 출력
    
    
    pygame.display.update()#게임화면을 다시 그리기

#pygame 종료
pygame.quit()