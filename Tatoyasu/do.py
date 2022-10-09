from Tatoyasu.candidate import get_candidate_list
import joblib
#from Bot.network import Network

def Do(board, pos, shape):
  #model = Network()
  model = joblib.load("Tatoyasu/best_model.txt")
  return get_candidate_list(board, pos, shape, model)