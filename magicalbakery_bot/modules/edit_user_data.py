import sqlite3
import datetime
import hikari
import lightbulb

def add_user(user: hikari.Member) -> str:
    user_id = int(user.id)
    db = sqlite3.connect('magicalbakery_bot/data/main.db')
    cursor = db.cursor()
    # Check if user already added
    cursor.execute(f"SELECT user_id FROM user_data WHERE user_id = {user_id}")
    result = cursor.fetchone()
    if result:
        return f"{user.display_name} has already been added."
    else:
        # Add new user
        money = 0
        last_checkin = str(datetime.datetime.now())
        cursor.execute('''INSERT INTO user_data(user_id, money, last_checkin)
                        VALUES(:user_id, :money, :last_checkin)''',
                        {'user_id':user_id, 'money':money, 'last_checkin':last_checkin})
        db.commit()
        return f"Added {user.display_name} to database."


# def delete_user(user: hikari.Member) -> str:
#     user_id = int(user.id)
#     db = sqlite3.connect('magicalbakery_bot/data/main.db')
#     cursor = db.cursor()
#     # Check if user is in database
#     cursor.execute(f"SELECT user_id FROM user_data WHERE user_id = {user_id}")
#     result = cursor.fetchone()
#     if result:
#         # Delete user
#         return f"{user.display_name} has been removed from database."
#     else:
#         # Add new user
#         return f"{user.display_name} not in database."

