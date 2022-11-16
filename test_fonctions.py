import mesfonctions as mf
import requests

class TestClass:
    
    input_file = "input.json"
    url = "https://www.youtube.com/watch?v=OB0QCHxzl1s"
    response = requests.get(url)
    soup = mf.BeautifulSoup(response.text, "html.parser")
    
    def test_json_to_dataframe(self):
        df_function = mf.json_to_dataframe(self.input_file)
        assert df_function.loc[0,"videos_id"] == "fmsoym8I-3o"
        assert df_function.loc[1,"videos_id"] == "LOO3xyFijDk"
    
    def test_title_of_video(self):
        title_function = mf.title_of_video(self.soup)
        assert title_function == "Dragon Ball Z Budokai 3 Theme Song Japanese Version"
        
    def test_name_of_author(self):
        name_function = mf.name_of_author(self.soup)
        assert name_function == "TheRedGeneration"
    
    def test_number_of_likes(self):
        likes_function = mf.number_of_likes(self.soup)
        assert likes_function == "2 760"
    
    def test_description_of_video(self):
        description_function = mf.description_of_video(self.soup)
        assert description_function[0] == "D"
        assert description_function[len(description_function)-1] == "!"
        assert description_function[len(description_function)-2] == "e"
        
    def test_urls_of_description(self):
        description_function = mf.description_of_video(self.soup)
        urls_function = mf.urls_of_description(description_function)
        assert urls_function == []
        
    def test_id_of_video(self):
        id_function = mf.id_of_video(self.soup)
        assert id_function == "OB0QCHxzl1s"    
        