import datetime
import magicalbakery_bot.modules.edit_user_data as edit_user_data
import sqlite3

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

    await ctx.respond(edit_user_data.add_user(target))


def load(bot: lightbulb.BotApp):
    bot.command(add_user)


def unload(bot: lightbulb.BotApp):
    bot.remove_command(bot.get_slash_command("adduser"))