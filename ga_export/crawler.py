import aiohttp
import asyncio
from contextlib import closing

from ga_export.scenari import scenari, Counter
from ga_export.settings import *



class Crawler():

    def __init__(self, scenario, loop):
        self.loop = loop
        self.scenario = scenario

    def do_scenari(self):

        [asyncio.ensure_future(scenari(loop=self.loop, **kwargs).run()) for kwargs in self.scenario]

        try:
            self.loop.run_forever()
        except:
            self.loop.close()
                # self.loop.run_until_complete(asyncio.gather(*tasks))


if __name__=="__main__":
    loop = asyncio.get_event_loop()
    a = {'action': 'get', 'url': GUICHET_ADRESSE, 'data': CODES,
     'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                'resultat': {'text': '', 'attrs': ['value', ], }}]  , 'scenari':[]}
    # print(loop)
    robot = Crawler(scenario=[{'action': 'get', 'url': GUICHET_ADRESSE, 'data': CODES, 'parse':[{'selection':{'type':'input', 'name':'_csrf_token'},
                                                                                                            'resultat':{'text':'','attrs':['value',], }}]
                                                                                                  , 'scenari': a} for i in range(0,10)

                            ]
                            , loop=loop )
    # print(loop)
    robot.do_scenari()
