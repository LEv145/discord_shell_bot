from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BaseConfig():
    bot_config: BotConfig


@dataclass
class BotConfig():
    token: str
    prefix: str
    owner_ids: set
