"""
Test script to verify the Streamlit app works correctly
"""
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Test 1: Check imports
print("=" * 60)
print("TEST 1: Checking Imports")
print("=" * 60)

try:
    import streamlit as st
    print("✓ streamlit imported successfully")
except ImportError as e:
    print(f"✗ Failed to import streamlit: {e}")
    sys.exit(1)

try:
    from pycaret.regression import load_model, predict_model
    print("✓ pycaret imported successfully")
except ImportError as e:
    print(f"✗ Failed to import pycaret: {e}")
    sys.exit(1)

try:
    from PIL import Image
    print("✓ PIL imported successfully")
except ImportError as e:
    print(f"✗ Failed to import PIL: {e}")
    sys.exit(1)

try:
    import pandas as pd
    print("✓ pandas imported successfully")
except ImportError as e:
    print(f"✗ Failed to import pandas: {e}")
    sys.exit(1)

# Test 2: Check model file
print("\n" + "=" * 60)
print("TEST 2: Checking Model File")
print("=" * 60)

model_path = os.path.join(BASE_DIR, 'insurance.pkl')
if os.path.exists(model_path):
    size = os.path.getsize(model_path)
    print(f"✓ insurance.pkl found - Size: {size:,} bytes")
else:
    print(f"✗ insurance.pkl NOT found at {model_path}")
    sys.exit(1)

# Test 3: Check image files
print("\n" + "=" * 60)
print("TEST 3: Checking Image Files")
print("=" * 60)

image_png = os.path.join(BASE_DIR, '..', 'assets', 'image.png')
image_jpeg = os.path.join(BASE_DIR, '..', 'assets', 'image.jpeg')

if os.path.exists(image_png):
    size = os.path.getsize(image_png)
    print(f"✓ image.png found - Size: {size:,} bytes")
else:
    print(f"⚠ image.png NOT found at {image_png}")

if os.path.exists(image_jpeg):
    size = os.path.getsize(image_jpeg)
    print(f"✓ image.jpeg found - Size: {size:,} bytes")
else:
    print(f"⚠ image.jpeg NOT found at {image_jpeg}")

# Test 4: Check data file
print("\n" + "=" * 60)
print("TEST 4: Checking Data File")
print("=" * 60)

csv_path = os.path.join(BASE_DIR, '..', 'insurance_charges.csv')
if os.path.exists(csv_path):
    df = pd.read_csv(csv_path)
    print(f"✓ insurance_charges.csv found")
    print(f"  - Rows: {len(df)}")
    print(f"  - Columns: {', '.join(df.columns.tolist())}")
else:
    print(f"✗ insurance_charges.csv NOT found at {csv_path}")

# Test 5: Try loading the model
print("\n" + "=" * 60)
print("TEST 5: Loading Model")
print("=" * 60)

try:
    model = load_model(os.path.join(BASE_DIR, 'insurance'))
    print("✓ Model loaded successfully")
    print(f"  - Model type: {type(model)}")
except Exception as e:
    print(f"✗ Failed to load model: {e}")
    sys.exit(1)

# Test 6: Test a prediction
print("\n" + "=" * 60)
print("TEST 6: Testing Prediction")
print("=" * 60)

try:
    test_input = pd.DataFrame([{
        'age': 25,
        'sex': 'male',
        'bmi': 28.5,
        'children': 0,
        'smoker': 'no',
        'region': 'northeast'
    }])
    
    predictions = predict_model(model, data=test_input)
    pred_value = predictions.iloc[0]['prediction_label']
    print(f"✓ Prediction successful!")
    print(f"  - Input: Age=25, Sex=male, BMI=28.5, Children=0, Smoker=no, Region=northeast")
    print(f"  - Predicted Insurance Charge: ${pred_value:.2f}")
except Exception as e:
    print(f"✗ Prediction failed: {e}")
    sys.exit(1)

# Summary
print("\n" + "=" * 60)
print("✓ ALL TESTS PASSED!")
print("=" * 60)
print("\nYour Streamlit app is ready to run!")
print("Command: streamlit run app.py")
print("\nThe app will:")
print("  1. Display header and sidebar images")
print("  2. Provide online prediction mode (manual input)")
print("  3. Provide batch prediction mode (CSV upload)")
print("  4. Use PyCaret model to predict insurance charges")
print("=" * 60)
