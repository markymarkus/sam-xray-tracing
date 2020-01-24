import boto3
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

patch(['boto3'])

s3_client = boto3.client('s3')
bucket_name = os.environ['Bucket']
file_name = os.environ['File']

def lambda_handler(event, context):
    logger.info('os environment vars:')  
    logger.info(os.environ)
# This works:
    get_object_from_s3(bucket_name, file_name)
# This fails:
    get_object_from_s3("and_thissturelyeerefails", file_name)    


@xray_recorder.capture('get_object')
def get_object_from_s3(bucket_name, bucket_key):
    response = s3_client.get_object(Bucket=bucket_name, Key=bucket_key)
    status_code = response['ResponseMetadata']['HTTPStatusCode']
    xray_recorder.current_subsegment().put_annotation('get_response', status_code)