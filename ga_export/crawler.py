import aiohttp
import asyncio
from contextlib import closing

from ga_export.scenari import scenari
from ga_export.settings import *

class Crawler():

    def __init__(self, scenario):
        self.scenario = scenario

    async def do_scenari(self):
        '''
        Permet de jouer un ou plusieurs scenario d'envoi de requêtes
        :return: 
        '''
        await self.main_session(self.scenario)

    async def main_session(self, scenario):

        try:
            async with aiohttp.ClientSession(raise_for_status=True) as self.session:
                for kwargs in self.scenario:
                    obj = scenari(self.session, **kwargs)
                    return await obj.run()
        except (aiohttp.client_exceptions.ClientResponseError) as e:
            print('Connection au site web impossible --> {}'.format(e))


if __name__=="__main__":
    with closing(asyncio.get_event_loop()) as loop:
        robot = Crawler(scenario=[{'action': 'post_request', 'url': GUICHET_ADRESSE, 'data': CODES, 'parse':[], 'scenari':[]}])
        loop.run_until_complete(robot.do_scenari())