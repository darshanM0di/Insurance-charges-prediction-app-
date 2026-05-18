# Insurance Charges Prediction App - Architecture

## System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    STREAMLIT WEB APPLICATION                 │
│                      (Port: 8501)                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────┐    ┌────────────────────────┐ │
│  │    SIDEBAR UI           │    │   MAIN CONTENT AREA    │ │
│  ├─────────────────────────┤    ├────────────────────────┤ │
│  │                         │    │                        │ │
│  │ [Header Image]          │    │ [Header Banner Image]  │ │
│  │                         │    │                        │ │
│  │ ℹ App Info:             │    │ Title:                 │ │
│  │ "App is created for     │    │ Insurance Charges      │ │
│  │  patient hospital       │    │ Prediction App         │ │
│  │  charges"               │    │                        │ │
│  │                         │    │ ┌──────────────────┐  │ │
│  │ [Sidebar Image]         │    │ │ INPUT SECTION    │  │ │
│  │                         │    │ ├──────────────────┤  │ │
│  │ Mode Selector:          │    │ │ Age: [____]      │  │ │
│  │ [Online ▼]              │    │ │ Sex: [Male ▼]    │  │ │
│  │ Options:                │    │ │ BMI: [____]      │  │ │
│  │ • Online                │    │ │ Children: [__▼]  │  │ │
│  │ • Batch                 │    │ │ Smoker: [☐]      │  │ │
│  │                         │    │ │ Region: [NE ▼]   │  │ │
│  │                         │    │ │                  │  │ │
│  │                         │    │ │ [Predict Button] │  │ │
│  │                         │    │ └──────────────────┘  │ │
│  │                         │    │                        │ │
│  │                         │    │ OUTPUT:                │ │
│  │                         │    │ ✓ Predicted charge    │ │
│  │                         │    │   is $12,345.67       │ │
│  │                         │    │                        │ │
│  └─────────────────────────┘    └────────────────────────┘ │
│                                                              │
└──────────────────────────────────────────────────────────────┘
                              ↓
                   ┌──────────────────────┐
                   │  Python Backend      │
                   │  (PyCaret)           │
                   └──────────────────────┘
                              ↓
                   ┌──────────────────────┐
                   │  Loaded ML Model     │
                   │  (insurance.pkl)     │
                   │                      │
                   │  Type: Regression    │
                   │  Framework: PyCaret  │
                   └──────────────────────┘
                              ↓
                   ┌──────────────────────┐
                   │   Prediction Engine  │
                   │                      │
                   │  Input:              │
                   │  • age (int)         │
                   │  • sex (str)         │
                   │  • bmi (float)       │
                   │  • children (int)    │
                   │  • smoker (str)      │
                   │  • region (str)      │
                   │                      │
                   │  Output:             │
                   │  • charges (float)   │
                   └──────────────────────┘
```

---

## Data Flow Diagram

### Online Prediction Flow
```
┌────────────────────────────────────────────────────────────┐
│  USER INPUT (Manual Form Entry)                            │
├────────────────────────────────────────────────────────────┤
│  Age, Sex, BMI, Children, Smoker, Region                   │
└─────────────────────────┬──────────────────────────────────┘
                          ↓
                ┌─────────────────────┐
                │  Create DataFrame   │
                │  [1 row × 6 cols]   │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  PyCaret Model      │
                │  predict_model()    │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  Output DataFrame   │
                │  with prediction    │
                │  _label column      │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  Format & Display   │
                │  ${value:.2f}       │
                └─────────────────────┘
```

### Batch Prediction Flow
```
┌────────────────────────────────────────────────────────────┐
│  USER UPLOAD (CSV File)                                    │
├────────────────────────────────────────────────────────────┤
│  file.csv with: age, sex, bmi, children, smoker, region    │
└─────────────────────────┬──────────────────────────────────┘
                          ↓
                ┌─────────────────────┐
                │  Read CSV with      │
                │  pd.read_csv()      │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  Validate Columns   │
                │  Check Data Types   │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  PyCaret Model      │
                │  predict_model()    │
                │  (all rows)         │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  Output DataFrame   │
                │  all rows + pred    │
                │  _label column      │
                └──────────┬──────────┘
                           ↓
                ┌─────────────────────┐
                │  Display with       │
                │  st.write()         │
                └─────────────────────┘
```

---

## Component Interaction

```
┌─────────────────────────────────────────────────────────────────┐
│                         STREAMLIT (app.py)                       │
│                                                                   │
│  ┌──────────────────┐         ┌──────────────────┐              │
│  │   UI Components  │         │  Business Logic  │              │
│  ├──────────────────┤         ├──────────────────┤              │
│  │ st.image()       │───────→│  Load Images     │              │
│  │ st.selectbox()   │         │  (PIL.Image)     │              │
│  │ st.number_input()│───────→│  Get User Input  │              │
│  │ st.checkbox()    │         │                  │              │
│  │ st.button()      │         │  Create DF       │              │
│  │ st.file_uploader │───────→│  predict()       │              │
│  │ st.write()       │←────────│  Return Results  │              │
│  │ st.success()     │         │                  │              │
│  └──────────────────┘         └────────┬─────────┘              │
│                                        ↓                        │
│                            ┌──────────────────────┐             │
│                            │  PYCARET REGRESSION  │             │
│                            │  Model (insurance)   │             │
│                            │                      │             │
│                            │  predict_model()     │             │
│                            │  load_model()        │             │
│                            └──────────────────────┘             │
│                                        ↓                        │
│                            ┌──────────────────────┐             │
│                            │  MODEL FILE (pkl)    │             │
│                            │  insurance.pkl       │             │
│                            └──────────────────────┘             │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Module Dependencies

