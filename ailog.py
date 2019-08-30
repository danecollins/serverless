import json
import boto3
import uuid
import datetime



# define where the data will go
bucket = 'awr-auto-install'
folder = 'installs'


def log_install(event, context):
    s3 = boto3.resource('s3')

    param_list = event['queryStringParameters']

    if ('key' not in param_list) or (param_list['key'] != 'sj$sharks'):
        response = {
            'statusCode': 404
        }
        return response

    file_name = str(uuid.uuid4())
    path_name = folder + '/' + file_name + '.json'
    
    data = param_list
    data['logged_at'] = str(datetime.datetime.now())

    object = s3.Object(bucket, path_name)
    object.put(Body=json.dumps(data))
    response = {
        "statusCode": 200,
        "body": "Install data logged to: {}\n".format(path_name)
    }
    return response


def list_files(event, context):
    s3 = boto3.client('s3')
    bucket_content = s3.list_objects_v2(Bucket=bucket)
    object_ids = [
        file_path['Key'].lstrip(f'{folder}/')
        for file_path in bucket_content.get('Contents', [])
        if file_path['Size'] > 0
    ]
    response = {
        "statusCode": 200,
        "body": f'Files in folder are: {json.dumps(object_ids)}'
    }
    return response

