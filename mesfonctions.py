from bs4 import BeautifulSoup
import pandas as pd
import re
import json as json

def json_to_dataframe(filename):
    videosID = pd.read_json(filename)
    print(f"\n{videosID.head()}\n")
    return videosID

def title_of_video(soup):
    return soup.find("meta", itemprop="name")["content"]

def name_of_author(soup):
    return soup.find("link",{'itemprop':'name'})["content"]

def number_of_likes(soup):
    data = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)  
    data_json = json.loads(data)
    videoPrimaryInfoRendererBuilder = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents']
    #print(videoPrimaryInfoRendererBuilder)
    indice = 0
    if 'videoPrimaryInfoRenderer' in videoPrimaryInfoRendererBuilder[0]:
        indice = 0
    elif 'videoPrimaryInfoRenderer' in videoPrimaryInfoRendererBuilder[1]:
        indice = 1
    else :
        indice = 2

    videoPrimaryInfoRenderer = videoPrimaryInfoRendererBuilder[indice]['videoPrimaryInfoRenderer']
    videoSecondaryInfoRenderer = videoPrimaryInfoRendererBuilder[(indice + 1)]['videoSecondaryInfoRenderer']
    likes = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
    likes = likes.replace('clics sur "J\'aime"', '')
    return likes

def description_of_video(soup):
    pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
    description = pattern.findall(str(soup))[0].replace('\\n','\n')
    return description

def urls_of_description(description):
    return re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', description)

def id_of_video(soup):
    return soup.find("meta",itemprop="videoId")['content']
