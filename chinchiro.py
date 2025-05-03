import random

def roll_dice():
    return sorted([random.randint(1, 6) for _ in range(3)])

def judge(dice):
    if dice == [1, 1, 1]:
        return ("ピンゾロ", 100)
    if dice[0] == dice[1] == dice[2]:
        return (f"{dice[0]}ゾロ", 50 + dice[0])
    if dice == [4, 5, 6]:
        return ("シゴロ", 40)
    if dice == [1, 2, 3]:
        return ("ヒフミ", 10)
    if dice[0] == dice[1]:
        return (f"目あり（{dice[2]}）", 20 + dice[2])
    if dice[1] == dice[2]:
        return (f"目あり（{dice[0]}）", 20 + dice[0])
    if dice[0] == dice[2]:
        return (f"目あり（{dice[1]}）", 20 + dice[1])
    return ("出目なし", 0)

def play():
    print("🎲 帝愛式チンチロリン：プレイヤー vs 班長（3回戦＋賭け金あり）\n")

    player_pelica = 10000
    bet_amount = 3000  # 毎戦の掛け金

    for round_num in range(1, 4):
        print(f"==== 第{round_num}回戦 ====")
        print(f"💴 所持ペリカ: {player_pelica}ペリカ")
        print(f"💰 賭け金: {bet_amount}ペリカ")

        if player_pelica < bet_amount:
            print("😱 ペリカが足りない……勝負不能ッ……！！")
            break

        input("Enterでサイコロを振れッ……！")

        # プレイヤーのターン
        player_dice = roll_dice()
        player_result, player_score = judge(player_dice)
        print(f"🎮 君の出目: {player_dice} → {player_result}（スコア: {player_score}）")

        input("……班長のターンだ。Enterで続行ッ……")

        # 班長のターン
        cpu_dice = roll_dice()
        cpu_result, cpu_score = judge(cpu_dice)
        print(f"👴 班長の出目: {cpu_dice} → {cpu_result}（スコア: {cpu_score}）")

        # 勝敗判定とペリカの増減
        if player_score > cpu_score:
            player_pelica += bet_amount
            print(f"🔥 勝利ッ！！ +{bet_amount}ペリカ！！")
        elif player_score < cpu_score:
            player_pelica -= bet_amount
            print(f"💀 負けた…… -{bet_amount}ペリカ……")
        else:
            print("🤝 引き分け……賭けは戻るッ")

        print(f"💼 現在のペリカ: {player_pelica}ペリカ\n")

    print("===== 最終結果 =====")
    print(f"🏁 最終所持ペリカ: {player_pelica}ペリカ")

    if player_pelica > 10000:
        print("🎉 地上昇格ッ……カツ丼だッ！！")
    elif player_pelica < 10000:
        print("🥶 もっと働け……地下行き続行ッ！！")
    else:
        print("😐 増えも減りもしなかった……小市民だな……")

if __name__ == "__main__":
    play()


# このコード……これはただのPythonコードではない……
# 「賭博破戒録カイジ」に登場する地獄の遊戯「チンチロリン」……
# それを──再現したものッ……ッ！！

# プレイヤーは3回勝負を行うッ！！
# 各ラウンドで命（ペリカ）を賭けて班長と勝負ッ！

# サイコロは3つ……それを振り、出目によって勝敗を判定……
# ピンゾロ・ゾロ目・シゴロ・ヒフミ……
# 目あり、そして無慈悲なる“出目なし”……
# その判定は、全てこのコードの中に詰め込まれているッ……！
# それぞれの出目に応じて、ペリカが増えたり減ったりするッ！！
#ちなみに中の人情報だがしょんべんは実装すんのめんどかったから実装しなかったぜ.....

# 勝てば賭け金分のペリカを得るッ！
# 負ければ減るッ！
# ただそれだけ……ただそれだけだが……
# そこには──圧倒的緊張と絶望があるッ！！

# 勝負は3戦……最終的な所持ペリカで地上昇格か、地下行き続行か……
# 地獄の分かれ道が、今このファイルの中にあるッ……！

# ※ このプログラムは福本伸行先生の作品に対する敬意をもって制作された非公式ファンコンテンツです。
# ※ 利用には商業目的は一切含まれておらず、教育・趣味・リスペクトに基づいて公開されています。
# ※ 使用しているのはPythonの標準ライブラリのみ──つまり、地上で誰でも動かせるッ！
# ※ ただし、実行にはPython3.13のインストールが必要です。
# ※ もしこのコードを見て「チンチロリン」をやりたくなったら、ぜひ本作を読んでみてください。
# ※ それでは、地獄の遊戯を楽しんでください……！！


