import pandas as pd
import numpy as np


def get_user_item_predict_table(temp_dict):

    df = pd.DataFrame()
    for k, v in temp_dict.items():

        temp = pd.DataFrame()
        temp['user_id'] = [k for i in v]
        temp['item_id'] = v

        df = df.append(temp)
    return df


def get_actual_item(df_data):

    unique_item = set(df_data['item_id'].tolist())
    unique_user = set(df_data['user_id'].tolist())
    d_show = {}
    for i in unique_user:
        temp = {i : df_data[df_data['user_id'] == i]['item_id'].tolist()}
        d_show.update(temp)
    d_dontshow = {}
    for k,v in d_show.items():
        lst = list(unique_item).copy()
        for i in v:
            lst.remove(i)
        temp = {k : lst}
        d_dontshow.update(temp)
        
    return d_dontshow


def create_data(n_rows: int = 100, n_user: int = 15, n_item: int = 20):

    user_id = np.random.randint(1,n_user,size=(1,n_rows))
    item_id = np.random.randint(1,n_item,size=(1,n_rows))
    score = np.random.randint(1,5,size=(1,n_rows))
    data = np.concatenate((user_id,item_id,score),axis=0)
    data = data.T
    df_data = pd.DataFrame(data, columns=['user_id', 'item_id', 'score'])
    df_data = df_data.drop_duplicates(subset=['user_id','item_id'])
    
    df_data_X = df_data[['user_id', 'item_id']]
    df_data_scores = df_data['score']
    
    return df_data_X, df_data_scores



def create_train_data(data, n_item):

    grps = data.groupby('user_id').agg('count')['item_id']
    train_data = pd.DataFrame()

    for ind, v in zip(grps.index, grps):
        if v > n_item:
            temp = data[data['user_id'] == ind]
            train_data = train_data.append(temp)
            
    X = train_data[['user_id', 'item_id']]
    y = train_data['score']        
            
    return X, y