import aiohttp
import asyncio
from contextlib import closing

from ga_export.scenari import scenari
from ga_export.settings import *

class Crawler():

    def __init__(self, scenario, loop):
        self.loop = loop
        self.scenario = scenario

    def do_scenari(self):
        '''
        Permet de jouer un ou plusieurs scenario d'envoi de requêtes
        :return: 
        '''
        self.main_session(self.scenario)

    def main_session(self, scenario):


                # for kwargs in self.scenario:
                    #print(kwargs)
                    # obj =
                    # run = await obj.run()
            # for kwargs in self.scenario:
            #     asyncio.ensure_future(scenari(**kwargs).run())
        tasks =  [ asyncio.ensure_future(scenari(**kwargs).run()) for kwargs in self.scenario ]

        # print(len(tasks))
        self.loop.run_until_complete(asyncio.wait(tasks))
        self.loop.close()



if __name__=="__main__":
    loop = asyncio.get_event_loop()
    a = {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
     'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                'resultat': {'text': '', 'attrs': ['value', ], }}]  , 'scenari':[]}
    robot = Crawler(scenario=[{'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES, 'parse':[{'selection':{'type':'input', 'name':'_csrf_token'},
                                                                                                            'resultat':{'text':'','attrs':['value',], }}]
                                                                                                  , 'scenari': a},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []},
                              {'action': 'get_request', 'url': GUICHET_ADRESSE, 'data': CODES,
                               'parse': [{'selection': {'type': 'input', 'name': '_csrf_token'},
                                          'resultat': {'text': '', 'attrs': ['value', ], }}]
                                  , 'scenari': []}]
                              , loop=loop )
    robot.do_scenari()
