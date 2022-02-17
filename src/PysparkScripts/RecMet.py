from metrics import Metrics
import pyspark.sql.functions as sf


met = Metrics(weights, longtail_thresh)
class RecMet:
    def __init__(self, weights, longtail_thresh):
        
        self.weights = weights
        self.longtail_thresh = longtail_thresh
        
        met = Metrics(self.weights, self.longtail_thresh)

        # Pyspark AI
        udf_AI = sf.udf(lambda x, y: met.AI(x, y), FloatType()) 
        # Pyspark PWAI
        udf_PWAI = sf.udf(lambda x, y: met.PWAI(x, y), FloatType())

        # Pyspark ARP
        udf_ARP = sf.udf(lambda x: met.ARP(x), FloatType())

        # Pyspark APLT
        udf_APLT = sf.udf(lambda x: met.APLT(x), FloatType())

        # Pyspark ACLT
        udf_ACLT = sf.udf(lambda x: met.ACLT(x), FloatType())

