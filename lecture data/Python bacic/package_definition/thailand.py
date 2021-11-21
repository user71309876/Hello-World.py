class ThailandPackage:
    def detail(self):
        print("[Thailand Package 3 night 5 days] Bangkok, Pattaya tourism \
(night market tour) 50 million won")
        
if __name__=="__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈에서 직접 실행해야 실행되여")
    trip_to=ThailandPackage()
    trip_to.detail()
else:
    print("thailand 외부에서 호출하면 이 문장이 실행되여")