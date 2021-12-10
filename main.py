import streamlit as st
import pymongo


def get_list_constructor(voiture_base):
    liste = []
    for constructor in voiture_base.find({}, {"_id" : 0, "Make": 1}):
        try:
            liste.index(constructor["Make"])
        except:
            liste.append(constructor["Make"])
    return (liste)

def get_list_model(voiture_base, constructor):
    liste = []
    for voiture in voiture_base.find({"Make" : constructor}, {"_id" : 0, "Model": 1}):
        try:
            liste.index(constructor["Model"])
        except:
            liste.append(constructor["Model"])
    return (liste)

#for voiture in voiture_base.find({"Make" : "BMW"}, {"_id" : 0, "Model": 1}):
def main():
    cluster = pymongo.MongoClient("mongodb+srv://"+st.secrets["DB_USER_NAME"] +":"+st.secrets["DB_PASSWORD"]+"@cluster0.lt7mc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    #cluster = pymongo.MongoClient("mongodb+srv://yanissimplon:yanissimplon@cluster0.lt7mc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Simplon"]
    voiture_base = db["sim"]
    st.title("Recherche :")
    container_voiture = st.container()
    constructeur = get_list_constructor(voiture_base)
    constructor = st.sidebar.selectbox("Constructeur", constructeur)
    model = st.sidebar.selectbox("Model", {})
    with container_voiture :
        button_Voiture = st.sidebar.button("Voiture")
        if(button_Voiture):
            st.write([voiture for voiture in voiture_base.find({}, {"_id" : 0})])
    with constructor:
        pass
        #model = st.sidebar.selectbox("Model", get_list_model(constructor))

main()

#   list_type_movie = list_type(movie)
#         multi_select_movie = st.sidebar.multiselect('Genre Film',
#                                            list_type_movie)
#         research_title_movie = st.sidebar.text_input("Recherche titre film")
#         research_actor_movie = st.sidebar.text_input("Recherche acteur film")
#         note_movie = st.sidebar.slider('Note film', 0, 10, 0)
#         time_movie = st.sidebar.slider('temps film en minute', 0, 360, 360)
#         button_research_movie = st.sidebar.button("Recherche film")
        
#         if (button_movie):
#             container_movie.dataframe(movie)
#         if (button_research_movie):
#             research_movie = search(multi_select_movie ,research_title_movie, research_actor_movie , movie, float(note_movie), time_movie)
#             container_movie.dataframe(research_movie)