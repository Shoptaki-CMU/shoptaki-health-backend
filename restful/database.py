from django.conf import settings
from arango import ArangoClient
from arango_orm import Database

client = ArangoClient(hosts=settings.ARANGO_DB['HOST'])
test_db = client.db(settings.ARANGO_DB['DATABASE'],
                    username=settings.ARANGO_DB['USERNAME'],
                    password=settings.ARANGO_DB['PASSWORD'])

db = Database(test_db)
