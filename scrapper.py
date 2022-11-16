#!/usr/bin/python

import requests
import argparse
import mesfonctions as mf

def main():
    
    # On récupère le nom des fichiers input et output
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', action='store', dest="inputfile", required=True)
    parser.add_argument('--output', action='store', dest="outputfile", required=True)
    args = parser.parse_args()
    
    # On lit le fichier json des IDs vidéos youtube et on structure le dataframe
    videosID = mf.json_to_dataframe(args.inputfile)
    videosID['title'] = 0
    videosID['author'] = 0
    videosID['likes'] = 0
    videosID['description'] = 0
    videosID['urls_descr'] = 0
    videosID['id_video'] = 0
    
    for i in range(len(videosID)):
        
        # Parcours des IDs vidéos
        id = videosID.loc[i,"videos_id"]
        
        # On récupère le code HTML de la page Youtube
        url = "https://www.youtube.com/watch?v="+id
        response = requests.get(url)
        soup = mf.BeautifulSoup(response.text, "html.parser")

        # Titre de la vidéo Youtube
        titre = mf.title_of_video(soup)
        print("Le titre de la vidéo Youtube est "+titre+"\n")
        videosID.loc[i,"title"] = titre
    
        # Nom du vidéaste
        author = soup.find("link",{'itemprop':'name'})["content"]
        print("Le nom du vidéaste est "+author+"\n")
        videosID.loc[i,"author"] = author
        
        # Nombre de pouces bleu
        likes = mf.number_of_likes(soup)
        print("Il y a eu "+likes+"\n")
        videosID.loc[i,"likes"] = likes

        # Description de la vidéo
        description = mf.description_of_video(soup)
        print("Description de la vidéo : "+description+"\n")
        videosID.loc[i,"description"] = description

        
        # Liens de la description
        urls = mf.urls_of_description(description)
        links = ""
        print("Les liens de la description : ", urls, "\n")
        for v in urls: links += v+", "
        videosID.loc[i,"urls_descr"] = links
        
        # L'ID de la vidéo
        id = mf.id_of_video(soup)
        print("L'ID de la vidéo youtube : "+id+"\n")
        videosID.loc[i,"id_video"] = id
        
        # Les n premiers commentaires
    
    print(videosID.head())
    videosID.to_json(args.outputfile)

    
    
    
    
    
main()
    

    