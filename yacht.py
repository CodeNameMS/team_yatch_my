import random
from typing import Counter


class roll_dice : 
    # 주사위 굴리는 파트
    def Random_dice() :
        list = []  
        for i in range(5) :
            dice = random.randrange(1,6)
            list.append(dice)    
        return list

    # 주사위 교체 파트
    def Change_dice(query, dice_result) :
        while True :
            if query == 'y' or query == 'Y' :
                choice_list = []
                while True :
                    input_select = input("다시 굴릴 주사위 번호를 하나씩 입력 후 Enter(종료 F, 재입력 A) : ")
                    if input_select in ['1', '2', '3', '4', '5'] :
                        choice_list.append(input_select)
                        print("입력한 번호 : ", choice_list)
                        continue
                    elif input_select == 'a' or input_select == 'A':
                        print("번호 초기화!!")
                        choice_list = []
                    elif input_select == 'f' or input_select == 'F' :
                        print("주사위 선택 종료")
                        break
                    else :
                        print("유효하지 않은 값 입니다 !!")
                        continue
                
                # i가 choice_list를 쭈욱 훑음
                # 0번 인덱스부터 다시 굴려야하니까 -1
                for i in choice_list :
                    dice_result[int(i)-1] = random.randrange(1,6)
                return dice_result

            elif query == 'n' or query == 'N' :
                return dice_result

            else :
                print("유효하지 않은 값 입니다 !!")
                continue

class result_dice :
    #주사위 결과값 파트
    def Show_result(dice_result) :
        dice_list = {}
        dice_list['1번 주사위'] = dice_result[0]
        dice_list['2번 주사위'] = dice_result[1]
        dice_list['3번 주사위'] = dice_result[2]
        dice_list['4번 주사위'] = dice_result[3]
        dice_list['5번 주사위'] = dice_result[4]

        return dice_list

# main
print("프로그램을 시작합니다.")

print("1. 게임시작")
print("2. 게임설명")
input_start = input("입력 : ")
count = 0

while(count<3) :
    if input_start == "1" :
        #게임 시작 코드 추가 필요
        dice_result = roll_dice.Random_dice()
        print(dice_result)
        query = input("값을 바꾸시겠어요? (Y/N)")
        if query == 'y' or query == 'Y' :
            roll_dice.Change_dice(query, dice_result)
            show = result_dice.Show_result(dice_result)
            print(show)
        elif query == 'n' or query == 'N' :
            break
        else :
            print("유효하지 않은 값입니다 !! ")
            continue
        count+=1

    elif input_start == "2" :
    #게임 설명 코드 추가 필요
        pass