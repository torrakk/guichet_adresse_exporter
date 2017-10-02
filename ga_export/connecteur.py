import re
import aiohttp
import asyncio
from contextlib import closing

from ga_export.settings import *

class Connect(object):


    def __init__(self, session, scenari):
        '''
        L'objet connect permet de se connecter au guichet adresse et d'interrragir avec ce dernier
        :param adresse: adresse à laquelle se connecter (chaine de caractère)
        :param credentials: login et mdp contenues dans un dictionnaire
        '''
        self.session = session
        self.scenari = scenari
        self.test_url = re.compile('^http(s)?:\/\/.*\..*$')

    def test_url(self, url):
        if not self.test_url.match(url):
            raise('Votre url est malformée')

    def action_repl(self):
        '''
        Permet de remplacer les actions text par les bonnes fonctions dans les scenario

        :return: scenari (sans action)
        '''
        try:
            self.action = getattr(self, self.scenari['action'])
            self.scenari.pop('action')
        except KeyError:
            raise ('Vous devez décrire une action pour votre scenari')
        return self.scenari

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


    async def get_request(self, **kwargs):
        '''
        
        :param url: page demandée
        :return: 
        '''
        async with self.session.get(**kwargs) as response:
            print(response.status)
            return await response.read()


    async def post_request(self, **kwargs):
        '''
        Génére une requête post via la session etablie
        
        :return: 
        web response, aoihttp object
        '''
        async with self.session.post(**kwargs) as response:
            print(response.status)
            return await response.read()

    async def request(self):
        kwargs = self.action_repl()
        await self.action(kwargs)




if __name__ == '__main__':

    with closing(asyncio.get_event_loop()) as loop:
        con = Connect({'action':'post_request','url':GUICHET_ADRESSE, 'data':CODES })
        loop.run_until_complete(con.do_scenari())
