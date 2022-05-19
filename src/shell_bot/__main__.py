from __future__ import annotations

import logging

import discord

from shell_bot.config import EnvironConfigLoader, AbstractConfig

from discord.ext import commands
from jishaku.help_command import DefaultPaginatorHelp


_logger = logging.getLogger(__name__)


def main() -> None:
    _logger.info("Started")

    loader: AbstractConfig = EnvironConfigLoader(prefix="SHELLBOT")
    config_data = loader.load()

    bot_config = config_data.bot_config

    bot = commands.Bot(
        command_prefix=bot_config.prefix,
        help_command=DefaultPaginatorHelp(),
        intents=discord.Intents.all(),
        owner_ids=bot_config.owner_ids,
    )

    bot.load_extension("jishaku")

    bot.run(bot_config.token)


if __name__ == "__main__":
    main()
