from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
import time

start=time.time()
# Create a SparkSession
spark = SparkSession.builder \
    .appName("HIGGS_LogisticRegression") \
    .master("local[120]") \
    .config("spark.driver.memory", "60g") \
    .getOrCreate()

# === Log Spark executor environment ===
sc = spark.sparkContext
sc = spark.sparkContext
print("=== Spark Runtime Info ===")
print(f"Master: {sc.master}")
print(f"App Name: {sc.appName}")
print(f"Default Parallelism (Cores): {sc.defaultParallelism}")
print(f"Executor Memory: {sc._conf.get('spark.executor.memory')}")
print(f"Driver Memory: {sc._conf.get('spark.driver.memory')}")
print(f"Executor Cores: {sc._conf.get('spark.executor.cores')}")
print("===========================")

# Load the dataset (no header; delimiter is comma)
data = spark.read.csv("HIGGS.csv", inferSchema=True, header=False)

# Assume the CSV has 29 columns: _c0 (label) and _c1 ... _c28 (features)
columns = ["label"] + [f"f{i}" for i in range(1, 29)]
data = data.toDF(*columns)

# Ensure the label is of type double
data = data.withColumn("label", col("label").cast("double"))

# Assemble features into a single vector column
assembler = VectorAssembler(inputCols=[f"f{i}" for i in range(1, 29)], outputCol="features")
data = assembler.transform(data)

# Split the dataset into training and test sets
train, test = data.randomSplit([0.8, 0.2], seed=42)

# Initialize and train the Logistic Regression model
lr = LogisticRegression(featuresCol="features", labelCol="label", maxIter=10)
model = lr.fit(train)

# Make predictions on the test set
predictions = model.transform(test)

# Evaluate the model using AUC
evaluator = BinaryClassificationEvaluator(labelCol="label", rawPredictionCol="rawPrediction", metricName="areaUnderROC")
auc = evaluator.evaluate(predictions)
print(f"---------------Test AUC: {auc}---------------------------------------")

end=time.time()
print(f"Total runtime: {(end - start)/60:.2f} minutes")


# Stop the SparkSession
spark.stop()