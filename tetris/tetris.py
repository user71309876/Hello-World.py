import pygame as pg
import os
from random import *

#초기화
pg.init()

#화면 크기 설정
screen_width=900#게임화면 넓이
screen_height=900#게임화면 높이
screen=pg.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pg.display.set_caption("TETRIS")#게임 이름

#FPS
clock=pg.time.Clock()

#경로 불러오기
current_path=os.path.dirname(__file__)# 현재 파일의 위치 반환
image_path=os.path.join(current_path,"images")

#배경 이미지 불러오기
background=pg.image.load(os.path.join(current_path,"background.png"))

#색깔 블럭 이미지 불러오기
bk_color=[
pg.image.load(os.path.join(current_path,"block_sky.png")),
pg.image.load(os.path.join(current_path,"block_blue.png")),
pg.image.load(os.path.join(current_path,"block_orange.png")),
pg.image.load(os.path.join(current_path,"block_yello.png")),
pg.image.load(os.path.join(current_path,"block_green.png")),
pg.image.load(os.path.join(current_path,"block_purple.png")),
pg.image.load(os.path.join(current_path,"block_red.png"))
]

#벽 이미지 불러오기
bk_wall1=pg.image.load(os.path.join(current_path,"block_wall1.png"))
bk_wall2=pg.image.load(os.path.join(current_path,"block_wall2.png"))
bk_wall3=pg.image.load(os.path.join(current_path,"block_wall3.png"))
bk_wall4=pg.image.load(os.path.join(current_path,"block_wall4.png"))

#버튼 이미지 불러오기
bt_unpush=[
pg.image.load(os.path.join(current_path,"button_up.png")),
pg.image.load(os.path.join(current_path,"button_down.png")),
pg.image.load(os.path.join(current_path,"button_right.png")),
pg.image.load(os.path.join(current_path,"button_left.png")),
pg.image.load(os.path.join(current_path,"button_E.png")),
]

#버튼 누른 이미지 불러오기
bt_push=[
pg.image.load(os.path.join(current_path,"button_push_up.png")),
pg.image.load(os.path.join(current_path,"button_push_down.png")),
pg.image.load(os.path.join(current_path,"button_push_right.png")),
pg.image.load(os.path.join(current_path,"button_push_left.png")),
pg.image.load(os.path.join(current_path,"button_push_E.png"))
]

#버튼 위치
bt_xypos=[
    (605,570),
    (605,680),
    (715,680),
    (495,680),
    (715,570)
]

#버튼 여부 라이브러리
bt_show=[0,0,0,0,0]

#설명 텍스트
des_txt=[
    "MOVE LEFT : A",
    "MOVE RIGHT : D",
    "MOVE DOWN : S",
    "TURN : W",
    "STRAIGHT DOWN : E"
]

#10*23 큰 통
buttle=[]
for i in range(0,23):
    buttle.append([10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,10])
buttle.append([7,7,7,7,7,7,7,7,7,7,7,7])#바닥 표시

#블럭 모양 정의
#블럭 최소 사각형의 맨 위 맨 왼쪽을 기준으로 삼는다
#블럭 모드 4개이므로 x,y좌표를 받고 턴한 계산값을 반환
class block:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def bk_turn(self,bk_pos):  
        mid=[]
        def_x=[]
        def_y=[]
        def_pos=[]
        for i in range(0,4):#최소 사각형의 맨 위 맨 왼쪽 좌표 구하기
            def_x.append(bk_pos[i][0])
            def_y.append(bk_pos[i][1])
        def_x.sort()#가장 작은 값을 구하기 위해 내림차순
        def_y.sort()
        def_pos=[def_x[0],def_y[0]]
        for i in range(0,4):#기본좌표를 뺀 후 x와 y를 reverse 시킴
            bk_pos[i][0]-=def_pos[0]
            bk_pos[i][1]-=def_pos[1]
            bk_pos[i].reverse()
            mid.append(bk_pos[i][0])
        mid.sort()#x값 중 큰 값과 작은 값을 위해 내림차순
        if mid[-1]+def_pos[0]>=380:
            def_pos[0]-=30
        rect_mid=((mid[0])+(mid[-1])+30)/2
        for i in range(0,4):
            bk_pos[i][0]=int(rect_mid*2-bk_pos[i][0]-30)#중간값에 대해 모든 좌표를 대칭이동
            bk_pos[i][0]+=def_pos[0]#빼줬던 기본값 더해주기
            bk_pos[i][1]+=def_pos[1]
        return bk_pos
    
    def bk_width(bk_pos):#넓이 구하기
        mid={}
        mid=set(mid)
        for i in range(0,4):
            mid.add(bk_pos[i][0])
        return int(len(mid)*30)
    
    def  bk_height(bk_pos):#높이 구하기
        mid={}
        mid=set(mid)
        for i in range(0,4):
            mid.add(bk_pos[i][1])
        return int(len(mid)*30)
    
    def def_x_pos(bk_pos):
        mid={}
        mid=set(mid)
        for i in range(0,4):
            mid.add(bk_pos[i][1])
        return int(mid[0])
