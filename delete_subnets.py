# import logging for get the logs in  execution
import logging
# import the boto3 which will use to interact  with the aws
import boto3
from botocore.exceptions import ClientError
import json

AWS_REGION = input("Please enter the AWS_REGION")

# this is the configration for the logger

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

vpc_client = boto3.client("ec2", region_name=AWS_REGION)


def del_subnet(subnet_id):
  
    try:
        response = vpc_client.del_subnet(SubnetId=subnet_id)

    except ClientError:
        logger.exception('Could not delete the subnet.')
        raise
    else:
        return response


if __name__ == '__main__':
    # SUBNET_ID = 'subnet-0d13cb95ea66f68e1'
    SUBNET_ID = input("Enter the subnet id")
    subnet = del_subnet(SUBNET_ID)
    logger.info(f'Your Subnet {SUBNET_ID} is deleted successfully.')