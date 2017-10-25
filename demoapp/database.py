"""
database.py
~~~~~~~~~~~
MongoDB related functions
"""
import logging
from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId


async def setup_db(app):
    """Initialises the database

    :param recreate_db: Recreate all objects BE CAREFUL, will remove database!
    """
    host = '10.253.1.4'
    port = 27017

    logging.debug('Initialising asyncio mongodb (motor) handler')
    db = AsyncIOMotorClient('mongodb://{}:{}/'.format(host, port)).demoapp
    app['db'] = db

    await create_some_dummy_data(db)


async def create_some_dummy_data(db):

    mathijs = {
            "name": "Mathijs",
            "occupation": "hobbyist",
            "skillset": "avoiding RFCs"
    }
    martijn = {
            "name": "Martijn",
            "occupation": "Beer drinker",
            "skillset": "Annoying Mathijs"
    }

    result = await db.demoapp.insert_one(mathijs)
    print('Result adding mathijs {}'.format(result.inserted_id))
    result = await db.demoapp.insert_one(martijn)
    print('Result adding martijn {}'.format(result.inserted_id))

    n = await db.demoapp.find().count()
    print('Total of {} records'.format(n))


async def list_users(db):
    """Retrieves all users from mongoDB instance"""
    n = await db.demoapp.find().count()
    print('Total of {} records'.format(n))

    cursor = db.demoapp.find()
    users = []
    print(cursor)
    for document in await cursor.to_list(length=None):
        print('huh {}'.format(document))
        users.append(document)

    return users