class block0(block):#1번 블럭(일자 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        for i in range(0,4):
            self.bk_pos.append([x+i*30,y])#기본 블럭 좌표 생성
        
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[0],tuple(self.bk_pos[i]))
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)
class block1(block):#2번 블럭(ㄴ 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        self.bk_pos.append([x,y])
        for i in range(0,3):
            self.bk_pos.append([x+i*30,y+30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[1],tuple(self.bk_pos[i]))   
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)   
class block2(block):#3번 블럭(ㄴ 거꾸로 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        self.bk_pos.append([x+60,y])
        for i in range(0,3):
            self.bk_pos.append([x+i*30,y+30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[2],tuple(self.bk_pos[i]))    
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)   
class block3(block):#4번 블럭(ㅁ 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        for i in range(0,2):
            self.bk_pos.append([x+i*30,y])
            self.bk_pos.append([x+i*30,y+30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[3],tuple(self.bk_pos[i]))      
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)
class block4(block):#5번 블럭(오른쪽거북목 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        for i in range(0,2):
            self.bk_pos.append([x+30-i*30,y+i*30])
            self.bk_pos.append([x+60-i*30,y+i*30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[4],tuple(self.bk_pos[i]))     
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)
class block5(block):#6번 블럭(볼록할 철 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        self.bk_pos.append([x+30,y])
        for i in range(0,3):
            self.bk_pos.append([x+i*30,y+30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[5],tuple(self.bk_pos[i]))     
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)  
class block6(block):#7번 블럭(왼쪽거북목 블럭)
    def __init__(self,x,y):
        block.__init__(self,x,y)
        self.bk_pos=[]
        for i in range(0,2):
            self.bk_pos.append([x+i*30,y+i*30])
            self.bk_pos.append([x+i*30+30,y+i*30])
            
    def turn(self):
        self.bk_pos=block.bk_turn(self,self.bk_pos)
        
    def show(self):
        for i in range(0,4):
            screen.blit(bk_color[6],tuple(self.bk_pos[i]))
    
    def width(self):
        return block.bk_width(self.bk_pos)
    
    def height(self):
        return block.bk_height(self.bk_pos)
        
block_list=[block0,block1,block2,block3,block4,block5,block6]

now_block=[]

#폰트 정의
game_font=pg.font.Font(None,30)#폰트 객체 생성(폰트,크기)

#시작 시간
start_ticks=pg.time.get_ticks()#시작 ticks 정보 받아옴

#while문을 간결히 하기 위한 함수
def UWall():#테스리스 u자 틀
    screen.blit(bk_wall1,(50,50))
    screen.blit(bk_wall2,(80,740))
    screen.blit(bk_wall1,(380,50)) 
def NextBkWall():#다음 도형 칸
    screen.blit(bk_wall3,(470,50))
    screen.blit(bk_wall3,(470,220))
    screen.blit(bk_wall4,(470,80))
    screen.blit(bk_wall4,(800,80))
def NextBkTxt():#다음 도형 텍스트
    next_txt=game_font.render("-NEXT-",True,(0,0,0))
    screen.blit(next_txt,(510,90))  
def HelpWall():#도움말칸
    screen.blit(bk_wall3,(470,280))
    screen.blit(bk_wall3,(470,280+230))
    screen.blit(bk_wall4,(470,280+30))
    screen.blit(bk_wall4,(470+330,280+30))
    screen.blit(bk_wall4,(470,280+110))
    screen.blit(bk_wall4,(470+330,280+110))               
def HelpTxt():#정보 텍스트
    for idx,val in enumerate(des_txt):
        next_txt=game_font.render(val,True,(0,0,0))
        screen.blit(next_txt,(470+40,280+idx*40+40)) 
def Dire():#방향키
    for i in range(0,5):
        if bt_show[i]==1:
            screen.blit(bt_push[i],bt_xypos[i])
        else:
            screen.blit(bt_unpush[i],bt_xypos[i])
#처음 나올 모형
first_block=randint(0,6)
now_block_x_pos=170
now_block_y_pos=50
now_block_x_to_pos=0
now_block_y_to_pos=0

