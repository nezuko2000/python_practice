#   input関数
# input("なまえをいれてください\n")
#   ターミナル上で文字が入力できるようになる
#   input()の()内の文字は入力して欲しい文字の説明
#   これをプロンプトと呼ぶ

#   "\n"と入力するとターミナル上で改行される

# string = input("なまえをいれてください\n")
# print("あなたの名前は" , string , "ですね？")

# answre = input("Yes? No?\n")
# print("おや？アンタの名前は" , string , "というのかい？")
# print("贅沢な名だねぇ……")
# print("今日からお前の名はnullだよ！いいね？null!")



# nで始まる英単語の配列
# n_words = ["name", "number", "nature", "need", "new", "night", "noise", "note", "nurse", "north"]

# 配列の要素を出力
# for word in n_words:
    # print(word)

# import random

# 英単語のリストを用意してください
# words = ["apple", "banana", "cherry", "date", "elephant", "fox", "grape", "honey", "iguana", "jackal", "kiwi", "lemon", "mango"]

# プロンプトで文字列を入力
# user_input = input("ローマ字の文字列を入力してください: ")

# 入力文字列の先頭1文字を取得
# first_letter = user_input[0]

# 先頭文字が一致する単語を抽出
# matching_words = [word for word in words if word.startswith(first_letter)]

# if matching_words:
    # ランダムに単語を選択して回答
    # random_word = random.choice(matching_words)
    # print(f"回答: {random_word}")
# else:
    # print("該当する単語が見つかりませんでした。")

# peach = input("桃の個数\n")
# orange = input("みかんの個数\n")
# print("太郎君は一個100円の桃を" , peach , "個、一個40円のみかんを" , orange , "個買いました。全部でいくらになったでしょうか？")
# print(100 * int(peach) + 40 * int(orange) , "円")

#   ももとみかんの個数から合計金額を計算する関数を作ってみる
#   関数の定義
#   "def [関数名]([引数名1] , [引数名2] , ......)"で関数の定義は始まる
#   "関数名"は処理の内容を連想しやすい名前にする
#   行の終わりには":"が必要
tax_rate = 1.1
def fruit_price(peach , orange):
#    ↓は関数自体の処理を記述する
    print("太郎君は一個100円の桃を" , peach , "個、一個40円のみかんを" , orange , "個買いました。全部でいくらになったでしょうか？")
    print(100 * int(peach) * tax_rate + 40 * int(orange) * tax_rate , "円")
# "ctrl" + "/"で一瞬でコメントアウトできる
fruit_price(30 , 40)
fruit_price(6 , 3)
fruit_price(9 , 6)
# def内の引数は自動的に変数として認識される

def fruit_price_return(peach , orange):
    text = "太郎君は一個100円の桃を" + str(peach) + "個、一個40円のみかんを" + str(orange) + "個買いました。全部でいくらになったでしょうか？\n" + str(100 * int(peach) * tax_rate + 40 * int(orange) * tax_rate) + "円"
    return text

# return文を使うとデータの処理とデータの表示を分けることができる
# 処理と表示を分けることでデバッグがしやすくなる(処理を小分けにする)

fruits = fruit_price_return(2 , 10)
print(fruits)
