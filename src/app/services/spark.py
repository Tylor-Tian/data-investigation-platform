from typing import Iterable

try:
    from pyspark.sql import SparkSession
except Exception:  # pragma: no cover - pyspark not installed in tests
    SparkSession = None


def query_hive(sql: str) -> Iterable[dict]:
    """Execute a Hive query using Spark and yield rows as dictionaries."""
    if SparkSession is None:
        raise RuntimeError("pyspark is not available")
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()
    df = spark.sql(sql)
    for row in df.collect():
        yield row.asDict()