```
app.py
├── streamlit (Web UI)
│   ├── st.image()
│   ├── st.sidebar
│   ├── st.selectbox()
│   ├── st.number_input()
│   ├── st.checkbox()
│   ├── st.button()
│   ├── st.file_uploader()
│   ├── st.write()
│   └── st.success()
│
├── pycaret.regression (ML Model)
│   ├── load_model()
│   └── predict_model()
│       ├── numpy (numerical operations)
│       ├── scikit-learn (prediction engine)
│       ├── pandas (dataframe operations)
│       └── scipy (statistical functions)
│
├── PIL (Image Processing)
│   └── Image.open()
│
└── pandas (Data Processing)
    ├── pd.read_csv()
    └── pd.DataFrame()
```

---

## File Organization

```
Project Root
│
├── 📂 insurance_project_pycaret/
│   │
│   ├── app.py                    ⭐ [MAIN APPLICATION]
│   │   ├── Imports all dependencies
│   │   ├── Loads model
│   │   ├── Defines UI components
│   │   ├── Handles online mode
│   │   └── Handles batch mode
│   │
│   ├── insurance.pkl             📊 [ML MODEL]
│   │   └── Trained PyCaret regression model
│   │
│   ├── requirements.txt          📋 [DEPENDENCIES]
│   │   ├── pycaret
│   │   ├── streamlit
│   │   └── pandas
│   │
│   └── README.md                 📖 [DOCUMENTATION]
│
├── image.png                     🖼️ [UI ASSET - HEADER]
├── image.jpeg                    📸 [UI ASSET - SIDEBAR]
├── insurance_charges.csv         📊 [TRAINING DATA]
└── venv/                         🐍 [PYTHON ENVIRONMENT]
```

---

## Request/Response Cycle

### Online Mode
```
User Browser                          Streamlit Server
     │                                       │
     │─── Load app (first time) ────────────→│
     │                                       │
     │←─── Render UI ─────────────────────────│
     │    (images, inputs, buttons)         │
     │                                       │
     │─── Fill form & Click Predict ────────→│
     │                                       │
     │                        (Server processes)
     │                        - Validate input
     │                        - Create DataFrame
     │                        - Load model
     │                        - Generate prediction
     │                        - Format result
     │                                       │
     │←─── Display Prediction ────────────────│
     │    ($XXXX.XX in green box)           │
     │
```

### Batch Mode
```
User Browser                          Streamlit Server
     │                                       │
     │─── Select 'batch' mode ──────────────→│
     │                                       │
     │←─── Show file uploader ───────────────│
     │                                       │
     │─── Upload CSV file ───────────────────→│
     │                                       │
     │─── Click Predict ─────────────────────→│
     │                                       │
     │                        (Server processes)
     │                        - Read CSV
     │                        - Validate columns
     │                        - Load model
     │                        - Predict all rows
     │                        - Create result DF
     │                                       │
     │←─── Display Results Table ────────────│
     │    (all rows with predictions)       │
     │
```

---

## State Management

```
Streamlit Session State
│
├── Model State
│   └── model (loaded once, cached)
│
├── UI State
│   └── add_selectbox (online/batch selection)
│
└── Input State
    ├── Online Mode
    │   ├── age
    │   ├── sex
    │   ├── bmi
    │   ├── children
    │   ├── smoker
    │   └── region
    │
    └── Batch Mode
        └── file_upload (CSV content)
```

---

## Error Handling Flow

```
User Input
     ↓
Validation Check
     ├─ Valid → Process Prediction
     │           ↓
     │        Display Result ✓
     │
     └─ Invalid → Show Error Message
                  ↓
                Display in red/warning
                ↓
                Prompt User to Fix Input
```

---

## Performance Characteristics

```
Operation              Time        Notes
─────────────────────  ──────────  ──────────────────
App Startup            2-5s        Model loading
Page Reload            1-2s        UI rendering
Single Prediction      100-200ms   Fast inference
Batch (1000 rows)      5-10s       Vectorized ops
File Upload            <1s         CSV read
Image Display          <100ms      Cached
```

---

## Security Architecture

```
Data Flow Protection
│
├── Input Validation
│   ├── Age range check (18-100)
│   ├── BMI range check (10-50)
│   ├── Category validation
│   └── CSV structure validation
│
├── Model Security
│   ├── Model file integrity (pkl)
│   ├── Prediction isolation
│   └── No data persistence
│
└── Output Sanitization
    └── Formatted currency display
```

