import numpy as np

class Fitness():
  def __init__(self, board):
    self.tiles = board

  def get_field_score(self):
    area = np.array(self.tiles)
    # -- 高さについて --
    peaks = self.get_peaks(area)
    highest_peak = np.max(peaks)
    agg_height = np.sum(peaks)

    # -- 穴について --
    holes = self.get_holes(peaks, area)
    n_holes = np.sum(holes)
    n_cols_with_holes = np.count_nonzero(np.array(holes) > 0)

    # -- 行と列について --
    row_transitions = self.get_row_transition(area, highest_peak)
    col_transitions = self.get_col_transition(area, peaks)

    # -- 凸凹 --
    bumpiness = self.get_bumpiness(peaks)

    # -- ブロックがない場所について --
    num_pits = np.count_nonzero(np.count_nonzero(area, axis=0) == 0)

    # -- 井戸について --
    wells = self.get_wells(peaks)
    max_wells = np.max(wells)

    # -- 消去行について --
    cleard = area.min(axis=1).sum()

    return np.array([agg_height, n_holes, n_cols_with_holes, row_transitions, col_transitions, bumpiness, num_pits, max_wells, cleard])


  @staticmethod
  def get_peaks(area):
    peaks = np.array([])
    for col in range(area.shape[1]):
      if 1 in area[:, col]:
        p = area.shape[0] - np.argmax(area[:, col], axis=0)
        peaks = np.append(peaks, p)
      else:
        peaks = np.append(peaks, 0)
    return peaks

  @staticmethod
  def get_holes(peaks, area):
    holes = []
    for col in range(area.shape[1]):
      start = -peaks[col]
      if start == 0:
        holes.append(0)
      else:
        holes.append(np.count_nonzero(area[int(start):, col] == 0))
    return holes

  @staticmethod
  def get_row_transition(area, highest_peak):
    s = 0
    for row in range(int(area.shape[0] - highest_peak), area.shape[0]):
      for col in range(1, area.shape[1]):
        if area[row, col] != area[row, col - 1]:
          s += 1
    return s

  @staticmethod
  def get_col_transition(area, peaks):
    s = 0
    for col in range(area.shape[1]):
      if peaks[col] <= 1:
        continue
      for row in range(int(area.shape[0] - peaks[col]), area.shape[0] - 1):
        if area[row, col] != area[row + 1, col]:
          s += 1
    return s

  @staticmethod
  def get_bumpiness(peaks):
    s = 0
    for i in range(9):
      s += np.abs(peaks[i] - peaks[i + 1])
    return s

  @staticmethod
  def get_wells(peaks):
    wells = []
    for i in range(len(peaks)):
      if i == 0:
        w = peaks[1] - peaks[0]
        w = w if w > 0 else 0
        wells.append(w)
      elif i == len(peaks) - 1:
        w = peaks[-2] - peaks[-1]
        w = w if w > 0 else 0
        wells.append(w)
      else:
        w1 = peaks[i - 1] - peaks[i]
        w2 = peaks[i + 1] - peaks[i]
        w1 = w1 if w1 > 0 else 0
        w2 = w2 if w2 > 0 else 0
        w = w1 if w1 >= w2 else w2
        wells.append(w)
    return wells