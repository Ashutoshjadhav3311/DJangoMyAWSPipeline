import boto3
import json
import base64
from botocore.exceptions import ClientError
 
def getdjangokey():
 
# AWS Secrets Manager to use AWS credentials & Django secret Key stored there
    secret_name = "sonarcloudDjangoSecreat"  
    region_name="us-west-2"
 
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
 
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # Handle the exception based on the error code
        raise e
    else:
        # Decrypts secret using the associated KMS CMK
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            djangosecret_dict = json.loads(secret)
#            print("Retrieved secret:", secret_dict)  # Testing line
            return djangosecret_dict
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return json.loads(decoded_binary_secret)    
 
