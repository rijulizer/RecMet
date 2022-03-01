import numpy as np

import pyspark.sql.functions as sf
from pyspark.sql.types import FloatType

class Metrics:
    def __init__(self, weights, longtail_thresh):
        self.weights = weights
        self.longtail_thresh = longtail_thresh

    # Average Intersection
    def AI(self, recommended, actual) -> float:
        
        common_num = len(list(set(actual).intersection(set(recommended))))
        AI = round(common_num/ min(len(actual), len(recommended)), 4)
        
        return AI

    # Popularity Weighted Avergae Intersection PWAI
    def PWAI(self, recommended, actual):
        
        # Set the smaller set as denominator
        if len(actual)<= len(recommended):
            denom_elem = actual
        else:
            denom_elem = recommended
        
        common_num_elem = list(set(actual).intersection(set(recommended)))
        # weighted sum of numerator elements
        num = np.array([self.weights[x] for x in common_num_elem]).sum()
        denom = np.array([self.weights[x] for x in denom_elem]).sum()      

        return float(round(num/denom, 4))
    
    def ARP(self, recommended):
        item_weights = np.array([self.weights[x] for x in recommended])
        arp = item_weights.mean()

        return float(round(arp, 4))
    
    def APLT(self, recommended):
        item_weights = np.array([self.weights[x] for x in recommended])
        avg_longtail_items = (item_weights > self.longtail_thresh).astype(int).mean()
        
        return float(round(avg_longtail_items, 4))

    def ACLT(self, recommended):
        item_weights = np.array([self.weights[x] for x in recommended])
        sum_longtail_items = (item_weights > self.longtail_thresh).astype(int).sum()
        
        return float(round(sum_longtail_items, 4))

# Class containing pyspark code
class recmet:
    def __init__(self, weights, longtail_thresh):
        
        self.weights = weights
        self.longtail_thresh = longtail_thresh
        # from PythonMetrics import Metrics
        met = Metrics(self.weights, self.longtail_thresh)

        # Pyspark AI
        self.AI = sf.udf(lambda x, y: met.AI(x, y), FloatType()) 
        
        # Pyspark PWAI
        self.PWAI = sf.udf(lambda x, y: met.PWAI(x, y), FloatType())

        # Pyspark ARP
        self.ARP = sf.udf(lambda x: met.ARP(x), FloatType())

        # Pyspark APLT
        self.APLT = sf.udf(lambda x: met.APLT(x), FloatType())

        # Pyspark ACLT
        self.ACLT = sf.udf(lambda x: met.ACLT(x), FloatType())

