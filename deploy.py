import boto3
import sys
import base64

def file_get_contents(filename):
    with open(filename, 'rb') as f:
        archive = f.read()
        return archive

args = sys.argv
layer_name=args[1]
upload_file = layer_name + '.zip'
print('Upload ' + layer_name + ' to lambda layer')
client = boto3.client('lambda')
response = client.publish_layer_version(
    LayerName=layer_name,
    Content={
        'ZipFile': file_get_contents(upload_file)
    },
    CompatibleRuntimes=['python3.6','python3.7']
)

print(response['LayerVersionArn'])
