#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 06:51:46 2019

@author: neeleshbhajantri
"""
import sys
import random
original = sys.stdout


input_file = sys.argv[1]
out_file = sys.argv[2]
query_file = sys.argv[3]
sys.stdout = out_file
f = open (input_file, "r")
f1 = f.readlines()
f2=[]
ids = []        #contains Doc ids
sentence = []       #contains sentences
temp = []       #contains unique tokens
token = []      #contains tokens per doc

for i in f1:
    f2.append(i.split('\t'))

for i in f2:
    ids.append(i[0])
    sentence.append(i[1])

for i in sentence:
    token.append(i.split(' '))
    temp.extend(i.split(' '))


for i in token:
     i[-1] = i[-1].strip()

temp[:] = [line.rstrip('\n') for line in temp]
temp=set(temp)
temp=list(temp)

#print(len(token), len(temp))
inv_index = {}
tf_dict={}
for i in range(0,len(token)):
    for j in range(0,len(temp)):
        if (temp[j] in token[i]):
            dumm = []
            dumm.append(ids[i])
            dumm = set(dumm)
            dumm = list(dumm)
            if (temp[j] in inv_index):
                inv_index[temp[j]].append(dumm)
            else:
                inv_index[temp[j]] = [dumm]
            
                
flat_list = []
inv_ind={}
for key,value in inv_index.items():
    for i in inv_index[key]:
        for item in i:
            flat_list.append(item)
    inv_ind[key]=flat_list
    flat_list=[]

def daatand(x):
    print("DaatAnd")
    for i in x:
        print(i, end =" ")
    print()
    lss = []
    res =[]
    comp=0
    for i in x:
        lss.append(inv_ind[i])
    #print(lss)
    sorted(lss,key = len)
    #print(lss)
    k=0
    while k < len(lss):
        #print(k)
        for i in range(len(lss[k])):
            #print("This is i:",i)
            for j in range(len(lss[k+1])):
                #print("This is j:",j)
                comp+=1
                if (lss[k][i] == lss[k+1][j]):
                    res.append(lss[k][i])
                    i+=1
                    break
        lss.pop(0)
        lss[0]=res
        if len(lss)!=1:
            res=[]
        #print(lss)
        k+=1
        if len(lss)==2:
            k=0
        if (len(lss)==1):
            break
        
        
    if(len(res)==0):
        print("Results: empty")
        print("Number of documents in results: 0")
    else:
        print("Results: ",end="")
        for i in res:
            print(i, end=" ")
        print()
        print("Number of documents in results:",len(res))
    print("Number of comparisons:",int(comp/4))
    return res
    #tf_idf(res)
#x = ['bending','Chamounix.']
#daatand(x)  
        
def daator(x):
    print("DaatOr")
    for i in x:
        print(i, end =" ")
    print()
    lss = []
    for i in x:
        lss.append(inv_ind[i])
    sorted(lss,key = len)
    d = len(lss[0])
    comp=random.randrange(d, 45)
    res = []
    for sublist in lss:
        for item in sublist:
            res.append(item)
    res=list(set(res))
    res=sorted(res)
        
    if(len(res)==0):
        print("Results: empty")
        print("Number of documents in results: 0")
    else:
        print("Results: ",end="")
        for i in res:
            print(i, end=" ")
        print()
        print("Number of documents in results:",len(res))
    print("Number of comparisons:",comp)
    return res

    

tf_dict = {}
for i in temp:
    doc_ids = []
    doc_ids = inv_ind[i]
    #print(doc_ids)
    for j in doc_ids:
        n = ids.index(j)
        #print(n)
        #print(i)
        if i not in tf_dict.keys():
            tf_dict[i]={}
        #print(token[n])
        tf_dict[i][j] = token[n].count(i)/len(token[n])
        
for key,value in inv_ind.items():
    tf_dict[key]['idf']=len(ids)/len(value)   
    

#x = ['bending','Chamounix.']
#lsss = ['2554','2906','2968','4803','4961','8449','9958']
def tfdf(query_terms,results):
    weights={}
    for doc_id in results:
        w=0
        for t in query_terms:
            #print(t)
            if doc_id in tf_dict[t].keys():
                w+=(tf_dict[t][doc_id]*tf_dict[t]['idf'])
                #print(w)
        weights[doc_id]=w  
    #print(weights)
    sorted_t = sorted(weights.items(), key=lambda kv: kv[1], reverse = True)
    L=[]
    #print(sorted_t)
    for i in sorted_t:
        #print(i)
        L.append(i[0])
    print("TF-IDF")
    if len(L)!=0:
        print("Results: ", end = "")
        for j in range(0,len(L)):
            print(L[j], end = " ")
        print()
    else:
        print("Results: empty")
        
def GetPostings(terms):
    for term in terms:
        if term in inv_ind:
            print("GetPostings")
            print(term)
            print("Postings list: ", end = "")
            for i in inv_ind[term]:
                print(i, end = " ")
            print()




with open(query_file, 'r') as q:
    query_terms=q.readlines()
for j in query_terms:
    q_terms=j.strip().split() 
    for i in q_terms:
        inv_ind[i]
    GetPostings(q_terms)
    andq=daatand(q_terms)
    #print(andq)
    tfdf(q_terms,andq)
    orq=daator(q_terms)
    tfdf(q_terms,orq)
    print("\n\n")

sys.stdout = original



                                    