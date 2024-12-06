
import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def marketBasket(df):
    row_lists = df.values.tolist()
    #print(row_lists)
    return row_lists

#Assumes it does not need to drop any columns
def apriori_algorithm(dfs, threshold):
    for cluster in dfs:
        #Convert cluster to market basklet form
        
        dataset = marketBasket(cluster)

        te = TransactionEncoder()
        te_ary = te.fit(dataset).transform(dataset)
        df = pd.DataFrame(te_ary, columns=te.columns_)
        #print(df)
        #print(apriori(df, min_support=0.3, use_colnames=True))
        frequent_itemsets = apriori(df, min_support=threshold, use_colnames=True)
        ar = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.35, num_itemsets=len(df))
        return {'fItemSets': frequent_itemsets, 'AR': ar}

