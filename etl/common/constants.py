"""
All constants
"""

from enum import Enum

class S3FileTypes(Enum):
    """
    Supported file types for s3BucketConnector
    """

    CSV = 'csv'
    PARQUET = 'parquet'


class MetaProcessFormat(Enum):
    """
    Formation for MetaProcess class 
    """

    META_DATE_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:-%M:-%s'
    META_SOURCE_DATE_C = 'source_date'
    META_PROCESS_C = 'datetime_of_processing'
    META_FILE_FORMAT = 'csv'