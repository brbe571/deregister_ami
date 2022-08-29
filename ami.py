import time
import datetime
import os
import json
import boto3
from botocore.exceptions import ClientError

expired_date = (datetime.datetime.now() - datetime.timedelta(days=years*365)).strftime('%Y-%m-%d')
print(expired_date)

cnt=1
def ami_from_ami_list():
    ec2 = boto3.client('ec2')
    amis = ec2.describe_images(Owners=['self'])
    print(amis)
    for ami in amis['Images']:
        creation_date = ami['CreationDate']
        ami_id = ami['ImageId']
        print(cnt, creation_date, ami_id)
        if creation_date < expired_date:
            print "deleting -> " + ami_id + " - create_date = " + create_date
            # deregister the AMI
            ec2.deregister_image(ImageId=ami_id)