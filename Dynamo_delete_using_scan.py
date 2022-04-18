from http import client
import boto3
from boto3.dynamodb.conditions import Key

client = boto3.client('dynamodb')
table = boto3.resource('dynamodb').Table({table_name})
scan = table.scan( FilterExpression=Key({column_name}).eq({value_need_to_be_compare}))
response_output=[]
response_output+= scan['Items']
while 'LastEvaluatedKey' in scan:
    scan = table.scan( FilterExpression=Key('clientid').eq(clientid),ExclusiveStartKey=scan['LastEvaluatedKey'])
    response_output+= scan['Items']
pk_response = []
sk_response = []
data={'Key':[]}
for item in response_output:
    respond_data ={'PK':item["PK"],'SK':item["SK"]}
    pk_response.append(item['PK'])
    sk_response.append(item['SK'])
    data['Key'].append(respond_data) #creating a dictionary

with table.batch_writer() as batch:
    for i in range(0, len(pk_response)):
        batch.delete_item(Key={"PK": pk_response[i],
                               "SK": sk_response[i]
                               })
