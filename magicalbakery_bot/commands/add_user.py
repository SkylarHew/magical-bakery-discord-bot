import datetime
import sqlite3
import os

import hikari
import lightbulb
from lightbulb import commands


@lightbulb.option("target", "The member to get add", hikari.Member)
@lightbulb.command("adduser", "Add user to database")
@lightbulb.implements(commands.SlashCommand)
async def add_user(ctx: lightbulb.context.Context) -> None:
    target_ = ctx.options.target
    # Convert the option into a Member object if lightbulb couldn't resolve it automatically
    target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
    )
    if not target:
        await ctx.respond("That user is not in the server.")
        return

    user_id = int(target.id)
    db = sqlite3.connect('magicalbakery_bot/data/main.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT user_id FROM user_data WHERE user_id = {user_id}")
    result = cursor.fetchone()
    if result:
        await ctx.respond(f"{target.display_name} has already been added.")
    else:
        money = 0
        last_checkin = str(datetime.datetime.now())
        cursor.execute('''INSERT INTO user_data(user_id, money, last_checkin)
                        VALUES(:user_id, :money, :last_checkin)''',
                        {'user_id':user_id, 'money':money, 'last_checkin':last_checkin})
        db.commit()
        await ctx.respond(f"Added {target.display_name} to database.")


def load(bot: lightbulb.BotApp):
    bot.command(add_user)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("adduser"))