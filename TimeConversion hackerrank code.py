#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def timeConversion(s):
    if (s.__contains__('PM')==True)and(s.__contains__('12')==False):
        s_new = s.replace('PM','')
        string_list = s_new.split(':')
        if(string_list[0]=='12'):
            string_list[0] = '0'+str(int(string_list[0])%12)
        else:
            string_list[0] = str(12 + int(string_list[0]))
        final_string = ':'.join(string_list)
    elif (s.__contains__('AM')==True):
        s_new = s.replace('AM','')
        string_list = s_new.split(':')
        if(string_list[0]=='12'):
            string_list[0] = '0'+str(int(string_list[0])%12)
        final_string = ':'.join(string_list)
    elif (s.__contains__('PM')==True):
        s_new = s.replace('PM','')
        string_list = s_new.split(':')
        if(string_list[0]=='12'):
            final_string = ':'.join(string_list)
    return final_string

