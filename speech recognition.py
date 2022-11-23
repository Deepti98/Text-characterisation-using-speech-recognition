#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import speech_recognition as sr


# In[2]:


import IPython.display as ipd


# In[3]:


recognizer = sr.Recognizer()
audio_file = sr.AudioFile("voice-data.wav")
type(audio_file)


# In[4]:


with sr.AudioFile("voice-data.wav") as source:
    audio_file=recognizer.record(source)
    result=recognizer.recognize_google(audio_data=audio_file)


# In[5]:


result


# In[6]:


with sr.AudioFile("voice-data.wav") as source:
    audio_file=recognizer.record(source, duration=5.0)
    result1=recognizer.recognize_google(audio_data=audio_file)


# In[7]:


result1


# In[8]:


with sr.AudioFile("voice-data.wav") as source:
    audio_file=recognizer.record(source,offset=6.0)
    result2=recognizer.recognize_google(audio_data=audio_file)


# In[9]:


result2


# # Cobining both the result

# In[10]:


with sr.AudioFile("voice-data.wav") as source:
    audio_file=recognizer.record(source,duration=5.0,offset=2.0)
    result3=recognizer.recognize_google(audio_data=audio_file)


# In[11]:


result3


# # Effect of noise

# In[12]:


with sr.AudioFile("voice-data.wav") as source:
    audio_file=recognizer.adjust_for_ambient_noise(source,duration=0.5)
    audio=recognizer.record(source)
    
result4=recognizer.recognize_google(audio)


# In[13]:


print(result4)


# In[14]:


result_str=result.split(' ')


# In[15]:


result_str


# # Different number of words used

# In[16]:


unique_words=set(result_str)
print(unique_words)


# In[17]:


print("Number of different words used :",len(unique_words))


# # Count the repeatation of words
# #First we will store the unique words in the dictionary

# In[18]:


#To count the number of times the unique words appear,first in unique_words list
word_dict={}#An empty dictionary
for word in result_str:
    word_dict[word]=0
print(word_dict)


# In[19]:


for word in result_str:
    word_dict[word]=word_dict[word]+1
print("The count for each word spoken number of times are :",word_dict)


# In[20]:


cols=['Repeatation']


# In[21]:


count_df=pd.DataFrame.from_dict(word_dict,orient='index',columns=cols)


# In[22]:


count_df


# In[23]:


count_df=count_df.reset_index()


# In[24]:


count_df


# In[25]:


count_df=count_df.rename(columns={'index':'word'})


# In[26]:


count_df


# # Counting the number of words spoken per minute

# In[27]:


print("Total number of words:",len(result_str))


# In[28]:


print("Total length of audio:3.08 minutes")


# In[29]:


print("Total number of words spoken per minute are:",(len(result_str)/3.08))


# In[ ]:




