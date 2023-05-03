import boto3
import pandas as pd


def handler(event, context):
    bucket = event["bucket"]
    key = event["key"]
    filename = download(bucket, key)
    df = pd.read_csv(filename)
    columns = df.columns
    columns = [col.lower() for col in columns]
    return {"columns": columns}


def download(bucket, key):
    s3 = boto3.resource("s3")
    filename = f"/tmp/{key.split('/')[-1]}"
    s3.Bucket(bucket).download_file(key, filename)
    return filename
