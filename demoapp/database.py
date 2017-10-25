"""
database.py
~~~~~~~~~~~
MongoDB related functions
"""
import logging
from motor.motor_asyncio import AsyncIOMotorClient
# from bson import ObjectId


async def setup_db(app, host='127.0.0.1', port=27017, recreate_db=True):
    """Initialises the database

    :param recreate_db: Recreate all objects BE CAREFUL, will remove database!
    """
    logging.debug('Initialising asyncio mongodb (motor) handler')
    db = AsyncIOMotorClient('mongodb://{}:{}/'.format(host, port)).demoapp
    app['db'] = db

    if recreate_db:
        await create_some_dummy_data(db.db)


async def create_some_dummy_data(db):

    payload = [
        {
            "name": "Mathijs",
            "occupation": "Hobbyist",
            "Key Competences": "Talking a lot"
        },
        {
            "name": "Martijn",
            "occupation": "Beer drinker",
            "competences": "Annoying Mathijs"
        }
    ]

    result = await db.demoapp.save(payload)
    return result


async def list_users(db):
    """Retrieves all users from mongoDB instance"""
    cursor = self.db.demoapp.find({})
    users = []
    for document in await cursor.to_list(length=None):
        users.append(document)

    return users
