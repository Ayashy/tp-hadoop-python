#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mrjob.job import MRJob

class MRMatrice(MRJob):

    def __init__(self, *args, **kwargs):
        super(MRMatrice, self).__init__(*args, **kwargs)
        self.vecteur=self.options.vector
        self.results={}
    
    def configure_args(self):
        super(MRMatrice, self).configure_args()
        self.add_file_arg('--vector')

    def mapper_init(self):
        with open(self.vecteur) as file :
            self.vecteur=[float(x) for x in file.readlines()[0].split()]

    def combiner(self, lineID,line):
        result=0
        for val in line:
            result+=float(val)
        yield (lineID, result)    

    def mapper(self, _, line):
        for i,val in enumerate(line.strip().split()[1:]):
            yield (line.strip().split()[0], float(val)*self.vecteur[i])

    def reducer(self, lineID, line):
        result=0
        for val in line:
            result+=float(val)
        self.results[int(lineID)]=result

    def reducer_final(self):
        for key in sorted(self.results.keys()):
            yield (key, self.results[key])



if __name__ == '__main__':
    MRMatrice.run()
