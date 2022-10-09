import time
import joblib

from os.path import dirname, abspath
from Tatoyasu.do import Do
"""
import sys

parent_dir = dirname(dirname(dirname(abspath(__file__))))
if parent_dir not in sys.path:
  sys.path.append(parent_dir)

"""

# from Bot.candidate import get_candidate_list

ACTIONS = ['nop', 'rotate', 'down', 'left', 'right', 'drop']

class Player:
    def __init__(self, name):
        self.name = name
        self.move = []
        self.l = 0
        self.d = 0
        self.r = 0
        self.rotate = 0
    
    def act(self, info):
        """
        infoはlistになっていて、最初が自分の情報、それ以外は相手の情報があります。
        情報は、6つあり
            board: 確定しているボード(2次元リスト)
            next: 次のブロック3つ（IやOといった形状を表す文字）
            score:現時点でのスコア
            block: 現在操作しているブロックの形（IやOといった形状を表す文字）
            shape: 現在操作しているブロックの形状 (2次元リスト)
            pos: 現在操作しているブロックの位置
        """
        if self.l == 0 and self.d == 0 and self.r == 0 and self.rotate == 0:
          self.move, self.rotate = Do(info[0]["board"],info[0]["pos"],info[0]["shape"])
          self.l = self.move.pop(0)
          self.d = self.move.pop(0)
          self.r = self.move.pop(0)

        if self.l > self.r:
          self.l = self.l - self.r
          self.r = 0
        elif self.l == self.r:
          self.l = 0
          self.r = 0
        elif self.r > self.l:
          self.r = self.r - self.l
          self.l = 0

        if self.rotate > 0:
          self.rotate -= 1
          return "rotate"
      
        if self.l > 0:
          self.l -= 1
          return "left"
        elif self.r > 0:
          self.r -= 1
          return "right"
        elif self.d > 0:
          self.d -= 1
          return "down"
        else:
          return "drop"