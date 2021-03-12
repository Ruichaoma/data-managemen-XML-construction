#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys
import re
from lxml import etree


# In[3]:


val = []
which_lst = []
where_lst = []


    
def whether_floating_type(factor):
    if type(factor) == float:
        return True
    else:
        return False
dir_folder = sys.argv[1]
def return_input(dire):
    return os.listdir(dire)
input_folder = return_input(dir_folder)
for xml_file in input_folder:
    file_load = etree.parse(f"{dir_folder}/{xml_file}")
    tag_list = []
    for i in file_load.getroot().iter():
        if i.tag not in tag_list:
            tag_list.append(i.tag)
    
    if len(tag_list) > 1:
        str_tag_list = []
        for j in range(len(tag_list)):
            if type(tag_list[j]) == str:
                str_tag_list.append(tag_list[j])
    tag_list_specific_info = file_load.xpath(f'//{str_tag_list[1]}')
    length_tag_list_specific_info = len(tag_list_specific_info)
    tag_list_specific_info_lst = []
    for i in range(length_tag_list_specific_info):
        
        if len(tag_list_specific_info[i].attrib)>0:
            
            for key, value in sorted(tag_list_specific_info[i].items()):
                val.append(value)
                which_lst.append(xml_file)
                where_lst.append(f"{str_tag_list[0]}.{str_tag_list[1]}.{key}")
             
    for i in range(2,len(str_tag_list)):
        for content in file_load.xpath(f'/{str_tag_list[0]}/{str_tag_list[1]}/{str_tag_list[i]}'):
            #print(content.text)
            content_text = content.text
            if content_text is not None:
                content_text = content_text.replace('_','')
                if whether_floating_type(content_text) == True:
                    if '.' not in content_text:
                        tight_str = re.sub("[^\w\s]", " ", content_text)
                        tight_str_split = tight_str.split()
                        val.append(tight_str_split[0])
                        which_lst.append(xml_file)
                        where_lst.append(f"{str_tag_list[0]}.{str_tag_list[1]}.{str_tag_list[i]}")
                    if '.' in content_text:
                        tight_str = re.sub("[^\w\s]", " ", content_text)
                        tight_str_split = tight_str.split()
                        if len(tight_str_split)>0:
                            for c in range(len(tight_str_split)):
                                val.append(tight_str_split[c])
                                which_lst.append(xml_file)
                                where_lst.append(f"{str_tag_list[0]}.{str_tag_list[1]}.{str_tag_list[i]}")                      
                else:
                    tight_str = re.sub("[^\w\s]", " ", content_text)
                    tight_str_split = tight_str.split()
                    if len(tight_str_split)>0:
                        for c in range(len(tight_str_split)):
                            val.append(tight_str_split[c])
                            which_lst.append(xml_file)
                            where_lst.append(f"{str_tag_list[0]}.{str_tag_list[1]}.{str_tag_list[i]}")
                            
                    

                                
index_root = etree.Element("index")  
#token_root = etree.SubElement(index_root,"token")
for i in (set(val)):
    token_root = etree.SubElement(index_root,"token")
    etree.SubElement(token_root,"value").text = i
    for k in range(len(val)):
        if i == val[k]:
            provenance_root = etree.SubElement(token_root,"provenance")
            etree.SubElement(provenance_root,"which").text = which_lst[k]
            etree.SubElement(provenance_root,"where").text = where_lst[k]
            
            
def output_xml(output_file,root_content):
    with open(output_file, 'wb') as output_xmlfile:
        all_write = etree.tostring(root_content, pretty_print = True)
        output_xmlfile.write(all_write)
        output_xmlfile.close()
            
output_xml_file = sys.argv[2]
            
output_xml(output_xml_file,index_root)

            
            
    
                
         
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




