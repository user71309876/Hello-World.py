import random
import pygame
import os

pygame.init()#초기화

#화면 크기 설정
screen_width=480#게임화면 넓이
screen_height=640#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Nado Game")#게임 이름

#FPS
clock=pygame.time.Clock()

#경로 불러오기
current_path=os.path.dirname(__file__)# 현재 파일의 위치 반환
image_path=os.path.join(current_path,"images")

#이미지 불러오기
background=pygame.image.load(os.path.join(image_path,"background.png"))
character=pygame.image.load(os.path.join(image_path,"character.png"))
enemy=pygame.image.load(os.path.join(image_path,"enemy.png"))

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
enemy_x_pos=random.randint(0,410)#화면의 가로길이의 절반에 해당하는 곳에 위치
enemy_y_pos=0#화면의 세로길이의 맨 밑에 해당하는 곳에 위치

#폰트 정의
game_font=pygame.font.Font(None,40)#폰트 객체 생성(폰트,크기)

#총 시간
total_time=10

#시작 시간
start_ticks=pygame.time.get_ticks()#시작 ticks 정보 받아옴

#이벤트 루프
running=True
while running:
    dt=clock.tick(30)#게임 화면의 초당 프레임수 설정
    
    #똥이 바닥에 닫았는지 여부
    if enemy_y_pos>=640:
        enemy_y_pos=0
        enemy_x_pos=random.randint(0,410)
    
    for event in pygame.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pygame.QUIT:#게임 닫기
            running=False
        if event.type==pygame.KEYDOWN:#키가 눌러졌는지 확인(화살표 ↓이게 아님)
            if event.key==pygame.K_a:#캐릭터를 왼쪽으로
                to_x-=move
            elif event.key==pygame.K_d:#캐릭터를 오른쪽으로
                to_x+=move
    
        if event.type==pygame.KEYUP:#방향키를 떼면 멈춤
            #좌우, 상하키를 동시에 눌렀을 때 잘 안되서 코드를 바꿈
            if event.key==pygame.K_a:#캐릭터를 왼쪽으로
                to_x+=move
            elif event.key==pygame.K_d:#캐릭터를 오른쪽으로
                to_x-=move
                
    character_x_pos+=to_x*dt

            
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
        
    #똥이 내려가는 속도
    enemy_y_pos+=30
    
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
    
    #타이머
    elapsed_time=(pygame.time.get_ticks()-start_ticks)/1000
    #(경과시간-시작시간)/1000, millisecond이기 때문에
    
    timer=game_font.render(str(int(total_time-elapsed_time)),True,(0,0,0))
    #출력할 글자,true,글자 색상
    screen.blit(timer,(10,10))
    
    if total_time-elapsed_time<=0:
        print("타임 아웃")
        running=False
    
    pygame.display.update()#게임화면을 다시 그리기


#잠시 대기
pygame.time.delay(2000)

#pygame 종료
pygame.quit()