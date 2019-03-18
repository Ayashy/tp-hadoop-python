#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mrjob.job import MRJob
from mrjob.step import MRStep


class MRSideJoin(MRJob):

    def __init__(self, *args, **kwargs):
        super(MRSideJoin, self).__init__(*args, **kwargs)
        self.vecteur=[]

    def mapper(self,_,line):
        data=line.strip().split(',')
        if(len(data)<6):
            yield (line.strip().split(',')[0], line.strip().split(',')[1])
        else:
            yield (line.strip().split(',')[2], line.strip().split(',')[3])

    def reducer(self, lineID, line):
        data=[val for val in line]
        yield (data[0], [round(sum([float(x) for x in data[1:]]),2),len(data)-1])


if __name__ == '__main__':
    MRSideJoin.run()
