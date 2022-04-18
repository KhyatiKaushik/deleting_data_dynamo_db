import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = boto3.resource('dynamodb').Table('bulk-load')

response = table.query(
    IndexName='{column_name}-index',
    KeyConditionExpression=Key({column_name}).eq({value_you_want_to_compare})
)
 with table.batch_writer() as batch:
     for item in scan['Items']:
         print('------------------')
         print(item)
         batch.delete_item(Key={"PK": item["PK"],
                                "SK": item["SK"]
                                })
