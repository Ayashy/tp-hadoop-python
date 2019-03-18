#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRMatrice(MRJob):

    def __init__(self, *args, **kwargs):
        super(MRMatrice, self).__init__(*args, **kwargs)
        self.vecteur=[]

    def mapper_init(self):
        self.vecteur=[2,4.5,6]
    
    def mapper(self, _, line):
        for i,val in enumerate(line.strip().split()[1:]):
            yield (line.strip().split()[0], int(val)*self.vecteur[i])

    def reducer(self, lineID, line):
        result=0
        for val in line:
            result+=int(val)
        yield (lineID, result)


if __name__ == '__main__':
    MRMatrice.run()
