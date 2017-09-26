import re
import aiohttp
import asyncio
from contextlib import closing

from ga_export.settings import *

class Connect(object):



    def __init__(self, scenario):
        '''
        L'objet connect permet de se connecter au guichet adresse et d'interrragir avec ce dernier
        :param adresse: adresse à laquelle se connecter (chaine de caractère)
        :param credentials: login et mdp contenues dans un dictionnaire
        '''
        self.scenario = scenario
        self.test_url = re.compile('^http(s)?:\/\/.*\..*$')


    def action_repl(self, scenario):
        '''
        Permet de remplacer les actions text par les bonnes fonctions dans les scenario
        
        :return: 
        scenario
        '''

        for scenari in scenario:
            try:
                scenari.update({'action': getattr(self, scenari['action'])})
            except KeyError:
                raise('Vous devez décrire une action pour votre scenari')
        return scenario


    def test_url(self, url):
        if not self.test_url.match(url):
            raise('Votre url est malformée')

    async def request_verif(self, **kwargs):
        '''
        fonction qui vérifie la présence des arguments dans l'url
        
        :param kwargs: 
        :return: 
        '''
        try:
            kwargs['url']
        except KeyError:
            raise ('il manque la cle : url dans les kwargs')

    async def main_session(self, scenario):

        try:
            async with aiohttp.ClientSession(raise_for_status=True) as self.session:
                for scenari in scenario:
                    requete = scenari.pop('action')
                    return  await requete(**scenari)
        except (aiohttp.client_exceptions.ClientResponseError) as e:
            print('Connection au site web impossible --> {}'.format(e))


    async def get_request(self, url=None, **kwargs):
        '''
        
        :param url: page demandée
        :return: 
        '''
        async with self.session.get(url = url, **kwargs) as response:
            print(response.status)
            return await response.read()


    async def post_request(self, url=None, **kwargs):
        '''
        Génére une requête post via la session etablie
        
        :return: 
        web response, aoihttp object
        '''
        async with self.session.post(url=url, **kwargs) as response:
            print(response.status)
            return await response.read()

    async def do_scenari(self):
        '''
        Permet de jouer un ou plusieurs scenario d'envoi de requêtes
        :return: 
        '''
        self.scenario = self.action_repl(self.scenario)
        await self.main_session(self.scenario)


if __name__ == '__main__':

    with closing(asyncio.get_event_loop()) as loop:
        con = Connect(scenario= [{'action':'post_request','url':GUICHET_ADRESSE, 'data':CODES , 'parse':''}, {'action':'get_request','url':GUICHET_ADRESSE}])
        loop.run_until_complete(con.do_scenari())
