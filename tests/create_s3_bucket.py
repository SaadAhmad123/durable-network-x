import os
from dotenv import load_dotenv
import boto3
from botocore.exceptions import ClientError

load_dotenv()

AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_REGION = os.environ.get("AWS_REGION")

class S3Bucket:
    def __init__(
        self,
        bucket_name: str,
        access_key: str = AWS_ACCESS_KEY,
        secret_key: str = AWS_SECRET_KEY,
        region: str = AWS_REGION,
    ):
        self.__bucket_name = bucket_name
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__region = region
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.__access_key,
            aws_secret_access_key=self.__secret_key,
            region_name=self.__region
        )

    def __enter__(self):
        try:
            self.s3_client.create_bucket(
                Bucket=self.__bucket_name,
                CreateBucketConfiguration={'LocationConstraint': self.__region}
            )
        except ClientError as e:
            if e.response['Error']['Code'] not in ('BucketAlreadyOwnedByYou', 'BucketAlreadyExists'):
                print(f"Error creating bucket: {e}")
                return None
            else:
                print(f"Bucket {self.__bucket_name} already exists. Using it.")
        return self


    def __exit__(self, exc_type, exc_value, traceback):
        try:
            for key in self.s3_client.list_objects(Bucket=self.__bucket_name).get("Contents", list()):
                self.s3_client.delete_object(Bucket=self.__bucket_name, Key=key["Key"])
            self.s3_client.delete_bucket(Bucket=self.__bucket_name)
        except ClientError as e:
            print(f"Error deleting bucket: {e}")

    @property
    def bucket_name(self):
        return self.__bucket_name
