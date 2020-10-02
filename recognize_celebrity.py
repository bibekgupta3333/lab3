import csv
import boto3
import pprint
from datasecret import aws_access_key_id, aws_secret_access_key, aws_session_token

photo = 'skateboard_resized.jpg'
client = boto3.client('rekognition',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token, region_name='us-east-1')

with open(photo, 'rb') as source_image:
    source_bytes = source_image.read()


response = client.recognize_celebrities(
    Image={'Bytes': source_bytes})

pprint.pprint(response)
