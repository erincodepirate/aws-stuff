import boto3

dynamodb = boto3.client('dynamodb')

movies = [
    {'title':'Godzilla vs Yo Momma','year':1959},
    {'title':'Bambi becomes carnivorous','year':1976}
    ]

def load_movies(movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('Movies-erin2')
    for movie in movies:
        year = int(movie['year'])
        title = movie['title']
        print("adding movie:",title, year)
        table.put_item(Item=movie)
        
load_movies(movies)