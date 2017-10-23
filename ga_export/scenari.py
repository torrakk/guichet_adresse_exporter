import asyncio
from contextlib import closing

from ga_export.parser import Parse
from ga_export.connecteur import Connect

class scenari():
    '''
    Un scenari est un objet cappable de se connecter et de s'appeler de manière recursive en passant 
    les attributs d'une page web scrapper à une autre
    
    le scenari se sert des objets futures pour
    1) Se connecter à la page 
    2) Parser ce qu'il y a à parser
    3) Ajouter un scenari enfant avec le resultat de 1 et 2
    
    '''

    def __init__(self, **kwargs):
        self.future = asyncio.Future()
        self.kwargs = kwargs
        # print("objet créée")
        actions = ['action', 'url', 'data', 'parse', 'scenari']

        assert list(self.kwargs.keys()) == actions, \
            "Votre scenari est malformé, " \
            "il manque des informations " \
            "{} doit être {}".format(self.kwargs, actions)

        for attr, value in kwargs.items():
            if attr in actions:
                setattr(self, attr, value)

    def validate(self):
        '''
        Cette fonction permet de verifier un scenari
        :return: 
        '''

    async def connect(self):
        '''
        Cette fonction permet se connecter à une page avec une methode get ou post
        Nous preparons les arguments pour qu'ils ne concernent que l'action à engagé
        :return: 
        '''
        co = Connect(**{ key: value for key, value in self.kwargs.items() if key in ('action', 'url', 'data')})
        return await co.request()

    def callback_scenari(self, future):
        '''
        Methode permettant de se servir de la session ouverte pour continuer à travailler 
        avec les données reçues et les cookies
        Pour cela nous injectons l'objet en tant que future dans la boucle evenementielle
        :return: 
        '''
        print('Nous sommes dans le callback')
        asyncio.ensure_future(scenari(**self.kwargs['scenari']).run())

    def print_fut(self, future):
        print(future.result())

    async def run(self):
        self.future.add_done_callback((self.callback_scenari if self.kwargs['scenari']!=[] else self.print_fut))
        session, page = await self.connect()
        return self.future.set_result(Parse(page).list_parse(self.parse)) if self.parse \
        else self.future.set_result(page)

    def __repr__(self):
        return(str(self.__dict__))


# if __name__=="__main__":
#     with closing(asyncio.get_event_loop()) as loop:
#         con = Connect({'action': 'post_request', 'url': GUICHET_ADRESSE, 'data': CODES})
#         loop.run_until_complete(con.do_scenari())