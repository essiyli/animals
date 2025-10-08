import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns



url = "https://raw.githubusercontent.com/sharmaroshan/Zoo-Dataset/master/zoo.csv"

df = pd.read_csv(url)


st.title("Zoo Dataset Dashboard")
st.write("""
Tämä dashboard havainnollistaa Zoo Datasetin sisältöä.
Data sisältää tietoa 101 eri eläinlajista ja niiden ominaisuuksista, kuten:
onko eläimellä selkäranka, elääkö se vedessä, onko sillä jalat, karvat, pyrstö, jne.

Tavoitteena on tutkia, miten eri ominaisuudet jakautuvat eri eläinluokkiin
(esim. nisäkkäät, linnut, matelijat, kalat, sammakkoeläimet, hyönteiset ja selkärangattomat).
""")

st.header("Datan rakenne")
st.write("Alla näkyvät datan ensimmäiset rivit ja sarakkeiden nimet:")
st.dataframe(df.head())

st.write(f"Rivejä: {df.shape[0]}, Sarakkeita: {df.shape[1]}")
st.write("Sarakkeet:", ", ".join(df.columns))

st.header("Tilastolliset tunnusluvut")
st.write("Numeeristen muuttujien tilastollinen yhteenveto:")
st.write(df.describe())


st.write("""
Tilastollisista tunnusluvuista voidaan havaita esimerkiksi:
- Jalojen määrän keskiarvo on noin 2,3 (koska monet eläimet ovat joko jalattomia tai nelijalkaisia).
- Muut ominaisuudet ovat binäärisiä (0/1), mikä kertoo vain niiden esiintymisestä.
""")


fig1 = plt.figure()
tail_counts = df["tail"].value_counts()
plt.pie(tail_counts.values, labels=["Has a tail", "No tail"], autopct="%.2f%%")
plt.title("Distribution of Animals by Tail Presence")
st.pyplot(fig1)

class_counts = df["class_type"].value_counts()

class_labels = {
    1: "Mammal",
    2: "Bird",
    3: "Reptile",
    4: "Fish",
    5: "Amphibian",
    6: "Insect",
    7: "Invertebrate"
}
labels = [class_labels[i] for i in class_counts.index]
fig2 = plt.figure()
plt.bar(labels, class_counts.values)
plt.title("Number of Animals per Class Type in Zoo Dataset")
plt.xlabel("Animal Class Type")
plt.ylabel("Count")
plt.title("The amount of different animal types")
plt.xticks(rotation=45)
st.pyplot(fig2)

leg_counts = df["legs"].value_counts().sort_index()

fig3 = plt.figure()
plt.plot(leg_counts.index, leg_counts.values, marker="o")
plt.title("Number of Animals per Leg Count")
plt.xlabel("Number of Legs")
plt.ylabel("Count")
st.pyplot(fig3)


fig4 = plt.figure()
df["class_name"] = df["class_type"].map(class_labels)
sns.boxplot(x="class_name", y="legs", data=df)
plt.title("Leg Distribution by Animal Class")
plt.xlabel("Animal Class")
plt.ylabel("Number of Legs")
plt.xticks(rotation=45)
st.pyplot(fig4)

fig5 = plt.figure()
sns.countplot(x="class_name", hue="airborne", data=df)
plt.title("Flying vs Non-Flying Animals by Class")
plt.xlabel("Animal Class")
plt.ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig5)

st.header("Yhteenveto")
st.write("""
Yhteenvetona voidaan todeta, että Zoo-datassa:
- Nisäkkäät muodostavat suurimman eläinluokan.
- Jalkojen määrä vaihtelee luokittain: esim. hyönteisillä useimmiten 6, kaloilla 0.
- Lentokyky on pääasiassa lintujen ominaisuus, mutta esiintyy harvoin muissa luokissa.
""")

