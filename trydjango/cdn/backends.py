from storages.backends.s3boto3 import S3Boto3Storage

<<<<<<< HEAD

class StaticRootS3Boto3Storage(S3Boto3Storage):
    location = 'static'


class MediaRootS3Boto3Storage(S3Boto3Storage):
    location = 'media'
=======
class StaticRootS3BotoStorage(S3Boto3Storage):
    location = "static"

class MediaRootS3BotoStorage(S3Boto3Storage):
    location = "media"
>>>>>>> 75-start
