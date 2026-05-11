import boto3

def get_connection(service):
    return boto3.client(service)

def show_buckets(s3_client):
    response = s3_client.list_buckets()

def create_bucket(s3_client, bucket_name):
    response = s3_client.create_bucket(Bucket=bucket_name, 
    CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})  

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print(f"Bucket {bucket_name} created successfully.")
    else:
            print(f"Failed to create bucket {bucket_name}.")


def upload_to_bucket(s3_client, bucket_name, file_name):
      s3_client.upload_file(file_name, bucket_name, file_name)
      print(f"File {file_name} uploaded to bucket {bucket_name} successfully.")

s3_client = get_connection('s3')
show_buckets(s3_client)

create_bucket(s3_client, 'hemant-ki-new-bucket')

upload_to_bucket(s3_client,'hemant-ki-new-bucket','file.txt')