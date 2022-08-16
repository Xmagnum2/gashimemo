import os
import text

print(text.title);

print("まず本作のヒロインを選んでね。")
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
        print(text.game_over1)
    case "3":
        print("「え。。。」")
        input()
        print(text.game_over1)

print(text.select2)
select = input("数字を入力：")
match select:
    case "1":
        print("「・・・・・ごめん、やっぱ無理。」")
        input()
        print(text.game_over2)
    case "2":
        print(text.scenario3)
    case "3":
        print("「・・・キモッ」")
        input()
        print(text.game_over2)
        
print(text.select3)
select = input("数字を入力：")
match select:
    case "1":
        print(text.scenario4)
    case "2":
        print("「早すぎ、信じらんない。」")
        input()
        print(text.game_over3)
    case "3":
        print("「ちょっと頭おかしいんじゃないの？」")
        input()
        print(text.game_over3)

print(text.select4)
select = input("数字を入力：")
match select:
    case "1":
        print("「冗談じゃ。。。ないよ。。。」")
        print("そういって彼女は教室を飛び出した。")
        input()
        print(text.game_over4)
    case "2":
        print("「そっか、、、」")
        input()
        print(text.game_over4)
    case "3":
        print(text.scenario5)

print(text.select5)
select = input("数字を入力：")
match select:
    case "1":
        print("「あまいな、思えはもう死んでいる。」")
        input()
        print(text.game_over5)
    case "2":
        print("「雰囲気が台無しだよ。。。」")
        input()
        print(text.game_over5)
    case "3":
        print(text.scenario6)