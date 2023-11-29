import boto3
import sys
import utils.vaultUtils
import utils.awsUtils
sys.path.append('E:\\Brainworks\\Snowflake\\GitHub\\github_file\\nvm-des-retail-analytic\\src\\utils')
from utils import VaultClient
from utils.awsUtil import AWSConnector


VAULT_URL = "http://127.0.0.1:8200"
ROLE_ID = "14f7d257-70d0-c61e-d1a6-552ea3955dcb"
SECRET_ID = "836f43ac-0165-73b1-106b-3519ef818a4f"
SECRET_PATH = "secret/data/aws"

vault_client = VaultClient(VAULT_URL, ROLE_ID, SECRET_ID, SECRET_PATH)
token = vault_client.authenticate_with_approle()

if token:
    secret_data = vault_client.get_secret(token)
    if secret_data:
        print("Secret data:", secret_data)
    else:
        print("Failed to retrieve secret.")
else:
    print("Failed to authenticate with AppRole.")


aws_access_key = secret_data['data']['accesskey']
aws_secret_key = secret_data['data']['secretkey']

region = 'us-east-1'  # Replace with your preferred AWS region


client='iam'
aws_connector = AWSConnector(aws_access_key, aws_secret_key, client, region)

# Access the S3 client through the instance
iam_client = aws_connector.aws_client_conn

# Now you can use s3_client to perform S3 operations
response = iam_client.list_groups()

print("IAM groups:", response)