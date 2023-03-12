"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

BucketNames = ["bucket1", "bucket2", "bucket3"]
BucketList = []

# Create an AWS resource (S3 Bucket)
def Createbucket():

    for i in range (0, len(BucketNames)):
        bucket = s3.Bucket(BucketNames[i])
        BucketList.append(bucket.id)

    # Export the name of the bucket
    pulumi.export('bucket_names', BucketList)        

Createbucket()




