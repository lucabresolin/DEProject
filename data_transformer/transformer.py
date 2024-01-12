from pyspark.sql import SparkSession
import pyspark.sql.functions as F
from pyspark.sql.window import Window


def main():
    spark = SparkSession.builder.appName("DataTransformer").getOrCreate()
    df = spark.read.csv("../extractor_consumer/data/raw/*", header=True)
    df.show(5)

    ag_df = df.groupby("date", "id_capteur").agg(F.sum(F.col("visitors")).alias("visitors"),
                                                 F.first(F.col("unite")).alias("unite"),
                                                 F.first(F.col("id_magasin")).alias("id_magasin"))
    ag_df.show(5)

    print(f"""nombre de lignes sans compte de visiteurs :  {ag_df.where(F.col("visitors").isNull()).count()}""")
    ag_df = ag_df.drop("id_magasin")  # drops na col
    ag_df.count()

    win_df = ((
        ag_df
        .withColumn("day_of_week", F.dayofweek("date"))
        .withColumn("moyenne_roulante",
                    F.mean("visitors").over(Window.partitionBy("day_of_week", "id_capteur").orderBy("date").rowsBetween(-4, -1)))
        .drop("day_of_week")
        .orderBy("date")
    ))
    win_df.show(5)

    pct_df = ((
        win_df
        .withColumn("pct_change",
                    F.round((100 * (F.col("visitors") - F.col("moyenne_roulante")) / (F.col("moyenne_roulante"))), 2))
    ))
    pct_df.show()

    pct_df.write.mode("overwrite").parquet("../streamlit_app/data/processed")


if __name__ == "__main__":
    main()
