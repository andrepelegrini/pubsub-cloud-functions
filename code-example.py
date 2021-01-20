import json
from datetime import datetime
from datetime import timezone
import os
import pandas as pd
from flatten_json import flatten
import gcsfs
from google.cloud import storage
import base64
import pytz

def load_raw(message_raw):

    tz = pytz.timezone('America/Sao_Paulo')
    now = datetime.now()
    aware = tz.localize(now, is_dst=None)

    bucket_name = 'bucket_name'
    dt_processamento = aware.strftime("%Y-%m-%d")
    table_path = 'test/test/profile/' + dt_processamento + '/'
    filename = 'profile-' + aware.strftime("%Y-%m-%d_%H:%M:%S") + '.txt'

    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(table_path+filename)
    blob.upload_from_string(message_raw)


def load_trusted(message):

    # Normalize json and rename columns
    data = flatten(message)
    df = pd.DataFrame(data, index=[0])

    df_result = df.rename(columns={'content_column_1': 'column_1',
                                   'content_column_2': 'column_2',
                                   'content_column_3': 'column_3'
                                   })

    # Load data to a trusted folder
    tz = pytz.timezone('America/Sao_Paulo')
    now = datetime.now()
    aware = tz.localize(now, is_dst=None)

    client = storage.Client()
    bucket = client.get_bucket('bexs_trusted_data')

    dt_processamento = 'dt=' + aware.strftime("%Y-%m-%d")
    partition_dir = 'test/test/profile/' + dt_processamento + '/'

    file_name = 'profile-' + aware.strftime("%Y-%m-%d_%H:%M:%S") + '.parquet'

    gcs = gcsfs.GCSFileSystem(project='example_staging', token=None)

    df_result.to_parquet('gs://bucket_name/' + partition_dir + file_name, compression='SNAPPY')

def load_data(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    message_raw = base64.b64decode(json.dumps(event['data']))
    message = json.loads(base64.b64decode(json.dumps(event['data'])))

    return load_raw(message_raw), load_trusted(message)
