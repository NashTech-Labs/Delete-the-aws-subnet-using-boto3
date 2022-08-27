# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

REGION = input("Please enter the AWS REGION")

# this is the configration for the logger_for

logger_for = logging.getlogger_for()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

response = boto3.client("ec2", region_name=REGION)


def del_subnet(subnet_id):
  
    try:
        res = response.del_subnet(SubnetId=subnet_id)

    except ClientError:
        logger_for.exception('Oops sorry, Your subnet can not be deleted.')
        raise
    else:
        return res


if __name__ == '__main__':
    ID = input("Enter the subnet id")
    subnet = del_subnet(ID)
    logger_for.info(f'Your Subnet {ID} is deleted successfully.')