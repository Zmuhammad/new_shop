import boto3
import boto3.session
from django.conf import settings


class Bucket :
    """ CDN Bucket manager

    init method creates connection

    """
    def __init__(self):
        session = boto3.session.Session()
        self.conn = session.client(
            service_name = 's3',
            aws_access_key_id = 'fcce29d5-df47-4c54-8869-ea079d66875f',
            aws_secret_access_key = '1e69f5b5c400d28289a7ed4c42cf752dbf52f90db727c162ce3c2b869fdfac01',
            endpoint_url = 'https://s3.ir-thr-at1.arvanstorage.ir',

        )


    def get_objects (self):
        result = self.conn.list_objects_v2(Bucket = 'zmux')
        if result ['KeyCount']:
            return result['Contents']
        else:
            return None
        

    def delete_object (self , key):
        self.conn.delete_object(Bucket = 'zmux' , Key = key)
        return True
    
    

bucket = Bucket()

# AWS_ACCESS_KEY_ID = 'fcce29d5-df47-4c54-8869-ea079d66875f'
# AWS_SECRET_ACCESS_KEY = '1e69f5b5c400d28289a7ed4c42cf752dbf52f90db727c162ce3c2b869fdfac01'
# AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.ir'
# AWS_STORAGE_BUCKET_NAME = 'zmux'