import os
import streamlit as st
from pycaret.regression import load_model, predict_model
from PIL import Image
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'insurance')
MODEL = load_model(MODEL_PATH)


def predict(model, input_df):
    predictions_df = predict_model(model, data=input_df)
    prediction_value = predictions_df.iloc[0]['prediction_label']  # just the number
    return prediction_value

def run():
    root_dir = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    assets_dir = os.path.join(root_dir, 'assets')
    i = Image.open(os.path.join(assets_dir, 'image.png'))
    h = Image.open(os.path.join(assets_dir, 'image.jpeg'))

    st.image(i)
    st.sidebar.info('App is created for patient hospital charges')
    st.sidebar.image(h)

    add_selectbox = st.sidebar.selectbox("How would you like to predict?", ('online','batch'))
    st.title('Insurance Charges Prediction App')

    if add_selectbox == 'online':
        age = st.number_input("Age", min_value=18, max_value=100, value=25)
        sex = st.selectbox("Sex", ["male", "female"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=10.0, step=1.0)
        children = st.selectbox("Children", list(range(0, 11)))
        smoker = 'yes' if st.checkbox("Smoker") else 'no'
        region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

        input_dict = {
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region
        }
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(MODEL, input_df)  # use wrapper
            st.success(f'The predicted insurance charge is ${output:.2f}')
    else:
        file_upload = st.file_uploader("Upload CSV file for predictions", type=["csv"])
        if file_upload is not None:
            input_df = pd.read_csv(file_upload)
            if st.button("Predict"):
                predictions_df = predict_model(MODEL, data=input_df)
                st.write(predictions_df)        

if __name__ == '__main__':
    run()