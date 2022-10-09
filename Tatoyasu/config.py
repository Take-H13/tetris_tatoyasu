input_size = 9 # Networkモデルの入力
output_size = 1 # Networkモデルの出力
elitism_pct = 0.2 # 交叉（交配）を行う際に優秀な個体としてそのまま世代以降する割合
mutation_prob = 0.2 # 突然変異を行う確率
weights_mutate_power = 0.5 # 突然変異でのノイズ割合
weights_init_max = 1 # 初期ウェイト上限
weights_init_min = -1 # 初期ウェイト下限
device = 'cpu'