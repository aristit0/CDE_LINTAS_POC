from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder \
    .appName("Insert to Employee PST") \
    .enableHiveSupport() \
    .getOrCreate()

spark.sql("""
zyy
""")

df = spark.read.table("development_iceberg.employee_stg")
df.withColumn("tanggal", current_date()) \
  .writeTo("development_test.employee_pst").append()

spark.stop()