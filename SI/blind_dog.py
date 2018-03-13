from agents import *
from parque2 import *

class BlindDog(Agent):
    def eat(self, thing):
        print("Dog: Ate food at {}.".format(self.location))
            
    def drink(self, thing):
        print("Dog: Drank water at {}.".format(self.location))
        

class Food(Thing):
    pass

class Water(Thing):
    pass

class Park(Environment):
    def percept(self, agent):
        '''prints & return a list of things that are in our agent's location'''
        things = self.list_things_at(agent.location)
        print(things)
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
        but to prevent killing our cute dog, we will or it with when there is no
        more food or water'''
        no_edibles = not any(isinstance(thing, Food) or isinstance(thing, Water) \
                             for thing in self.things)
        dead_agents = not any(agent.is_alive() for agent in self.agents)
        return dead_agents or no_edibles
        
    def __str__(self):
        grid = ""
        locations = {}
        for element in self.agents:
            locations.update({element.location:self.things})
            print(locations)
        return grid

cao = BlindDog()
cao2 = BlindDog()


#for a in cao.__dict__.keys() :
#    print(a)


#print(cao.alive)
#print(cao.program)
#print(cao.location)

parque = Park()
#print("Coisas: {}".format(parque.things))
#print("Agentes:{}".format(parque.agents))

parque.add_thing(cao)
parque.add_thing(cao2)

#print("Coisas: {}".format(parque.things))
#print("Agentes:{}".format(parque.agents))
#print(cao.location)

print(parque)

