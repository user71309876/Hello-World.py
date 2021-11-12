import pygame

pygame.init()#초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_height=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#FPS
clock=pygame.time.Clock()

#이미지 불러오기
background=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//background.png")
character=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//character.png")
enemy=pygame.image.load("C://Users//꼴뽁딱찌//Desktop//Python Popping a Balloon//enemy.png")

#캐릭터 불러오기
character_size=character.get_rect().size#이미지의 크기를 구해옴
character_width=character_size[0]#캐릭터의 가로사이즈
character_height=character_size[1]#캐릭터의 세로사이즈
character_x_pos=(screen_width-character_width)/2#화면의 가로길이의 절반에 해당하는 곳에 위치
character_y_pos=screen_height-character_height#화면의 세로길이의 맨 밑에 해당하는 곳에 위치

#이동할 좌표
to_x=0
to_y=0

#이동속도
move=0.6

#enemy character
enemy_size=enemy.get_rect().size#이미지의 크기를 구해옴
enemy_width=enemy_size[0]#캐릭터의 가로사이즈
enemy_height=enemy_size[1]#캐릭터의 세로사이즈
enemy_x_pos=(screen_width-enemy_width)/2#화면의 가로길이의 절반에 해당하는 곳에 위치
enemy_y_pos=(screen_height-enemy_height)/2#화면의 세로길이의 맨 밑에 해당하는 곳에 위치



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
    
        if event.type==pygame.KEYUP:#방향키를 떼면 멈춤
            #좌우, 상하키를 동시에 눌렀을 때 잘 안되서 코드를 바꿈
            if event.key==pygame.K_a:#캐릭터를 왼쪽으로
                to_x+=move
            elif event.key==pygame.K_d:#캐릭터를 오른쪽으로
                to_x-=move
            elif event.key==pygame.K_w:#캐릭터를 위로으로
                to_y+=move
            elif event.key==pygame.K_s:#캐릭터를 밑으로
                to_y-=move

                
    character_x_pos+=to_x*dt
    character_y_pos+=to_y*dt
            
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
        
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height
    
    #충돌처리
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos
    
    enemy_rect=enemy.get_rect()
    enemy_rect.left=enemy_x_pos
    enemy_rect.top=enemy_y_pos
    
    #충돌 체크
    if character_rect.colliderect(enemy_rect):#character가 enemy와 충돌했는가
        print("충돌했어요")
        running=False
        
            
    screen.blit(background,(0,0))#배경 그리기    
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    
    pygame.display.update()#게임화면을 다시 그리기

#pygame 종료
pygame.quit()