from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder \
    .appName("Insert to Employee PST") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("""
    CREATE TABLE IF NOT EXISTS development_test.employee_pst (
        id INT,
        name STRING,
        department STRING,
        salary DOUBLE,
        tanggal DATE
    )
    PARTITIONED BY (tanggal)
    STORED BY ICEBERG
""")

df = spark.read.table("development_test.employee_stg")
df.withColumn("tanggal", current_date()) \
  .writeTo("development_test.employee_pst").append()

spark.stop()