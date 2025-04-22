from pyspark.sql import SparkSession
from pyspark.sql.functions import lit
from datetime import datetime

# Ambil tanggal lokal hari ini dalam format 'YYYYMMDD'
today_str = datetime.now().strftime("%Y%m%d")

# Inisialisasi Spark session
spark = SparkSession.builder \
    .appName("Ingest people_staging to people with dynamic partition") \
    .enableHiveSupport() \
    .getOrCreate()

# Konfigurasi untuk partisi dinamis
spark.sql("SET hive.exec.dynamic.partition = true")
spark.sql("SET hive.exec.dynamic.partition.mode = nonstrict")

# Baca data dari staging
df = spark.table("development_test.people_staging")

# Tambahkan kolom partisi tanggal dengan value dari tanggal hari ini
df_with_partition = df.withColumn("tanggal", lit(today_str))

# Simpan ke tabel target dengan append dan partisi tanggal
df_with_partition.write \
    .mode("append") \
    .format("hive") \
    .partitionBy("tanggal") \
    .saveAsTable("development_test.people")

# Stop Spark session
spark.stop()
