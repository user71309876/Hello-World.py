import pygame
import os

pygame.init()#pygame 초기화

#화면 크기 설정
screen_width=640#게임화면 넓이
screen_hight=480#게임화면 높이
screen=pygame.display.set_mode((screen_width,screen_hight))

#화면 타이틀 설정
pygame.display.set_caption("Nado Pang")#게임 이름

#FPS
clock=pygame.time.Clock()

#경로 불러오기
current_path=os.path.dirname(__file__)# 현재 파일의 위치 반환
image_path=os.path.join(current_path,"images")

#배경 만들기
background=pygame.image.load(os.path.join(image_path,"background.png"))
background_size=background.get_rect().size

#스테이지 만들기
stage=pygame.image.load(os.path.join(image_path,"stage.png"))
stage_size=stage.get_rect().size
stage_height=stage_size[1]

#캐릭터 만들기
character=pygame.image.load(os.path.join(image_path,"character.png"))
character_size=character.get_rect().size
character_width=character_size[0]
character_height=character_size[1]
character_x_pos=(background_size[0]-character_width)/2
character_y_pos=background_size[1]-stage_size[1]-character_size[1]

weapon=pygame.image.load(os.path.join(image_path,"weapon.png"))
balloon1=pygame.image.load(os.path.join(image_path,"balloon1.png"))
balloon2=pygame.image.load(os.path.join(image_path,"balloon2.png"))
balloon3=pygame.image.load(os.path.join(image_path,"balloon3.png"))
balloon4=pygame.image.load(os.path.join(image_path,"balloon4.png"))


#이벤트 루프
running=True
while running:
    for event in pygame.event.get():#이벤트 receive
        if event.type==pygame.QUIT:#게임 닫기
            running=False
    
    screen.blit(background,(0,0))#배경 호출
    screen.blit(stage,(0,480-stage_height))#스테이지 호출
    screen.blit(character,(character_x_pos,character_y_pos))#스테이지 호출
    
    
    pygame.display.update()#화면 다시 그리기

#pygame 종료
pygame.quit()