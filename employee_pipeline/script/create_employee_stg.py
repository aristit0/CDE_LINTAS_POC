from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Create Employee STG") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("""
    CREATE TABLE IF NOT EXISTS development_test.employee_stg (
        id INT,
        name STRING,
        department STRING,
        salary DOUBLE
    )
    STORED BY ICEBERG
""")

data = [(i, f"Employee_{i}", "IT", 5000 + i) for i in range(1, 1001)]
df = spark.createDataFrame(data, ["id", "name", "department", "salary"])
df.writeTo("development_test.employee_stg").overwrite()

spark.stop()