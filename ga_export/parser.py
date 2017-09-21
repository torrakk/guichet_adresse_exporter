####
# Le parser permet d'aller chercher les éléments qui nous interessent dans la page web

####
from bs4 import BeautifulSoup
import operator
from functools import reduce

class parse():

    def __init__(self, page):
        assert type(page)==str, "La page doit être de type string"
        self.page = page
        self.soup = BeautifulSoup(self.page, 'html.parser')

    def parse(self, **kwargs):
        '''
        
        :param objet: recherche un objet contenu dans une balise
               kwargs : {'type':None, 'classe':None, 'value':None, 'regex':None} 
        :return: 
    
        '''

        model = {'type':None, 'classe':None, 'value':None, 'regex':None}
        dict = { args:kwargs[args] for args in model.keys() if args in kwargs.keys() }
        print([i.attrs for i in self.soup.find_all(**kwargs)])
        print([i.contents for i in self.soup.find_all(**kwargs)])




    def filterfunct(self, **kwargs):
        '''
        
        :param kwargs: paramètres injectés dans parse 
        :return: 
        '''
        return reduce(operator.and_, kwargs)

if __name__=='__main__':
    a = parse('<html><head><title>test</title></head><body><div class="test" value="ok">xxx</div><div class="test" >yyy</div></body></html>').parse(**{'class':'test', 'value':'ok'})
