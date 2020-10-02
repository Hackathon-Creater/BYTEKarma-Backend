sid='DATABASE'
password = 'awsisawesome'
url='database-1.cuvbkbmjs5sa.us-east-1.rds.amazonaws.com'
port='1521'
instance_name='aws_db_instance'


def getConnectionString():
    return instance_name + '/' + password + '@' + url + ':' + port + '/' +sid