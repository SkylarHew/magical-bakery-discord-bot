import os

import hikari
import lightbulb

import magicalbakery_bot


def create_bot() -> lightbulb.BotApp:
    # Load the token from a secrets file you'll need to create yourself.
    with open("./secrets/TOKEN") as f:
        token = f.read().strip()

    # Create the main bot instance with all intents.
    bot = lightbulb.BotApp(
        token=token,
        prefix="!",
        intents=hikari.Intents.ALL,
        default_enabled_guilds=magicalbakery_bot.GUILD_ID,
    )

    # Load all extensions.
    bot.load_extensions_from("./magicalbakery_bot/commands")

    return bot


if __name__ == "__main__":
    if os.name != "nt":
        # uvloop is only available on UNIX systems, but instead of
        # coding for the OS, we include this if statement to make life
        # easier.
        import uvloop

        uvloop.install()

    # Create and run the bot.
    create_bot().run()