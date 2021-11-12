def std_weight(hei,gen):
    if gen=="남자":
        print(f"키 {hei}cm 남자의 표준 체중은 {round(pow(hei,2)*22/10000,2)}kg 입니다")
    if gen=="여자":
        print(f"키 {hei}cm 여자의 표준 체중은 {round(pow(hei,2)*21/10000,2)}kg 입니다")

std_weight(gen="여자", hei=160)