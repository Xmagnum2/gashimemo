import os
import text

print(text.title);
input()
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
        case "西 ももか":
            return True
        case "ももか":
            return True
        case "北 ひなた":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "北　ひなた":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "ひなた":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "北":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "南 なぎさ":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "南　なぎさ":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "なぎさ":
            print("あー、その子今別の客対応中ですね。")
            return False
        case "南":
            print("あー、その子今別の客対応中ですね。")
            return False
        case _:
            print("そんな名前の子いないよ！！")
            return False

while(True):
    heroine = input("どの子を選ぶ？：")
    if check_heroine(heroine): break
heroine = "ももか"
print("ふーん。。。")
input()
print(f"じゃあ {heroine} を落とせるよう頑張ってね。")
input()
os.system('cls')
print(text.scenario1)
print(text.select1)
select = ""
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break

match select:
    case "1":
        print(text.scenario2)
    case "2":
        print("「そうだね。。。」")
        input()
        print(text.game_over1)
        exit()
    case "3":
        print("「え。。。」")
        input()
        print(text.game_over1)
        exit()

print(text.select2)
select = ""
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break
match select:
    case "1":
        print("「・・・・・ごめん、やっぱ無理。」")
        input()
        print(text.game_over2)
        exit()
    case "2":
        print(text.scenario3)
    case "3":
        print("「・・・キモッ」")
        input()
        print(text.game_over2)
        exit()

print(text.select3)
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break
match select:
    case "1":
        print(text.scenario4)
    case "2":
        print("「早すぎ、信じらんない。」")
        input()
        print(text.game_over3)
        exit()
    case "3":
        print("「ちょっと頭おかしいんじゃないの？」")
        input()
        print(text.game_over3)
        exit()

print(text.select4)
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break
match select:
    case "1":
        print("「冗談じゃ。。。ないよ。。。」")
        print("そういって彼女は教室を飛び出した。")
        input()
        print(text.game_over4)
        exit()
    case "2":
        print("「そっか、、、」")
        input()
        print(text.game_over4)
        exit()
    case "3":
        print(text.scenario5)

print(text.select5)
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break
match select:
    case "1":
        print("「あまいな、思えはもう死んでいる。」")
        input()
        print(text.game_over5)
        exit()
    case "2":
        print("「雰囲気が台無しだよ。。。」")
        input()
        print(text.game_over5)
        exit()
    case "3":
        print(text.scenario6)

print(text.select6)
while(True):
    select = input("数字を入力：")
    if select in ["1", "2", "3"]: break
match select:
    case "1":
        print("「えっ！？」")
        input()
        print(text.scenario7)
    case "2":
        print("「シンプルにめんどくさい」")
        input()
        print(text.game_over6)
        exit()
    case "3":
        print("「わたしは床で寝るからあなたは外で寝てね」")
        input()
        exit()
        print(text.game_over6)
