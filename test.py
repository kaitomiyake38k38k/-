"""
このファイルに解答コードを書いてください
"""

# ファイルの読み込み
f = open('input.txt', 'r')
datalist = f.readlines()

# 辞書作成用の配列の作成
num_list = []
word_list = []

# ファイルの内容を配列に格納
for i in datalist:
    # 行を":"で分割
    input_line = i.split(":")
    # 整数iを格納
    num_list.append(int(input_line[0]))
    # 要素が2以上であるか
    if len(input_line) >= 2:
        # 文字列sから改行コードを除いて配列に格納
        word_list.append(input_line[1].replace('\n', ''))

# 整数mを変数に格納
out_number = num_list[-1]

# 辞書の作成
dic = {key: val for key, val in zip(num_list[:-1], word_list)}

# keyの値でソート
dic_sorted = sorted(dic.items(), key=lambda x: x[0])

# 出力用の変数を定義
out = ""

for i in dic_sorted:
    # 整数mが整数iで割り切れたら
    if out_number % i[0] == 0:
        # 出力に文字列sを追加
        out = out+i[1]

if len(out) > 0:
    # outが1文字以降であればoutを出力
    print(out)
else:
    # outが0文字であればout_numberを出力
    print(out_number)
