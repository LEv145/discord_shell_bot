import os
import abc

from .model import BaseConfig, BotConfig


class AbstractConfig(abc.ABC):
    def load(self) -> BaseConfig:
        raise NotImplementedError


class EnvironConfigLoader(AbstractConfig):
    def __init__(self, prefix: str) -> None:
        self._prefix = prefix

    def load(self) -> BaseConfig:
        try:
            bot_config = BotConfig(
                token=os.environ[f"{self._prefix}_TOKEN"],
                prefix=os.environ[f"{self._prefix}_PREFIX"],
                owner_ids=os.environ.get(f"{self._prefix}_OWNER_IDS", set()),
            )
        except KeyError as exception:
            raise InvalidConfig() from exception

        return BaseConfig(bot_config=bot_config)


class InvalidConfig(Exception):
    pass
