import boto3
import sys


def file_get_contents(filename):
    with open(filename, 'rb') as f:
        archive = f.read()
        return archive


args = sys.argv
layer_name = args[1]
upload_file = layer_name + '.zip'
print('Upload ' + layer_name + ' to lambda layer')
client = boto3.client('lambda')
response = client.publish_layer_version(
    LayerName=layer_name,
    Content={
        'ZipFile': file_get_contents(upload_file)
    },
    CompatibleRuntimes=['python3.6', 'python3.7']
)

layer_arn = response['LayerArn']
layer_version_arn = response['LayerVersionArn']
layer_version = response['Version']
statement_id = layer_name + '_' + layer_version

response = client.add_layer_version_permission(
    LayerName=layer_arn,
    VersionNumber=layer_version,
    StatementId=statement_id,
    Action='lambda:GetLayerVersion',
    Principal='*'
)

layer_permission_statement = response['Statement']

print('LayerArn = ' + layer_arn)
print('LayerVersion = ' + layer_version)
print('LayerVersionArn = ' + layer_version_arn)
