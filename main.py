import requests
from bs4 import BeautifulSoup as bs
URL = 'https://en.wikipedia.org/wiki/List_of_serial_killers_by_country'
#for page in range
#a=input('Enter a country :')
#l=a.replace(" ", "_")
req = requests.get(URL)
soup =bs(req.text,'lxml')
#cntry=soup.find_all('ul')[1]
#td1=soup.find_all('h3')
#countries,k=[],''
#a=td[0:85]
#for i in range(len(a)):
    #k=a[i]
    #countries.append(k.text)
#print(countries)
#print(countries)
td=soup.find_all('h3')[0:78]
for i in range(len(td)):
    if td[i].text=='United Kingdom':
        td2=(td[i])
  
uls ,lis,Img_URL,links = [],[],[],[]
for nextSibling in td2.findNextSiblings():
    if nextSibling.name == 'h3':
        break
    if nextSibling.name == 'ul':
        uls.append(nextSibling)

for i in uls:
    for li in i.find_all('li'):
        lis.append(li)
#print(lis[4].find_all('a')[0].get('href'))
for q in range(len(lis)):
    Img_URL.append(lis[q].find_all('a')[0].get('href'))
#print(len(lis))
data=[]
#for j in range(len(lis)):
    #a=lis[j].text.rsplit("[")[0]
    #data.append(a)
#print('data:',data[0].rsplit(':')[0],data[0].rsplit(':')[1])
imgs=[]
#if '(' in data[20]:
    #name=data[20].rsplit('(')[0]
#elif':'in data[20]:
    #name=data[20].rsplit(':')[0]
#print(name)
#name=name.replace(' ','_')
#if name[-1]=='_':
    #name=name[:-1]
#print(name)
#source_img=requests.get(url_img).text
#print(source_img.title)
#table = soup_img.find('table').find_all('tr')[1].find_all('img')[0].get('src')

#print(table)
for name1 in Img_URL:
    url_img='https://en.wikipedia.org/'+name1
    source_img=requests.get(url_img).text
    soup_img= bs(source_img, 'lxml')
    try:
        img = soup_img.find('table').find_all('tr')[1].find_all('img')[0].get('src')
        name=name1.replace('/wiki/','')
        if name in img:
            img=img
        else:
            img=''
    except:
        img=''
    imgs.append(img)
    links.append(url_img)
print(links)
    #print(type(table))
    #img = table.find_all('img').get('src')
    #imgs.appen(img)
#print (imgs)


#print(lis[7].text.rsplit("[")[0])
#print('length:',len(lis))
#a=input('Enter a country:')

#td = soup.find_all('ul')[1].find_all('li')
#print(td)
#for i in range(78):
    #k=td[i].find_all('a')[0].get('href')
    #name='#'+a
    #if k==name:
        #print(k)
#for t in td:
    #k=t.find_all('a')
    

