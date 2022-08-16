import os
import text

print(text.title);
name = input();

print(f"\nOK! これで始めるよ!! {name}")
print("では次に本作のヒロインを選んでね。")
input()


print(text.heroine_desc)

def check_heroine(str):
    match str:
        case "西":
            return True
        case "西ももか":
            return True
        case "西　ももか":
            return True
        case "ももか":
            return True
            
while(True):
    heroine = input("どの子を選ぶ？：")
    if check_heroine(heroine): break
    else: print("そんな名前の子いないよ！！")
heroine = "ももか"
print("ふーん。。。")
input()
print(f"じゃあ {heroine} を落とせるよう頑張ってね。")
input()
os.system('cls')
print(text.scenario1)
print(text.select1)
select = input("数字を入力：")
match select:
    case "1":
        print(text.scenario2)
    case "2":
        print("「そうだね。。。」")
        input()
        print(text.game_over)
    case "3":
        print("「え。。。」")
        input()
        print(text.game_over)