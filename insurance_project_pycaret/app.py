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
    st.set_page_config(
        page_title='Insurance Charges Prediction',
        page_icon='💊',
        layout='centered',
        initial_sidebar_state='expanded',
    )

    root_dir = os.path.abspath(os.path.join(BASE_DIR, os.pardir))
    assets_dir = os.path.join(root_dir, 'assets')
    header_image = Image.open(os.path.join(assets_dir, 'image.png'))
    sidebar_image = Image.open(os.path.join(assets_dir, 'image.jpeg'))

    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #0d6efd 0%, #20c997 100%); padding: 24px; border-radius: 16px;'>
            <h1 style='color: white; text-align: center; margin: 0;'>Insurance Charges Prediction App</h1>
            <p style='color: #e8f9ff; text-align: center; font-size: 18px; margin: 8px 0 0;'>Predict patient insurance costs with a beautiful, fast, and reliable UI.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.image(header_image, use_column_width=True)
    st.write('### Predict insurance charges using your patient profile or batch data upload')

    st.sidebar.header('Prediction modes')
    st.sidebar.info('Choose online single prediction or batch CSV scoring.')
    st.sidebar.image(sidebar_image, use_column_width=True)

    mode = st.sidebar.selectbox('How would you like to predict?', ('online', 'batch'))

    if mode == 'online':
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input('Age', min_value=18, max_value=100, value=35)
            sex = st.selectbox('Sex', ['male', 'female'])
            bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=28.5, step=0.1)
        with col2:
            children = st.selectbox('Children', list(range(0, 11)))
            smoker = 'yes' if st.checkbox('Smoker') else 'no'
            region = st.selectbox('Region', ['southwest', 'southeast', 'northwest', 'northeast'])

        input_dict = {
            'age': age,
            'sex': sex,
            'bmi': bmi,
            'children': children,
            'smoker': smoker,
            'region': region,
        }
        input_df = pd.DataFrame([input_dict])

        if st.button('Predict'):
            output = predict(MODEL, input_df)
            st.metric(label='Estimated Insurance Charge', value=f'${output:,.2f}')
            st.write('#### Input summary')
            st.table(input_df)
    else:
        file_upload = st.file_uploader('Upload CSV file for predictions', type=['csv'])
        if file_upload is not None:
            input_df = pd.read_csv(file_upload)
            if st.button('Predict'):
                predictions_df = predict_model(MODEL, data=input_df)
                predictions_df['prediction_label'] = predictions_df['prediction_label'].round(2)
                st.success('Batch prediction completed successfully')
                st.write(predictions_df)
                csv_data = predictions_df.to_csv(index=False).encode('utf-8')
                st.download_button('Download predictions', csv_data, 'insurance_predictions.csv', 'text/csv')

if __name__ == '__main__':
    run()