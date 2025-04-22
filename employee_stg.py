from pyspark.sql import SparkSession
from datetime import datetime

spark = SparkSession.builder \
    .appName("Create Employee STG") \
    .enableHiveSupport() \
    .getOrCreate()

# Buat table jika belum ada
spark.sql("""
    CREATE TABLE IF NOT EXISTS development_test.employee_stg (
        id INT,
        name STRING,
        department STRING,
        salary DOUBLE
    )
    STORED BY ICEBERG
""")

# Generate data dummy
data = [(i, f"Employee_{i}", "IT", 5000 + i) for i in range(1, 1001)]
df = spark.createDataFrame(data, ["id", "name", "department", "salary"])

# Overwrite ke table
df.writeTo("development_test.employee_stg").overwrite()

spark.stop()
