from app.services.bucket.s3 import S3Service
from app.services.bucket.baseBucketService import BaseBucketService

bucket_service = S3Service()
assert isinstance(bucket_service, BaseBucketService), "selected service is not an instance of BaseBucketService"