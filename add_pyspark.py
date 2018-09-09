import logging

import pytest
from pyspark.sql import SparkSession


def quiet_py4j():
    """Suppress spark logging for the test context."""
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)


@pytest.fixture(scope="session")
def spark_session():
    """Fixture for creating a spark context."""

    spark = (SparkSession
             .builder
             .master('local[*]')
             .appName('test')
             .enableHiveSupport()
             .getOrCreate())

    quiet_py4j()
    return spark


pytestmark = pytest.mark.usefixtures("spark_session")


def test_do_word_counts(spark_session):
    """ test word couting
    Args:
       spark_context: test fixture SparkContext
    """
    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]

    input_rdd = spark_session.sparkContext.parallelize([1, 2, 3])
    results = input_rdd.collect()

    expected_results = 3
    assert results == expected_results
