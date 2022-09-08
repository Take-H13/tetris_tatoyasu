# 対戦テトリス

このプログラムはテトリスを元に作られています。
ただし、細かいルールなどは若干異なっています。

## 目的

自動で対戦するテトリスのプレーヤーを作成する。

## 動作確認方法

tetris.pyを実行して、ゲームをやってみましょう。
ターミナルで本実験で使用するテトリスの動きが確認できます。

|キー|動作|
|:---:|:---|
|↑|回転|
|→ | 右に1マス|
|←|左に1マス|
|↓|下に1マス|
|スペース|一気に下|

## Scoreの計算方法

点数計算はすごく簡単で、新しいミノが追加されると5点、1列消すたびに100点、4列消せば400点となります。

## AIモード

自分で作ったAIの動きを確認する方法です。
今回はランダムに手を選ぶBotを動かしてみます。
ターミナルを2つ用意します。

最初にサーバを起動します。

```shell
python ai_mode.py
```

その次に、別のターミナルでAIを動かします。

```shell
python client.py
```

ゲームオーバーになるとAIの方は終わります。
サーバを修了したい場合は、**Ctrl-C**です。
**Ctrl-C**はコントロールキーを押しながら、キーのCを押します。

## 実験の方法
各自、Botのディレクトリを自分達のチーム名でコピーし、そのディレクトリのPlayer.pyを書き直して、強いAIを作成してみてください。

## 対戦モード
対戦のやり方は、ターミナルを3つ用意します。
1つは、サーバプログラムを走らせるため、残りは各クライアントを走らせるためです。

```shell
python3 battle.py
```

でサーバプログラムが立ち上がり、各クライアントの接続を待ちます。
2つのターミナルでそれぞれAIモードと同様にclientを動かせば、対戦が始まります。

自分が作ったAIと対戦したい場合は、

```shell
python3 human.py
```

と起動せれば、戦えます。
ただし、操作は起動したターミナルで行い、画面はbattle.pyに表示されています。
