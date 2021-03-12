#!/usr/bin/env python
# coding: utf-8

# In[57]:


import os
import sys
import re
from lxml import etree




input_xml = sys.argv[1]
dir_folder = sys.argv[2]
input_info = sys.argv[3]
def return_input(dire):
    return os.listdir(dire)
input_folder = return_input(dir_folder)
input_info_split = input_info.split(" ")
tree = etree.parse(input_xml)
which_lst = []
where_lst = []
which_attri_lst = []
where_attri_lst = []
Element_lst = []
file_lst = []

def first_step(info,nage,nali):
    for i in info:
        for j in tree.xpath(f'//token[value = "{i}"]'):
            for a1 in j.xpath('provenance/which'):
                nage.append(a1.text)
            for a2 in j.xpath('provenance/where'):
                nali.append(a2.text)
first_step(input_info_split,which_lst,where_lst)
            
#print(which_lst)
#print(where_lst)

def first_attri_step(info,nage,nali):
    for i in info:
        for j in tree.xpath(f'//@token[contains(value, "{i}")]]'):
            for a1 in j.xpath('provenance/which'):
                nage.append(a1.text)
            for a2 in j.xpath('provenance/where'):
                nali.append(a2.text)
                

first_step(input_info_split,which_lst,where_lst)
for i in input_info_split:
    for k in range(len(which_lst)):
        tree = etree.parse(f"{dir_folder}/{which_lst[k]}")
        where_lst_split = where_lst[k].split(".")
        
        for content in tree.xpath(f'/{where_lst_split[0]}/{where_lst_split[1]}/{where_lst_split[2]}'):
            if i in content.text:
                elem = f'Element:<{content.tag}>{content.text}</{content.tag}>'
                if elem not in Element_lst:
                    Element_lst.append(f'Element:<{content.tag}>{content.text}</{content.tag}>')
                    file_lst.append(f'File:{which_lst[k]}')


        for content in tree.xpath(f'//{where_lst_split[1]}'):
            #print(len(content))
            if len(content.attrib)>0:
                for key, value in sorted(content.items()):
                    if i in value:
                        elem = f'Element:<{key}>{value}</{key}>'
                        if elem not in Element_lst:
                            Element_lst.append(f'Element:<{key}>{value}</{key}>')
                            file_lst.append(f'File:{which_lst[k]}')


def judge_word(element,file):
    if  len(file)>0:
        return True
    else:
        return False
    
if judge_word(Element_lst,file_lst) == True:
    for i in range(len(Element_lst)):
        print(Element_lst[i])
        print(file_lst[i])
else:
    print("No such tokens")
        



# In[ ]:





# In[ ]:




