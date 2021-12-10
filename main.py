import streamlit as st
import pymongo

def main():
    #cluster = pymongo.MongoClient("mongodb+srv://"+st.secrets["DB_USER_NAME"] +":"+st.secrets["DB_PASSWORD"]+"@cluster0.lt7mc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    cluster = pymongo.MongoClient("mongodb+srv://yanissimplon:yanissimplon@cluster0.lt7mc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = cluster["Simplon"]
    voiture_base = db["sim"]
    st.title("Recherche :")
    container_voiture = st.container()
    constructeur = voiture_base.distinct("Make")
    select_constructor = st.sidebar.selectbox("Constructeur", constructeur)
    
    with container_voiture :
        if select_constructor:
            select_model = st.sidebar.selectbox("Model", voiture_base.distinct("Model",{"Make": select_constructor}))

        if select_model :
            voiture = voiture_base.find({"Model" : select_model, "Make" : select_constructor}, {})[0]
           
            st.write("La " + voiture["Make"] + " " + voiture["Model"] + " de "+ str(voiture["Year"]),
            " a " + str(voiture["Engine HP"]),
            "chevaux et " + str(voiture["Engine Cylinders"]) + " cylindres. Sa consommation ",
            "sur autoroute est de "+ str(voiture["highway MPG"]) + "L au 100km et de ",
            str(voiture["city mpg"]) +"L au 100km en ville")
        formulaire = st.container()
        with formulaire:
            make = st.text_input("Make")
            model = st.text_input("Model")
            year = st.text_input("Year")
            chev = st.text_input("Engine Cylinders")
            demande = st.button("Nouveau Formulaire")
            if (demande):
                if (make != "" and model != ""):
                    try:
                        y = int(year)
                        c = int(chev)
                        voiture_base.insert_one({"Make" : make, "Model" : model, "Year" : y, "Engine Cylinders": c})
                    except:
                        print("Error Type")
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