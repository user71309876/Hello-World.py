import pygame as pg
import os

pg.init()#pygame 초기화

#화면 크기 설정
screen_width=640#게임화면 넓이
screen_hight=480#게임화면 높이
screen=pg.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pg.display.set_caption("Nado Pang")#게임 이름

#FPS
clock=pg.time.Clock()

#경로 불러오기
current_path=os.path.dirname(__file__)# 현재 파일의 위치 반환
image_path=os.path.join(current_path,"images")

#배경 만들기
background=pg.image.load(os.path.join(image_path,"background.png"))
background_size=background.get_rect().size

#총알 가려주는 배경 만들기
background_hide=pg.image.load(os.path.join(image_path,"background_weapon_hide.png"))
background_hide_x_pos=0
background_hide_y_pos=370#(스크린 높이값)-(캐릭터 높이값)-(스테이지 높이값)

#스테이지 만들기
stage=pg.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

#캐릭터 만들기
character=pg.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(background_size[0]-character_width)/2
character_y_pos=background_size[1]-stage_size[1]-character_size[1]

#캐릭터 이동방향
character_to_x=0

#캐릭터 이동속도
character_speed=5

#무기 만들기
weapon=pg.image.load(os.path.join(image_path,"weapon.png"))
weapon_size=weapon.get_rect().size
weapon_width=weapon_size[0]

#무기는 한번에 여러 발 발사 가능
weapons=[]

#무기 이동 속도
weapon_speed=10

#공 만들기(4개 크기에 대해 따로 처리)
ball_images=[
    pg.image.load(os.path.join(image_path,"balloon1.png")),
    pg.image.load(os.path.join(image_path,"balloon2.png")),
    pg.image.load(os.path.join(image_path,"balloon3.png")),
    pg.image.load(os.path.join(image_path,"balloon4.png"))
]

#공 크기에 따른 최초 스피트
ball_speed_y=[-18,-15,-12,-9]

#공들
balls=[]

#최초 발생하는 큰 공 추가
balls.append({
    "pos_x":50, #공의 x 좌표, 여기서 시작한다 이말
    "pos_y":50, #공의 y 좌표, 여기서 시작한다 이말
    "img_idx":0, #공의 이미지 인덱스(여기선 balloon1)
    "to_x":3, # x축 이동방향
    "to_y":-6,# y축 이동방향
    "init_spd_y":ball_speed_y[0] #y로 최초속도
})

#사라질 무기, 공 정보 저장 변수
weapon_to_remove=-1#그냥 Null정보 저장햇다 생각하셈
ball_to_remove=-1

# font 정의
game_font=pg.font.Font(None,40)


total_time=100
start_ticks=pg.time.get_ticks()#시작 시간 정의

#게임 종료 메세지
#Time Over(시간 초과 실패), Mission Complete(성공), Game Over(캐릭터 공에 맞음)

