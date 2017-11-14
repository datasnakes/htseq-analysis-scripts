# -*- coding: utf-8 -*-
import pandas as pd
import os
from HTSeqAnalysis.pbsjob import PBSJob

df = pd.read_csv('impulsivity_samplenames.csv', header=None)
samplenames = sorted(list(df[0]))

path = '/ddn/home3/vallender/Projects/Impulsivity'
commandpath = '/home/ums/r1954/ptmp/HTSeq-0.9.1/scripts/htseq-count'
command = 'htseq-count'

for samplename in samplenames:
    samplepath = os.path.join(path, samplename)