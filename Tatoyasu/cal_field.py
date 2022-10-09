import math

block_shapes = [
    # I Block - 2回転
    [[1], [1], [1], [1]],
    # O Block - 2回転
    [[1, 1],
     [1, 1]],
    # S Block - 2回転
    [[0, 1, 1],
     [1, 1, 0]],
    # Z Block - 2回転
    [[1, 1, 0],
     [0, 1, 1]],
    # J Block - 4回転
    [[0, 1],
     [0, 1],
     [1, 1]],
    # L Block - 4回転
    [[1, 0],
     [1, 0],
     [1, 1]],
    # T Block - 4回転
    [[0, 1, 0],
     [1, 1, 1]],
]

# 必要な情報：board , pos , direction < 行く先（移動方向） >, shape
class C_Board:
  def __init__(self, board, pos, shape):
    self.board = board
    self.current_block_pos = pos
    self.current_block_shape = shape

  def _rotate_block(self, loop):
    for i in range(loop):
      rotated_shape = list(map(list, zip(*self.current_block_shape[::-1])))
      if self._can_move(self.current_block_pos, rotated_shape):
        self.current_block_shape = rotated_shape

  def _move_block(self, direction):
    pos = self.current_block_pos
    if direction == "left":
      new_pos = [pos[0], pos[1] - 1]
    elif direction == "right":
      new_pos = [pos[0], pos[1] + 1] 
    elif direction == "down":
      new_pos = [pos[0] + 1, pos[1]]
    else:
      raise ValueError("wrong directions")

    if self._can_move(new_pos, self.current_block_shape):
      self.current_block_pos = new_pos
      return True
    elif direction == "down":
      self._land_block()
      return False
    else:
      return False

  def _land_block(self):
    size = C_Block.get_size(self.current_block_shape)
    for row in range(size[0]):
      for col in range(size[1]):
        if self.current_block_shape[row][col] == 1:
          self.board[self.current_block_pos[0] + row][self.current_block_pos[1] + col] = 1

  def _check_overlapping(self, pos, shape):
    size = C_Block.get_size(shape)
    for row in range(size[0]):
      for col in range(size[1]):
        if shape[row][col] == 1:
          if self.board[pos[0] + row][pos[1] + col] == 1:
            return True
    return False
  
  def _can_move(self, pos, shape):
    size = C_Block.get_size(shape)
    if pos[1] < 0 or pos[1] + size[1] > 10 or pos[0] + size[0] > 20:
      return False

    return not self._check_overlapping(pos, shape)

  def print_board(self):
    print(self.board)

  def now_board(self):
    return self.board
    
class C_Block:
  def __init__(self, block_type):
    self.shape = block_shapes[block_type]

  @staticmethod
  def get_size(shape):
    return [len(shape), len(shape[0])]