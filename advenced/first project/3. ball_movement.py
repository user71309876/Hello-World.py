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

balloon1=pg.image.load(os.path.join(image_path,"balloon1.png"))
balloon2=pg.image.load(os.path.join(image_path,"balloon2.png"))
balloon3=pg.image.load(os.path.join(image_path,"balloon3.png"))
balloon4=pg.image.load(os.path.join(image_path,"balloon4.png"))


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
        
    screen.blit(background,(0,0))#배경 호출
    for weapon_x_pos,weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos,weapon_y_pos))
    screen.blit(background_hide,(background_hide_x_pos,background_hide_y_pos))
    screen.blit(stage,(0,480-stage_height))#스테이지 호출
    screen.blit(character,(character_x_pos,character_y_pos))#스테이지 호출
    
    pg.display.update()#화면 다시 그리기

#pygame 종료
pg.quit()