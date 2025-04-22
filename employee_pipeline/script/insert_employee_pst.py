from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder \
    .appName("Insert to Employee PST") \
    .enableHiveSupport() \
    .getOrCreate()

# Baca dari staging table
df = spark.read.table("development_iceberg.employee_stg")

# Tambahkan kolom tanggal, lalu append ke tabel Iceberg tujuan
df.withColumn("tanggal", current_date()) \
  .writeTo("development_iceberg.employee_pst") \
  .append()

spark.stop()