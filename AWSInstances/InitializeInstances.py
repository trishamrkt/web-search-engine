""" security group name: csc326-group33 """

import boto.ec2

""" Establish connection """
conn = boto.ec2.connect_to_region('us-east-1',
                                    aws_access_key_id='ACCESS_KEY_ID',
                                    aws_secret_access_key='AWS_SECRET_ACCESS_KEY');

""" Get and save key-pair"""
keyPair = conn.create_key_pair(key_name='pandjkey');

keyPair.save('C:\csc326-aws');

""" Create Security group
    Authorize the required protocols and ports """
securityGroup = conn.create_security_group(name='csc326-group33', description='Security group for Group 33 - CSC326');

securityGroup.authorize(ip_protocol='icmp', from_port=-1, to_port=1, cidr_ip='0.0.0.0/0')
securityGroup.authorize(ip_protocol='tcp', from_port=22, to_port=22, cidr_ip='0.0.0.0/0')
securityGroup.authorize(ip_protocol='tcp', from_port=80, to_port=80, cidr_ip='0.0.0.0/0')

""" Initialize and run instance """
reservation = conn.run_instances(image_id='ami-8caa1ce4',
                                min_count=1,
                                max_count=1,
                                key_name='pandjkey',
                                security_group=['csc326-group33'],
                                instance_type='t1.micro');
