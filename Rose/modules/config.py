from .vars import *
import motor.motor_asyncio

db_url = Config.MONGO_DATABASE

owner = Config.OWNER_ID

owner_username = Config.OWNER_USERNAME

connect = motor.motor_asyncio.AsyncIOMotorClient(db_url)

create = connect.Rose



users = create.users

messages = create.messages

bans = create.bans



async def get_message_id(message_id):

	message_id = await messages.find_one({'message_id_forward': f'{message_id}'})

	return message_id
