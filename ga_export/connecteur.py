import re
import aiohttp
import asyncio
from contextlib import closing
import random

from ga_export.settings import *


def problemes_connexion(func):
    '''
    Decorateur permettant d'émettre une erreur en cas non possiblité de connexion
    :return: 
    '''
    def clientresponse(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (aiohttp.client_exceptions.ClientResponseError) as e:
            print('Connection au site web impossible --> {}'.format(e))

    return clientresponse


class Connect(object):


    def __init__(self, **scenari):
        '''
        L'objet connect permet de se connecter au guichet adresse et d'interrragir avec ce dernier
        :param adresse: adresse à laquelle se connecter (chaine de caractère)
        :param credentials: login et mdp contenues dans un dictionnaire
        '''
        #self.session = session
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



    @problemes_connexion
    async def get_request(self, **kwargs):
        '''
        
        :param url: page demandée
        :return: 
        '''
        # print('nous sommes en get')
        if 'session' in kwargs:
            async with self.session.get(**kwargs) as response:
                return (self.session, await response.text())
        else:
            async with aiohttp.ClientSession(raise_for_status=True) as self.session:
                #print(await asyncio.sleep(random.randint(1, 100)))
                # time = random.randint(1, 10)
                # print(str(time))
                # await asyncio.sleep(time)
                async with self.session.get(**kwargs) as response:
                    return (self.session, await response.text())

    @problemes_connexion
    async def post_request(self, **kwargs):
        '''
        Génére une requête post via la session etablie
        
        :return: 
        web response, aoihttp object
        '''
        # print('nous sommes en post')

        # async with self.session.post(**kwargs) as response:
        #     return await response.text()
        # else:
        if 'session' in kwargs:
            async with self.session.post(**kwargs) as response:
                return (self.session, await response.text())
        else:
            async with aiohttp.ClientSession(raise_for_status=True) as self.session:
                # time =random.randint(1, 100)
                # print(str(time))
                # await asyncio.sleep(time)
                async with self.session.post(**kwargs) as response:
                    return (self.session, await response.text())

    async def request(self):
        kwargs = self.action_repl()
        return await self.action(**kwargs)




if __name__ == '__main__':

    with closing(asyncio.get_event_loop()) as loop:
        con = Connect({'action':'post_request','url':GUICHET_ADRESSE, 'data':CODES })
        loop.run_until_complete(con.do_scenari())
