import streamlit as st
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

API_KEY = "8a8943dd03f541cd89607a76224c803a"

lifestyle = {

"Obesity":[
"Walk 10k steps daily",
"Eat high protein meals",
"Avoid sugary drinks",
"Strength training 3x week"
],

"Diabetes":[
"Avoid refined sugar",
"Eat high fiber foods",
"Walk 30 minutes daily",
"Monitor blood sugar"
],

"PCOS":[
"Low GI diet",
"Exercise regularly",
"Avoid processed foods",
"Sleep 7–8 hours"
],

"Hypertension":[
"Reduce salt intake",
"Daily cardio exercise",
"Practice stress management",
"Maintain healthy weight"
],

"High Cholesterol":[
"Eat omega-3 foods",
"Avoid fried foods",
"Increase fiber intake",
"Regular physical activity"
],

"Underweight":[
"Increase calorie intake",
"Eat protein rich foods",
"Strength training",
"Eat frequent meals"
],

"Anemia":[
"Eat iron rich foods",
"Leafy vegetables",
"Vitamin C foods",
"Avoid tea after meals"
],

"Heart Health":[
"Low fat diet",
"Daily walking",
"Maintain healthy BMI",
"Reduce stress"
],

"Digestive Problems":[
"Eat probiotic foods",
"Drink enough water",
"Avoid spicy foods",
"Eat smaller meals"
]
}

data = {
"Age":[20,25,30,35,40,28,32,45],
"BMI":[22,31,28,26,19,34,29,24],
"Problem":[
"Normal",
"Obesity",
"Diabetes",
"Hypertension",
"Underweight",
"Obesity",
"Heart Health",
"Normal"
],
"Diet":[
"Balanced",
"Low Carb",
"Low Sugar",
"Low Sodium",
"High Calorie",
"Low Carb",
"Low Fat",
"Balanced"
]
}

df = pd.DataFrame(data)

le_problem = LabelEncoder()
le_diet = LabelEncoder()

df["Problem"] = le_problem.fit_transform(df["Problem"])
df["Diet"] = le_diet.fit_transform(df["Diet"])

X = df[["Age","BMI","Problem"]]
y = df["Diet"]

model = RandomForestClassifier()
model.fit(X,y)

def get_meals(query):

    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "apiKey":API_KEY,
        "query":query,
        "number":5
    }

    response = requests.get(url,params=params)

    if response.status_code != 200:
        return []

    data = response.json()

    meals = []

    if "results" in data:
        for item in data["results"]:
            meals.append(item["title"])

    return meals

st.markdown("<h1 style='text-align:center; color:#9B59B6;'>NutriBuddy AI</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center;'>AI Health & Diet Dashboard</h4>", unsafe_allow_html=True)

st.write("Enter your details")

age = st.number_input("Age",1,100)
height = st.number_input("Height (cm)",100,220)
weight = st.number_input("Weight (kg)",30,200)

gender = st.selectbox("Gender",["Male","Female"])

problem = st.selectbox(
"Health Problem",
[
"Obesity",
"Diabetes",
"PCOS",
"Hypertension",
"High Cholesterol",
"Underweight",
"Anemia",
"Heart Health",
"Digestive Problems"
]
)

favorite_meal = st.selectbox(
"Favorite Meal",
[
"Chicken",
"Rice",
"Salad",
"Soup",
"Pasta",
"Vegetables",
"Eggs",
"Fish"
]
)

if st.button("Generate Diet Plan"):

    height_m = height/100
    bmi = weight/(height_m**2)


    if gender=="Male":
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:
        bmr = 10*weight + 6.25*height - 5*age - 161

    if bmi<18.5:
        category="Underweight"
    elif bmi<25:
        category="Normal"
    elif bmi<30:
        category="Overweight"
    else:
        category="Obese"

    

    col1, col2, col3 = st.columns(3)

    col1.metric("BMI", round(bmi,2))
    col2.metric("Calories", int(bmr))
    col3.metric("Category", category)


    if problem not in le_problem.classes_:
        problem_encoded = le_problem.transform(["Normal"])[0]
    else:
        problem_encoded = le_problem.transform([problem])[0]

    prediction = model.predict([[age,bmi,problem_encoded]])

    diet_prediction = le_diet.inverse_transform(prediction)

    st.subheader("AI Predicted Diet Type")
    st.write(diet_prediction[0])


    query = diet_prediction[0] + " " + favorite_meal

    meals = get_meals(query)

    st.subheader("Recommended Meals")

    if meals:
        for meal in meals:
            st.write("•",meal)
    else:
        st.write("No meals found")

    

    if problem in lifestyle:

        st.subheader("Lifestyle Advice")

        for tip in lifestyle[problem]:
            st.write("•",tip)

   

    st.subheader("BMI Bar Graph")

    fig1, ax1 = plt.subplots()

    categories = ["Underweight","Normal","Overweight","Obese"]
    values = [0,0,0,0]

    if category=="Underweight":
        values[0]=bmi
    elif category=="Normal":
        values[1]=bmi
    elif category=="Overweight":
        values[2]=bmi
    else:
        values[3]=bmi

    ax1.bar(categories,values)
    ax1.set_title("BMI Category")

    st.pyplot(fig1)

    st.subheader("Daily Calories")

    fig2, ax2 = plt.subplots()

    ax2.bar(["Calories"],[bmr])

    st.pyplot(fig2)

    st.subheader("Weekly Meal Plan")

    for i in range(7):
        meal = meals[i % len(meals)]
        st.write(f"Day {i+1} : {meal}")
    else: 
        st.write("“To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness and maintain an interest in life.” " \
        "– William Londen.")