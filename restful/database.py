from django.conf import settings
from pyArango.connection import Connection
from arango_orm import Database

conn = Connection(
    arangoURL=f"http://{settings.ARANGO_DB['HOST']}:{settings.ARANGO_DB['PORT']}",
    username=settings.ARANGO_DB['USERNAME'],
    password=settings.ARANGO_DB['PASSWORD'],
)

db = Database(conn, settings.ARANGO_DB['DATABASE'])
