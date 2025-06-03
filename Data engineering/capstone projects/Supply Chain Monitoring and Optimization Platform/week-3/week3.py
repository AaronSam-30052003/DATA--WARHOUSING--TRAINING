from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, datediff
def main():
# Initialize Spark session
    spark = SparkSession.builder \
        .appName("SupplyChainDelayAnalysis") \
        .getOrCreate()
# Load the CSV file (adjust path as needed)
    df = spark.read.csv("processed_supply_chain_report.csv", header=True, inferSchema=True)
# Convert dates to proper format
    df = df.withColumn("orderdate", col("orderdate").cast("date")) \
           .withColumn("deliverydate", col("deliverydate").cast("date"))
# Calculate delay in days
    df = df.withColumn("delay_days", datediff(col("deliverydate"), col("orderdate")))
# Create a new column to indicate delay status (1 = delayed, 0 = on-time)
    df = df.withColumn("is_delayed", when(col("delay_days") > 0, 1).otherwise(0))
# Filter delayed shipments
    delayed_df = df.filter(col("delay_days") > 0)
# Show some delayed shipment results
    print("Delayed Shipments:")
    delayed_df.select("orderid", "itemid", "orderdate", "deliverydate", "delay_days", "is_delayed").show(10)
# Group by supplierid and suppliername and count delayed orders
    delayed_count_df = delayed_df.groupBy("supplierid", "suppliername").count()
    print("Delayed orders count by supplier:")
    delayed_count_df.show()
# Save the processed data with delay info
    df.coalesce(1).write.csv("processed_supply_chain_report_with_delays", header=True, mode="overwrite")
# Save the aggregated delayed orders count
    delayed_count_df.coalesce(1).write.csv("delayed_orders_count_by_supplier", header=True, mode="overwrite")
# Stop Spark session
    spark.stop()
if __name__ == "__main__":
    main()
