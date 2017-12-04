""" FIELDS TO CHANGE:
    1. ACCESS_KEY_ID
    2. AWS_SECRET_ACCESS_KEY"""

import boto.ec2

def terminate_instances():
    """ Establish connection """
    conn = boto.ec2.connect_to_region('us-east-1',
                                        aws_access_key_id='ACCESS_KEY_ID',
                                        aws_secret_access_key='AWS_SECRET_ACCESS_KEY');

    reservations = conn.get_all_reservations(filters={'instance-state-name': 'running'});
    inst_ids = []

    """ Get all running instance ids """
    for reservation in reservations:
        for instance in reservation.instances:
            inst_ids.append(instance.instance_id)

    """ Terminate instances """
    conn.stop_instances(instance_ids=inst_ids)
    conn.terminate_instances(instance_ids=inst_ids)
