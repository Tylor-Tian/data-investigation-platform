import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from app.services.spark import query_hive, SparkSession
from app.services.flink import process_stream, StreamExecutionEnvironment


def test_spark_unavailable():
    if SparkSession is None:
        with pytest.raises(RuntimeError):
            list(query_hive("SELECT 1"))


def test_flink_unavailable():
    if StreamExecutionEnvironment is None:
        with pytest.raises(RuntimeError):
            process_stream("topic")
