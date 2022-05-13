import boto3
import datetime
from botocore.vendored import requests
import os

#OBJECT_NAME_FORMAT = os.environ['OBJECT_NAME_FORMAT']
S3_BUCKET_NAME = os.environ['S3_BUCKET']
DOWNLOAD_URL = os.environ['DOWNLOAD_URL']

s3_bucket = boto3.resource('s3').Bucket(S3_BUCKET_NAME)


def lambda_handler(event, context):
    #object_name = (datetime.datetime.utcnow()).strftime(OBJECT_NAME_FORMAT)
    FILE_NAME=datetime.datetime.utcnow().strftime('%Y%m%d_%H:%M:%S')
    n = 6
    
    # initialize sum and counter
    suma = 0
    i = 1
    
    while i <= n:
        suma ="lhr_desktop_url"+str(i)+".csv"
        data = requests.get(DOWNLOAD_URL+suma, timeout=30).content
        folder_name="desktop"
        file_csv="lhr_desktop_url"+str(i)+FILE_NAME+".csv"
        s3_bucket.put_object(Key=folder_name+'/'+file_csv, Body=data)
        print("Stored object %s" % file_csv)
        i = i+1    # update counter
        
    m = 6
    
    # initialize sum and counter
    suma2 = 0
    j = 1
    
    while j <= m:
        suma2 ="lhr_mobile_url"+str(j)+".json"
        data = requests.get(DOWNLOAD_URL+suma2, timeout=30).content
        folder_name2="mobile"
        file_csv2="lhr_desktop_url"+str(i)+FILE_NAME+".csv"
        s3_bucket.put_object(Key=folder_name2+'/'+file_csv2, Body=data)
        print("Stored object %s" % file_csv2)
        j = j+1    # update counter
    
    #data = requests.get(DOWNLOAD_URL+, timeout=30).content
    #s3_bucket.put_object(Key=object_name, Body=data)
    #print("Stored object %s" % object_name)