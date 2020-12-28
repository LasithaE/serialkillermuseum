from flask import Flask, render_template,request, url_for,redirect
from bs4 import BeautifulSoup as bs
import requests
app = Flask(__name__)
source = requests.get('https://en.wikipedia.org/wiki/List_of_serial_killers_by_country').text
soup = bs(source, 'lxml')

@app.route('/')
def index():
    td1=soup.find_all('h3')
    countries,k=[],''
    a1=td1[0:85]
    for i in range(len(a1)):
        k=a1[i]
        countries.append(k.text)
    countries.remove('United States')
    countries.remove('Germany')
    countries.remove('France')
    
    return render_template('index.html',**locals())

@app.route("/test" , methods=['GET', 'POST'])

def test():
    
    select = request.form.get('country_name')
    td=soup.find_all('h3')[0:78]
    for w in range(len(td)):
        if td[w].text==select:
            td2=(td[w])
  
    uls ,lis = [],[]
    for nextSibling in td2.findNextSiblings():
        if nextSibling.name == 'h3':
            break
        if nextSibling.name == 'ul':
            uls.append(nextSibling)

    for k in uls:
        for li in k.find_all('li'):
            lis.append(li)
    data,imgs,Img_URL,links=[],[],[],[]
    for j in range(len(lis)):
        a=lis[j].text.rsplit("[")[0]
        data.append(a)
    for q in range(len(lis)):
        Img_URL.append(lis[q].find_all('a')[0].get('href'))
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
        
    return render_template('card.html',len = len(data), data = data,imgs=imgs,links=links)
@app.route("/about" , methods=['GET', 'POST'])
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(threaded=True, port=5000)
