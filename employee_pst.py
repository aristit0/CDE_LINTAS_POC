from pyspark.sql import SparkSession
from pyspark.sql.functions import current_date

spark = SparkSession.builder \
    .appName("Insert to Employee PST") \
    .enableHiveSupport() \
    .getOrCreate()

# Buat table partitioned
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

# Baca dari staging table
df_stg = spark.read.table("development_test.employee_stg")
df_pst = df_stg.withColumn("tanggal", current_date())

# Insert into partitioned table
df_pst.writeTo("development_test.employee_pst").append()

spark.stop()
