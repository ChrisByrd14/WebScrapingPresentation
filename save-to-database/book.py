#!/usr/bin/env python3
"""Book model for database interaction.
"""

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


db = SqliteExtDatabase('books.db')

class Book(Model):
    class Meta:
        database = db
    id = IntegerField(primary_key=True)
    name = CharField(null=False)
    url = CharField(null=True)
    upc = CharField(null=True)
    price = DoubleField(default=0.00)
    in_stock = IntegerField(default=0)
    created_on = DateTimeField(constraints=[SQL("DEFAULT (datetime('now'))")])


if __name__ == '__main__':
    with db:
        db.create_tables([Book])

