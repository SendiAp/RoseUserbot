from .import pmdb

async def set_pm(user_id: int, value: bool):
    doc = {"user_id": user_id, "pmpermit": value}
    doc2 = {"user_id": "Approved", "users": []}
    r = await pmdb.find_one({"user_id": user_id})
    r2 = await pmdb.find_one({"user_id": "Approved"})
    if r:
        await pmdb.update_one({"user_id": user_id}, {"$set": {"pmpermit": value}})
    else:
        await pmdb.insert_one(doc)
    if not r2:
        await pmdb.insert_one(doc2)
