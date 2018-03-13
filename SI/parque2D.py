# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 14:54:52 2018

@author: fc48286
"""

from agents import *


class Parque2D (XYEnvironment) :
    
    def default_location(self,thing) :
        return 0
    
    
    def percept(self, agent):
        '''prints & return a list of things that are in our agent's location'''
        things = self.list_things_at(agent.location)
        print("{}:{}".format(agent.nome,list(map(str,things))))  ## exercício 3/4
        return things
    
    
    def execute_action(self, agent, action):
        '''changes the state of the environment based on what the agent does.'''
        if action == "move down":
            agent.movedown()
        elif action == "eat":
            items = self.list_things_at(agent.location, tclass=Food)
            if len(items) != 0:
                if agent.eat(items[0]): #Have the dog pick eat the first item
                    self.delete_thing(items[0]) #Delete it from the Park after.
        elif action == "drink":
            items = self.list_things_at(agent.location, tclass=Water)
            if len(items) != 0:
                if agent.drink(items[0]): #Have the dog drink the first item
                    self.delete_thing(items[0]) #Delete it from the Park after.
                
                
    def is_done(self):
        '''By default, we're done when we can't find a live agent, 
        but to prevent killing our cute dog, we will or it with when there is no more food or water'''
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water)\
                             for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles
    
    
    def __str__(self):
        d = dict()
        for x in self.things :
            loc = x.location
            d[loc] = d.get(loc,"") + "/" + str(x)
        if len(self.things) > 0 :
            max_loc = max([x.location for x in self.things])
        else :
            max_loc = -1

        mapa = str()
        for i in range(max_loc + 1):
            mapa += "{}: {}\n".format(i,d.get(i,""))

        return str(mapa)


class BlindDog(Agent) :
    def __init__(self, nome, programa = None) :
        super().__init__(programa)
        self.nome = nome
    
    @property
    def nome(self) :
        return self.__nome
    @nome.setter
    def nome(self,nome) :
        self.__nome = nome
        
    def movedown(self):
        self.location += 1
    
    def eat(self, thing):
        '''returns True upon success or False otherwise'''
        if isinstance(thing, Food):
            print("Dog: {} ate food at {}.".format(self.nome,self.location))
            return True
        return False
    
    def drink(self, thing):
        ''' returns True upon success or False otherwise'''
        if isinstance(thing, Water):
            print("Dog: {} drank water at {}.".format(self.nome,self.location))
            return True
        return False

    def __str__(self) :
        return self.nome


if __name__ == '__main__' :
    
    parque = Parque2D(8,6) # criação de um parque com 8 colunas e 6 linhas
    print("largura:",parque.width)
    print("altura:",parque.height)
    print("x_start:", parque.x_start)
    print("x_end:", parque.x_end)
    print("y_start:", parque.y_start)
    print("y_end:", parque.y_end)
    
    #print("#------------------------------------------------------------#")
    #cao = BlindDog()
    #parque.add_thing(cao)
    #print(cao.location)
    print("#------------------------------------------------------------#")
    
    dog1 = BlindDog("*")
    dog2 = BlindDog("@")
    parque.add_thing(dog1, (1,2))
    parque.add_thing(dog2, (3,4))
    print(parque)