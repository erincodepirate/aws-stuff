import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Movies-erin2')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'year':1990,
            'title':'Some Pig'
        }    
    )
    batch.put_item(
        Item={
            'year':1923,
            'title':'Blaahhhh'
        }
    )