from peewee import *

db = PostgresqlDatabase(
    'countries',
    host = 'localhost',
    port = '5432',
    user = 'superman',
    password = '123'
)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db
        
class Countries2(BaseModel):
    name =  CharField(max_length=255, null = False)
    official_name =  CharField(max_length=255, null = False)
    capital = CharField(max_length=255, null = False)
    region =  CharField(max_length=255, null = False)
    subregion = CharField(max_length=255, null = False)
    population = IntegerField(null = False)
    continents = CharField(max_length=255, null = False)
    timezones = CharField(max_length=255, null = False)
    


db.create_tables([Countries2]) 