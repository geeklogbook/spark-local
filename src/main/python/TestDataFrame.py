#OUTSIDE THE CONTAINER -> docker exec -it spark-master /opt/bitnami/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark-apps/testDataFrame.py
#INSIDE THE CONTAINER  -> spark-submit --master local /opt/spark-apps/testDataFrame.py
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.createDataFrame([
    (1, 144.5, 5.9, 33, 'M'),
    (2, 167.2, 5.4, 45, 'M'),
    (3, 124.1, 5.2, 23, 'F'),
    (4, 144.5, 5.9, 33, 'M'),
    (5, 133.2, 5.7, 54, 'F'),
    (3, 124.1, 5.2, 23, 'F'),
    (5, 129.2, 5.3, 42, 'M')], ['id', 'weight', 'height', 'age', 'gender'])

df = df.dropDuplicates()

df.show()