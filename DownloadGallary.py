import argparse
import sys
import requests
from bs4 import BeautifulSoup
import os

def ima(link,page):
    gid=link.split('/')[4]
    url=link+"?gid="+gid+"&page="+page+"&view=0"

    r=requests.get(url)
    page_view=r.content
    soup = BeautifulSoup(page_view,"html.parser")

    form_tag=soup.find_all("form",attrs={"action":"?gid="+gid+"&pid=&view=0&edit=1"})[0]
    photo_id=form_tag.find_all("table")[0].find_all("tr")[0].find_all("td")[0]['id']

   
    host=link[0:link.find(".com")]
    print(host) 
    slideshow_url=host+".com/photo/"+photo_id+"/?pgid=&gid="+gid+"&page="+page
    


    slide_r=requests.get(slideshow_url)
    slide_html=slide_r.content
    slide_soup = BeautifulSoup(slide_html,"html.parser")
    a_tags=slide_soup.find_all("div",attrs={"id","navigation"})[0].find_all("a")

    index=1
    for a_tag in a_tags:
        image_link=a_tag['original']
        name=image_link.split('?')[0].split('/')[7]
        print(str(index)+". Image link: "+image_link)
        with open(name, 'wb') as f:
            im = requests.get(image_link)
            f.write(im.content)
            print(str(index)+". Downloaded: "+ name+"\n")
        index+=1

def myp(link):
    r=requests.get(link)
    page_view=r.content
    soup = BeautifulSoup(page_view,"html.parser")
    image_wrap=soup.find_all("div",attrs={"class":"img-wrap"})[0]
    images_tags=image_wrap.find_all("a")

    tag_list=[]
    for tag in images_tags:
        if(tag['href'].find("#")==-1):
            tag_list.append(tag)

    image_url=link[0:link.find("index")]
    for image_tag in tag_list:
        image_link=image_url+image_tag['href']
        print("Image link: "+image_link)
        name=image_link.split('/')[6]+image_tag['href'].split('/')[1]
        with open(name, 'wb') as f:
            im = requests.get(image_link)
            f.write(im.content)
            print("Downloaded: "+ name+"\n")

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--link',type=str)
    parser.add_argument('--pages',type=str,default="0")
    parser.add_argument('--site',type=str)
    args = parser.parse_args()
    
    if(args.site=="ima"):
        pages=args.pages.split(",")
        for page in pages:
            ima(args.link,page)
    elif(args.site=="myp"):
        myp(args.link)
