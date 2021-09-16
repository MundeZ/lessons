import numpy as np
import pandas as pd
from scipy.sparse.linalg import svds

class RecSysSVD:
    
    def __init__(self):
        pass
    
    
    def fit(self, df_data, df_scores):
        
        df_data['score'] = df_scores
        
        df_pivot_table = pd.pivot_table(df_data, values= 'score', index= 'user_id', columns= 'item_id')
        df_pivot_table = df_pivot_table.fillna(0)
        self.user_dict = {df_pivot_table.index.values[i] : i   for i in range(len(df_pivot_table.index.values))}
        self.item_dict = {df_pivot_table.columns.values[i] : i   for i in range(len(df_pivot_table.columns.values))}
        
        
        temp = df_pivot_table.values
        U, S, V = svds(temp, k = min(temp.shape)-1)
        S = np.diag(S)
        self.scores_table = np.dot(np.dot(U,S),V)
        self.temp_score = np.mean(self.scores_table)
        
    
    def predict(self, df_data):
        
        scores = []
        temp = df_data.values
        
        
        for i in range(temp.shape[0]):
            try:
                scores.append(self.predict_one(temp[i,0], temp[i,1]))
            except:
                scores.append('Error')
                
        return scores

    
    def predict_one(self, user, item):
        
        if user in self.user_dict.keys() and item in self.item_dict.keys():
            return abs(self.scores_table[self.user_dict[user]][self.item_dict[item]])
        else:
            return self.temp_score