game_result="Game over"
#이벤트 루프
running=True
while running:
    dt=clock.tick(30)#FPS 설정
    
    for event in pg.event.get():#이벤트 receive
        if event.type==pg.QUIT:#게임 닫기
            running=False
            
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_a:
                character_to_x-=character_speed
            elif event.key==pg.K_d:
                character_to_x+=character_speed
            elif event.key==pg.K_SPACE:
                weapon_x_pos=character_x_pos+character_width/2-weapon_width/2
                weapon_y_pos=character_y_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
                #총을 발사할때마다 weapon list에 weapon의 x,y 좌표가 캐릭터의 위치에 따라 찍힌다
                
        if event.type==pg.KEYUP:
            if event.key==pg.K_a:
                character_to_x+=character_speed
            elif event.key==pg.K_d:
                character_to_x-=character_speed
        
    #캐릭터 이동          
    character_x_pos+=character_to_x
    
    #캐릭터가 프레임을 넘었나 여부
    if character_x_pos<0:
        character_x_pos=0
    elif character_x_pos>screen_width-character_width:
        character_x_pos=screen_width-character_width
        
    #무기 위치 조정
    #weapons=[[w[0],w[1]-weapon_speed] for w in weapons]
    
    #천장에 닿은 무기 없애기
    weapons=[[w[0],w[1]-weapon_speed] for w in weapons if w[1]>0]
    """
    weapon의 항목 갯수만큼 반복함, weapon의 weapon_x_pos와 weapon_y_pos를 각각 w[0],과 w[1]에 넣음
    w[0]은 그데로, w[1]은 weapon_speed만큼 빼줌(weapon을 위로 올라가게 함)
    그리고 그 객체에 계산된 객체를 다시 넣어줌
    단, weapon의 y 좌표가 0이 될 때 그 리스트는 사라진다
    """
    
    #공 위치 정의
    for ball_idx, ball_val in enumerate(balls):#ball_idx는 lib의 key, ball_val는 lib의 value 넣음
        ball_pos_x=ball_val["pos_x"]#공의 x 좌표
        ball_pos_y=ball_val["pos_y"]#공의 y 좌표
        ball_img_idx=ball_val["img_idx"]#공 번호
        
        ball_size=ball_images[ball_img_idx].get_rect().size#공의 사이즈 불러오기
        ball_width=ball_size[0]#공의 넓이
        ball_height=ball_size[1]#공의 높이
        
        #가로벽에 닿았을 때 공 이동 위치 변경(튕겨나오는 효과)
        if ball_pos_x<0 or ball_pos_x>screen_width-ball_width:
            ball_val["to_x"]=ball_val["to_x"]*-1#"to_x" value를 마이너스 해준다
        
        #스테이지에 튕겨서 올라가는 처리    
        if ball_pos_y >=screen_hight-stage_height-ball_height:#바닥에 닿았을 경우
            #ball_val["to_y"]=ball_val["init_spd_y"]#고정된 (-18)이라는 가속도를 넣음 근데 난 이게 싫어서
            ball_val["to_y"]=ball_val["to_y"]*-1#작용,반작용으로 (-1)을 곱해줌
        else:#그 외 모든 경우에는 속도를 증가함
            ball_val["to_y"]+=0.5#밑으로 내려가니깐 +를 해줌
            #처음에는 ball_val["to_y"]가 -6으로 나와서 위로 올라감
        
        ball_val["pos_x"]+=ball_val["to_x"]#현재 속도를 더해주는 모습
        ball_val["pos_y"]+=ball_val["to_y"]
        
        
    #캐릭터 rect 정보 업데이트
    character_rect=character.get_rect()
    character_rect.left=character_x_pos
    character_rect.top=character_y_pos    
    """
    character_rect=character.get_rect()
    print(character_rect)
    는 출력 결과가 <rect(0, 0, 33, 60)> 이렇게 나오고
    
    character_rect=character.get_rect().size
    print(character_rect)
    는 출력 결과가 (33, 60) 이렇게 나온다
    
    즉, size가 없으면 크기(픽셀 단위)와 left(x 좌표),top(y 좌표)를 표시하지 않은 채로
            "pygame.Rect"형태로 호출
        size가 있으면 크기만 있는 tuple 형태로 호출한다
    """
    for ball_idx, ball_val in enumerate(balls):#모든 공에 대해 계산해야 되서 for문이 쓰임
        ball_pos_x=ball_val["pos_x"]
        ball_pos_y=ball_val["pos_y"]
        ball_img_idx=ball_val["img_idx"]
        
        #공 rect 정보 업데이트
        ball_rect=ball_images[ball_img_idx].get_rect()
        ball_rect.left=ball_pos_x
        ball_rect.top=ball_pos_y
        
        #공과 캐릭터 충돌 처리
        if character_rect.colliderect(ball_rect):
            running=False
            break
        
        #공과 무기들 충돌 처리
        for weapon_idx, weapon_val in enumerate(weapons):#모든 무기에 대해 계산해야 되서 for문이 쓰임
            weapon_pos_x=weapon_val[0]
            weapon_pos_y=weapon_val[1]
            
            #무기 rect 정보 업데이트
            weapon_rect=weapon.get_rect()
            weapon_rect.left=weapon_pos_x
            weapon_rect.top=weapon_pos_y
            
            #공과 무기 충돌 처리
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove=weapon_idx#해당 무기 없애기 위한 값 설정
                ball_to_remove=ball_idx#same as up line
                
                #가장 작은 크기의 공이 아니라면 다음 단계의 공으로 나누어주기
                if ball_img_idx<3:
                    
                    #현재 공 크기 정보
                    ball_width=ball_rect.size[0]
                    ball_height=ball_rect.size[1]
                    
                    #나눠진 공 정보
                    small_ball_rect=ball_images[ball_img_idx+1].get_rect()
                    small_ball_width=small_ball_rect.size[0]
                    small_ball_height=small_ball_rect.size[1]
                    
                    #왼쪽으로 튕겨나가는 작은 공
                    balls.append({
                        "pos_x":ball_pos_x+ball_width/2-small_ball_width/2, #공의 x 좌표, 여기서 시작한다 이말
                        "pos_y":ball_pos_y+ball_height/2-small_ball_height/2, #공의 y 좌표, 여기서 시작한다 이말
                        "img_idx":ball_img_idx+1, #공의 이미지 인덱스(여기선 balloon1)
                        "to_x":-3, # x축 이동방향
                        "to_y":-6,# y축 이동방향 
                        "init_spd_y":ball_speed_y[ball_img_idx+1] #y로 최초속도
                        })
                    #오른쪽으로 툉겨나가는 작은 공
                    balls.append({
                        "pos_x":ball_pos_x+ball_width/2-small_ball_width/2, #공의 x 좌표, 여기서 시작한다 이말
                        "pos_y":ball_pos_y+ball_height/2-small_ball_height/2, #공의 y 좌표, 여기서 시작한다 이말
                        "img_idx":ball_img_idx+1, #공의 이미지 인덱스(여기선 balloon1)
                        "to_x":3, # x축 이동방향
                        "to_y":-6,# y축 이동방향
                        "init_spd_y":ball_speed_y[ball_img_idx+1] #y로 최초속도
                        })
                break#for문 탈출
        else:#계속 게임을 진행
            continue#안쪽 for 문 조건이 맞지 않으면 coninue. 바깥 for 문 계속 수행
        break#안쪽 for 문에서 break 를 만나면 여기로 진입 가능. 2중 for 문을 한번에 탈출
    """
    for 바깥 조건:
        바깥 동작
        for 안쪽 조건:#for도 하나의 if였음!
            안쪽 동작
            if 충돌하면:
                break#안쪽 for문을 탈출함 그리고 바깥쪽 for문에 있는 break를 동작
                     #continue가 아니므로 바깥쪽 for문 조건으로 가지 않고 break로 감
        else#여기서 이 else는 for에 대한 else임. 즉, for문 조건이 끝났으면 else문으로 옴
            continue#여기서 다시 바깥 for문 실행. 
        break
    """
    
    #충돌된 무기,공 없애기
    if ball_to_remove>-1:
        del balls[ball_to_remove]
        ball_to_remove=-1
        
    if weapon_to_remove>-1:
        del weapons[weapon_to_remove]
        weapon_to_remove=-1
            
    if len(balls)==0:
        game_result="Mission Complete"
        running=False
    
    screen.blit(background,(0,0))#배경 호출
    
    for weapon_x_pos,weapon_y_pos in weapons:#weapon list로부터 x,y좌표를 입력받아
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))#출력시키는 모습
        
    screen.blit(background_hide,(background_hide_x_pos,background_hide_y_pos))
    
    for idx, val in enumerate(balls):
        ball_pos_x=val["pos_x"]
        ball_pos_y=val["pos_y"]
        ball_img_idx=val["img_idx"]
        screen.blit(ball_images[ball_img_idx],(ball_pos_x,ball_pos_y))
        #공 호출 해줍니다
        
    screen.blit(stage,(0,480-stage_height))#스테이지 호출
    screen.blit(character,(character_x_pos,character_y_pos))#캐릭터 호출
    
    #경과 시간 계산
    elapsed_time=(pg.time.get_ticks()-start_ticks)/1000
    timer=game_font.render(f"Time : {int(total_time-elapsed_time)}",True,(255,255,255))
    screen.blit(timer,(10,10))
    
    #시간 초과했다면
    if total_time-elapsed_time<=0:
        game_result="Time Over"
        running=False
        
    
    pg.display.update()#화면 다시 그리기

msg=game_font.render(game_result,True,(255,255,0))
msg_rect=msg.get_rect(center=(int(screen_width/2),int(screen_hight/2)))
screen.blit(msg,msg_rect)

pg.display.update()#화면 다시 그리기

pg.time.delay(2000)

#pygame 종료
pg.quit()