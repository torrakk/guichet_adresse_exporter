import re
import aiohttp
import asyncio
from contextlib import closing

from ga_export.settings import *

class Connect(object):

    def __init__(self, adresse, code):
        '''
        L'objet connect permet de se connecter au guichet adresse et d'interrragir avec ce dernier
        :param adresse: adresse à laquelle se connecter (chaine de caractère)
        :param credentials: login et mdp contenues dans un dictionnaire
        '''
        self.loop = loop
        self.code = code
        self.adresse = adresse
        self.test_url = re.compile('^http(s)?:\/\/.*')
        if not self.test_url.match(self.adresse):
            raise('Votre url est malformée')


    async def connect_post(self):
        '''
        Etabli une connexion via l'url, avec les logins et mdp de passe voulus
        
        Ajouter le 
        _csrf_token
        et le _submit
        :return: 
        '''

        async with aiohttp.ClientSession() as self.session:
            async with self.session.post(url=self.adresse, data=self.code) as self.response:
                print(self.response.status)
                self.resp = await self.response.text()
                if 'Extraire' in self.resp:
                    print('OK\n\n')
                #print(self.response)

    def parse_page(self):
        '''
        Permet d'analyser la page comprennant les exports existants paramétrés
        :return: 
        '''

    def export_result(self):
        '''
        
        :return: 
        '''

if __name__ == '__main__':

    with closing(asyncio.get_event_loop()) as loop:
        con = Connect(GUICHET_ADRESSE, CODES)
        loop.run_until_complete(con.connect_post())
