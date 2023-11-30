from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int] | None


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    try:
        admins = list(map(int, env.list("ADMIN_IDS")))
    except:
        admins = None
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN"), admin_ids=admins))
