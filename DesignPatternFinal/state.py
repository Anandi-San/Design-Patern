class EnemyState:
    name = "state"
    allowed = []

    def switch(self,state):
        if state.name in self.allowed:
            print('Current State:', self, '=> Enemy switched to', state.name)
            self.__class__ = state
        else:
            print('Current State:', self, '=> Enemy cannot switch to', state.name, 'from', self)

    def __str__(self):
        return self.name
class waiting(EnemyState):
    name = "waiting"
    allowed = ['patrolling', 'chasing']

class patrolling(EnemyState):
    name = "patrolling"
    allowed = ['waiting', 'chasing']

class chasing(EnemyState):
    name = "chasing"
    allowed = ['patrolling']

class Enemy:
    def __init__(self):
        self.state = waiting()

    def change(self,state):
        self.state.switch(state)

slime = Enemy()
print(slime.state.__str__())
slime.change(chasing)
slime.change(waiting)
print(slime.state.__str__())