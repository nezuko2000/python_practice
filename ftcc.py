# tracks = ["りんくさーきっと" , "つくばさーきっと" , "つくば1000" , "ぐんまサイクルスポーツセンター" , "ほんじょうサーキット" , "ふじスピードウェイ" , "オートパラダイスごてんば" , "セントラルサーキット"]
# tracks.sort(reverse=True)
# print(tracks)

# メソッドには戻り値があるとは限らない
# カーソルを乗せれば戻り値が返ってくるかがわかる(VSCodeのみの機能)

# 獲得ポイント計算

# rank = input("順位\n")
# cars = input("出走台数\n")
# position = int(cars) - int(rank) + 1
# points = (position - 1) * position / 2
# print(points)

# FTCCのシリーズポイント計算
def series_points(number_of_cars , rank):
# ポイント計算
    position = number_of_cars - rank + 1
    quantity = (position + 1) * position / 2
# バラストの計算
    ballast = quantity * 3
# リストリクターの計算
    restrictor = ballast  * 100 // 200
    return quantity , ballast , restrictor

quantity , ballast , resirictor = series_points(10 , 1)
print(quantity , ballast , resirictor)