#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Minln


class Animal(object):
    pass

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dogs(Mammal,Runnable):
    pass

class Bats(Mammal,Flyable):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class CarnivorousMinIn(object):
    def fly(self):
        print('Carniver...')

class Dogss(Mammal,RunnableMixIn,CarnivorousMinIn):
    pass

