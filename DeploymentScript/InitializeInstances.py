""" FIELDS FOR YOU TO CHANGE:
    1. ACCESS_KEY_ID
    2. AWS_SECRET_ACCESS_KEY
    3. KEY_NAME
    4. KEY_PAIR_SAVE_LOCATION
    5. SECURITY_GROUP_NAME """

import boto.ec2

def initialize_instances():
    """ Establish connection """
    conn = boto.ec2.connect_to_region('us-east-1',
                                        aws_access_key_id='ACCESS_KEY_ID',
                                        aws_secret_access_key='AWS_SECRET_ACCESS_KEY');

    """ Get and save key-pair"""
    keyPair = conn.create_key_pair(key_name='KEY_NAME');

    keyPair.save('KEY_PAIR_SAVE_LOCATION');

    """ Create Security group
        Authorize the required protocols and ports """
    securityGroup = conn.create_security_group(name='SECURITY_GROUP_NAME', description='Security group for Group 33 - CSC326');

    securityGroup.authorize(ip_protocol='icmp', from_port=-1, to_port=1, cidr_ip='0.0.0.0/0')
    securityGroup.authorize(ip_protocol='tcp', from_port=22, to_port=22, cidr_ip='0.0.0.0/0')
    securityGroup.authorize(ip_protocol='tcp', from_port=80, to_port=80, cidr_ip='0.0.0.0/0')

    """ Initialize and run instance """
    reservation = conn.run_instances(image_id='ami-8caa1ce4',
                                    min_count=1,
                                    max_count=1,
                                    key_name='KEY_NAME',
                                    security_group=['SECURITY_GROUP_NAME'],
                                    instance_type='t1.micro');
