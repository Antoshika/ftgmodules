#   Coded by D4n1l3k300    #
#     t.me/D4n13l3k00      #
# This code under AGPL-3.0 #

from requests.api import request
from .. import loader, utils
from requests import get


@loader.tds
class FullApiMod(loader.Module):
    """Фулл"""
    strings = {'name': 'FullApi'}

    @loader.owner
    async def rndfullcmd(self, m):
        """.rndfull - получить рандомный фулл :)
        """
        await m.edit("<a href=\""+get("https://api.d4n13l3k00.ru/random_full").json()['url']+"\">Подгончик для братков</a>")
