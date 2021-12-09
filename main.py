import streamlit as st
import pymongo




def main():
    # cluster = pymongo.MongoClient("mongodb+srv://"+ st.secrets["DB_USER_NAME"] +":"+st.secrets["DB_PASSWORD "]+"@cluster0.lt7mc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    # db = cluster["Simplon"]
    # voiture_base = db["sim"]
    st.title("Recherche :")
    container_voiture = st.container()
    with container_voiture :
        button_Voiture = st.sidebar.button("Voiture")
        if(button_Voiture):
            pass



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