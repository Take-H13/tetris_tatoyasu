from Tatoyasu.cal_field import C_Board
from Tatoyasu.fitness import Fitness
import copy
import joblib

def get_candidate_list(board, pos, shape, model):
  # 落下予想したボードの情報配列
  #candidate = []
  # テトリミノは最大4回転する（2回転のものも4回転すると考える）
  rotate = 4
  # 動作
  move = [] 
  t_move = []
  fs = []
  # 各回転パターンに応じて動かす（2回しか回転しないものも4回行う）
  for i in range(rotate):
    cal_board = C_Board(board, pos, shape)
    n1_board = copy.deepcopy(cal_board)
    n1_board._rotate_block(i)

    l_num = 0
    # 左に寄せる
    while True:
      if not n1_board._move_block("left"):
        break
      l_num += 1
    # コピーを制作
    n2_board = copy.deepcopy(n1_board)
    r_num = 0
    while True:
      d_num = 0
      while True:
        if not n1_board._move_block("down"):
          #print([l_num, d_num, r_num]) # 左　下　右
          fitness = Fitness(n1_board.now_board())
          field_score = fitness.get_field_score()
          s = model.activate(field_score)
          fs.append(s)
          move.append([l_num, d_num, r_num])
          #print(np.array(n1_board.now_board()))
          break
        d_num += 1
      if not n2_board._move_block("right"):
        break
      r_num += 1
      n1_board = copy.deepcopy(n2_board)
    t_move.append(max(fs))
  return move[fs.index(max(fs))], t_move.index(max(t_move))