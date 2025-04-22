from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Create Employee STG") \
    .enableHiveSupport() \
    .getOrCreate()

# Generate dummy data
data = [(i, f"Employee_{i}", "IT", 5000 + i) for i in range(1, 1001)]
df = spark.createDataFrame(data, ["id", "name", "department", "salary"])

# Write using Iceberg API (assume Spark configured with Iceberg catalog named 'hive')
df.writeTo("development_iceberg.employee_stg").createOrReplace()

spark.stop()