# RecMet

RecMet is a library written in Pyspark and Python, containing different evaluation metrics for recommendation systems. The python functions wrapped in spark udf can be directly used with spark data frames.

## Installation

to install from the github repo 

```bash
git clone https://github.com/rijulizer/RecMet.git
cd RecMet
pip install .
```
or to use in databricks like environments use -  "git+'https://github.com/rijulizer/RecMet.git'"
## Usage

```python
from RecMet import recmet

# Instantiate recmet with the weights dictionary containing products as keys 
# and weights as values, and a threshold for the weights to be considered as long-tail

rm = recmet(weights, longtail_thresh)

sdf_rec_metric= sdf_rec.withColumn('AI',rm.AI(sf.col('Recommended'), sf.col('Test')))\
               .withColumn('PWAI',rm.PWAI(sf.col('Recommended'), sf.col('Test')))\
               .withColumn('ARP',rm.ARP(sf.col('Recommended')))\
               .withColumn('APLT',rm.APLT(sf.col('Recommended')))\
               .withColumn('ACLT',rm.ACLT(sf.col('Recommended')))
sdf_rec_metric.show()
```
## Average Intersection (AI)

```python
sdf_rec_metric = sdf_rec.withColumn('AI',rm.AI(sf.col('Recommended'), sf.col('Test')))
```

The Average Intersection (AI) is a generalized version of Average Recall (AR), which is used to measure the accuracy of recommendation. It indicates a measure of common elements between a recommendation set and a test set. In most real-life practical settings, the length of the test set for each user is not constant, and AI factors in that aspect, both the test set and the recommendation set can be of variable length.

## Popularity Weighted Average Intersection (PWAI)

```python
sdf_rec_metric = sdf_rec.withColumn('PWAI',rm.PWAI(sf.col('Recommended'), sf.col('Test')))
```

The Popularity Weighted Average Intersection (PWAI) is a special case of AI, where the weight of each product is considered to create the metric of accuracy. Often in practical scenarios, there are items that are very popular and there are items that are not so popular. And assigning different weights to them makes sense while calculating the accuracy. Weights (key- value pair) can be assigned by the user while instantiating the object.

## Average Rank of Products (ARP)

```python
sdf_rec_metric = sdf_rec.withColumn('PWAI',rm.PWAI(sf.col('Recommended'), sf.col('Test')))
```

The Popularity Weighted Average Intersection (PWAI) is a special case of AI, where the weight of each product is considered to create the metric of accuracy. Often in practical scenarios, there are items that are very popular and there are items that are not so popular. And assigning different weights to them makes sense while calculating the accuracy. Weights (key- value pair) can be assigned by the user while instantiating the object.

## Average percentage of long Tail Items (APLT)

```python
sdf_rec_metric = sdf_rec.withColumn('PWAI',rm.PWAI(sf.col('Recommended'), sf.col('Test')))
```

The Popularity Weighted Average Intersection (PWAI) is a special case of AI, where the weight of each product is considered to create the metric of accuracy. Often in practical scenarios, there are items that are very popular and there are items that are not so popular. And assigning different weights to them makes sense while calculating the accuracy. Weights (key- value pair) can be assigned by the user while instantiating the object.

## Average Count of long Tail Items (ACLT)

```python
sdf_rec_metric = sdf_rec.withColumn('PWAI',rm.PWAI(sf.col('Recommended'), sf.col('Test')))
```

The Popularity Weighted Average Intersection (PWAI) is a special case of AI, where the weight of each product is considered to create the metric of accuracy. Often in practical scenarios, there are items that are very popular and there are items that are not so popular. And assigning different weights to them makes sense while calculating the accuracy. Weights (key- value pair) can be assigned by the user while instantiating the object.

<p align="center">
<img src="images/name.png" alt="name" width=600>
</p>


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
