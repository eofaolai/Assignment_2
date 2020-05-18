#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import flask
app = flask(__name__)

@app.route(’/hello/<name>’, methods=[’GET’])
def hello_world(name):
return "Hello, {}!".format(name)

if __name__ == "__main__":
app.run(host=’0.0.0.0’, port=8080)


# In[ ]:


from flask import flask
app = flask(__name__)

# request from url 
@app.route(’18.207.92.139:8000/random company’, methods=[’GET’])
##def hello_world(name):
##return "Hello, {}!".format(name) ##return render template?
##GET_RESP = REQUESTS.GET(’18.207.92.139:8000/random company’,TIMEOUT)

get_resp = requests.get(’18.207.92.139:8000/random company’, timeout=5)

##post_resp = requests.post(URL_STRING, data=DICTIONARY)

# Download the HTML of this website and extract the name and purpose of the generated company.
# beautiful soup to parse through HTML
# repeat x50 with sleeps

## write to external file, use file handler
with open() as fh
    fh.write()


if __name__ == "__main__":
app.run(host=’0.0.0.0’, port=8080)


# In[1]:


from bs4 import BeautifulSoup
import requests


# In[77]:


f= open("Company_site_scrape.txt","w+")

for i in range(50):
    url = 'http://174.129.86.170:8000/random_company'
    get_resp = requests.get(url, timeout=5)
    content = BeautifulSoup(get_resp.content, "html.parser")
    text = content.get_text()
    
    find_name = text.find('Name:')
    find_name = find_name + 6
    length_name = text[find_name:].find('\n')
    end_name = find_name + length_name
    pull_name = text[find_name:end_name]
    
    find_purpose = text.find('Purpose:')
    find_purpose = find_purpose + 9
    length_purpose = text[find_purpose:].find('\n')
    end_purpose = find_purpose + length_purpose
    pull_purpose = text[find_purpose:end_purpose]
    
    
    f.write(pull_name + "; " + pull_purpose + "; ")
        
f.close()


# In[49]:


#### code testing from this cell

#reponse = requests.get(’18.207.92.139:8000/random company’, timeout=5)
#url = ’http://18.207.92.139:8000/random_company’
url = 'http://174.129.86.170:8000/random_company'
get_resp = requests.get(url, timeout=5)
content = BeautifulSoup(get_resp.content, "html.parser")

print(content)


# In[28]:


len(content.find("body"))


# In[50]:


text = content.get_text()
#soup_name = content.find('Name')
#print(soup_name)
print(text)
#soup_text.find_all(text='Name')


# In[70]:


find_name = text.find('Name:')
find_name = find_name + 6
print(find_name)


# In[71]:


length_name = text[find_name:].find('\n')
length_name


# In[72]:


end_name = find_name + length_name
print(end_name)


# In[73]:


pull_name = text[find_name:end_name]
pull_name


# In[74]:


find_purpose = text.find('Purpose:')
find_purpose = find_purpose + 9
#print(find_purpose)
length_purpose = text[find_purpose:].find('\n')
#length_purpose
end_purpose = find_purpose + length_purpose
#print(end_purpose)
pull_purpose = text[find_purpose:end_purpose]
pull_purpose


# In[76]:


print(pull_name + "; " + pull_purpose + "; ")


# In[ ]:




f.write(pull_name + "; " + pull_purpose + "; ")


# In[6]:


#soup_text.body.findAll(text='Name:')


# In[27]:


#string1 = content.findAll('li')
#print(string1)


# In[29]:


#Name1 = string1.find('Name:')
#print(Name1)


# In[28]:


#Name1 = content.findAll('li', attrs={'class':'name'})
#print(Name1)


# In[ ]:


### Resource citations: 
### https://hackernoon.com/building-a-web-scraper-from-start-to-finish-bb6b95388184
### https://realpython.com/beautiful-soup-web-scraper-python/
### https://www.guru99.com/reading-and-writing-files-in-python.html


# In[ ]:


### 1. Make a request to “18.207.92.139:8000/random company”
### 2. Extract the company name and company purpose
### 3. Repeat this process 50 times

### save to file