#도형 자유낙하시 내려가는 시간 이전 시간
pre_time=0

#도형 속도
block_speed=30

#밑바닥에 닿았는지 여부
block_ready=1


#이벤트 루프
running=True
while running:
    dt=clock.tick(30)#게임 화면의 초당 프레임수 설정
    
    if block_ready==1:
        next_block=randint(0,6)
        now_block=block_list[first_block](now_block_x_pos,now_block_y_pos)
        block_ready=0
        now_block_color=first_block
        first_block=next_block
    
    for event in pg.event.get():#어떤 이벤트가 발생하였는가
        if event.type==pg.QUIT:#게임 닫기
            running=False
            
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_w:#돌리기
                now_block.turn()
                bt_show[0]=1
            elif event.key==pg.K_s:#밑
                now_block_y_to_pos+=block_speed
                bt_show[1]=1
            elif event.key==pg.K_d:#오른쪽
                now_block_x_to_pos+=block_speed
                bt_show[2]=1
            elif event.key==pg.K_a:#왼쪽
                now_block_x_to_pos-=block_speed
                bt_show[3]=1
            elif event.key==pg.K_e:#스트레이트
                bt_show[4]=1
                
        if event.type==pg.KEYUP:
            if event.key==pg.K_w:#돌리기
                bt_show[0]=0
            elif event.key==pg.K_s:#밑
                now_block_y_to_pos-=block_speed
                bt_show[1]=0
            elif event.key==pg.K_d:#오른쪽
                now_block_x_to_pos-=block_speed
                bt_show[2]=0
            elif event.key==pg.K_a:#왼쪽
                now_block_x_to_pos+=block_speed
                bt_show[3]=0
            elif event.key==pg.K_e:#스트레이트
                bt_show[4]=0
    
    #도형 x,y좌표 움직여 주기
    for i in range(0,4):
        now_block.bk_pos[i][0]+=now_block_x_to_pos
        now_block.bk_pos[i][1]+=now_block_y_to_pos
        
    #도형을 밑으로 내리는 것
    ela_time=int((pg.time.get_ticks()-start_ticks)/1000)
    if pre_time!=ela_time:
        for i in range(0,4):
            now_block.bk_pos[i][1]+=30
        pre_time=ela_time
        
    #양 옆으로 도형 및 벽 닿는거 처리
    for i in range(0,4):
        if buttle[int((now_block.bk_pos[i][1]-50)/30)][int((now_block.bk_pos[i][0]-80)/30+1)]==10:
            for i in range(0,4):
                now_block.bk_pos[i][0]-=now_block_x_to_pos
            break
        # if buttle[int((now_block.bk_pos[i][1]-50)/30)][int((now_block.bk_pos[i][0]-80)/30-1)]==10:
        #     print("hi")
        #     for i in range(0,4):
        #         now_block.bk_pos[i][0]+=block_speed
        #     break
        
    #큰 통에 도형 넣어주기 and 밑바닥에 닫는지 여부
    for i in range(0,4):
        if -1<buttle[int((now_block.bk_pos[i][1]-50)/30+1)][int((now_block.bk_pos[i][0]-80)/30+1)]<8:
            block_ready=1
            for i in range(0,4):
                y=int((now_block.bk_pos[i][0]-80)/30)+1
                x=int((now_block.bk_pos[i][1]-50)/30)
                buttle[x][y]=int(now_block_color)
        else:
            continue
        del now_block
        break
        
    screen.blit(background,(0,0))#배경 불러오기    
    UWall()#테트리스 U자 틀   
    NextBkWall()#다음 도형 칸
    NextBkTxt()#다음 도형 텍스트
    HelpWall()#도움말칸
    HelpTxt()#도움말텍스트
    Dire()#방향키
    block_list[next_block](570,120).show()
    if block_ready==0:
        now_block.show()
    #시간 표시
    ela_time=int((pg.time.get_ticks()-start_ticks)/1000)
    screen.blit(game_font.render(str(ela_time),True,(0,0,0)),(750,90))
    
    #
    for i in range(0,23):
        for j in range(0,12):
            if -1<buttle[i][j]<8:
                screen.blit(bk_color[buttle[i][j]],(j*30+50,i*30+50))
    
    first_block_pro=0
    pg.display.update()#게임화면을 다시 그리기

#pg 종료
pg.quit()
"""
남은 과업
줄 없애는 코드 만들기
(optional)점수 만들기
(optional)단계 만들기
자잘한 버그 고치기
"""