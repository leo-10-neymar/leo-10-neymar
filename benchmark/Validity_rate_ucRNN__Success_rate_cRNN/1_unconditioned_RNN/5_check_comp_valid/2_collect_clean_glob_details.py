#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Hang Xiao 2023.04
# xiaohang07@live.cn
import os,sys,glob


pwd=os.getcwd()

#os.system("rm results_"+pwd.split("/")[-1]+"_unique.sli")
os.system("rm results_"+pwd.split("/")[-1]+".sli")

result_csv=''
result_filtered_csv=''
slices=[]

for i in glob.glob("job_*/result.csv"):
    with open(i,'r') as result:
        for i in result.readlines():
            slices.append(i.strip())
print(len(slices))

with open("results_"+pwd.split("/")[-1]+".sli",'a') as result:
    for i in slices:
        result.write(i+'\n')


for i in glob.glob("job_*"):
    os.system("rm -r "+i)
                
                
                
                
