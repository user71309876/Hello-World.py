
for week in range(1,51):
    with open(f"{week}주차.txt","w",encoding="utf8") as report_file:
        report_file.write(f"- {week} 주차 주간보고 -")
        report_file.write("\n부서 : ")
        report_file.write("\n이름 : ")
        report_file.write("\n업무요약 : ")