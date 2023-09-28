#   条件式と分岐
#   順番に一つずつ実行する”順次処理”
#   条件によって処理を選択”分岐処理”
#   条件に合致していると処理を繰り返す”反復処理”

#   Boolean型
#   TrueとFalseのみ
#   比較演算子

#   演算子	 条件
#   a < b	a は b より小さい
#   a <= b	a は b と等しいか小さい
#   a > b	a は b より大きい
#   a >= b	a は b と等しいか大きい
#   a == b	a と b は等しい
#   a != b	a と b は等しくない

print(2 < 2000)
print(2000 < 2)

#   練習
ranking = 334

if ranking <= 0:
    print(ranking)
    print("error !")
#   条件に合致すると"error !"と表示する
#   if文などの条件分岐の関数には文末に":"を付ける
#   最上段の条件が優先される
#   if ranking <= 3:を最上段にすると0以下での"予選通過！"が表示された
#   if　,　else　,　elif文の中はインデントを4つ付ける（自動で付く）
elif ranking <= 3:
    print("予選通過！")
#   ifにさらに条件を追加するときはelif
#   2つ目以降の条件は無限にelifを使う
else:
    print("予選落ち…")
#   if , elifいずれにも条件が合致しない場合にも処理したい場合にはelse

split1 = "*****************"
print(split1)

#   and演算子
ranking = 3
if (0 < ranking) and (ranking <= 3):
    print("予選通過！")
#   if文で複数の条件を指定する場合には() and ()の形で記述する
#   指定した条件が全てTrueでなければならない
#   これを論理積と呼ぶ

split2 = "----------------"
print(split2)

#   or演算子
ranking = 1
if (ranking == 1) or (ranking == 2) or (ranking == 3):
    print("予選通過！")
#   等しいことを示したいときは==で表す
#   orでいずれかの条件がTrueの時はTrueを出力するようにできる
#   これを論理和と呼ぶ

split3 = "~~~~~~~~~~~~~~~~~~"
print(split3)

#   not演算子
ranking = 10
formula = (ranking == 1) or (ranking == 2) or (ranking == 3)
if not (formula):
    print("予選落ち…")
#   notでFalseの時にTrueが出力される
#   これを否定と呼ぶ