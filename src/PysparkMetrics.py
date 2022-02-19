from PythonMetrics import Metrics
import pyspark.sql.functions as sf
from pyspark.sql.types import FloatType

class RecMet:
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
