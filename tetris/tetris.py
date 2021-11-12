import pygame

pygame.init()#초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_height=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("TETRIS")#게임 이름

#FPS
clock=pygame.time.Clock()

#이미지 불러오기
block_black=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//tetris//block_black.png")
block_green=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//tetris//block_green.png")
block_black=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//tetris//block_black.png")


#폰트 정의
game_font=pygame.font.Font(None,40)#폰트 객체 생성(폰트,크기)

#총 시간
total_time=10

#시작 시간
start_ticks=pygame.time.get_ticks()#시작 ticks 정보 받아옴

move=30

#이벤트 루프
running=True
while running:
    dt=clock.tick(120)#게임 화면의 초당 프레임수 설정
    
    for event in pygame.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT:#게임 닫기
            running=False
        if event.type==pygame.KEYDOWN:#키가 눌러졌는지 확인(화살표 ↓이게 아님)
            if event.key==pygame.K_a:#캐릭터를 왼쪽으로
                to_x-=move
            elif event.key==pygame.K_d:#캐릭터를 오른쪽으로
                to_x+=move
            elif event.key==pygame.K_w:#캐릭터를 위로으로
                to_y-=move
            elif event.key==pygame.K_s:#캐릭터를 밑으로
                to_y+=move
    
    screen.blit(block_green,(100,100))
    
    pygame.display.update()#게임화면을 다시 그리기



#pygame 종료
pygame.quit()