```markdown
# VascuSense

Machine learning-based diagnostic tool for vascular health assessment.

## Overview

VascuSense analyzes patient data to classify vascular health status (normal vs. abnormal). The project includes data preprocessing, model training/evaluation, and an interactive web dashboard for result visualization.

## Project Structure

```
VascuSense/
├── my_web_app/
│   ├── dashboard.py
│   └── pages/
├── week_6_roc.py
├── requirements.txt
├── X_train.csv
├── X_test.csv
├── y_train.csv
├── y_test.csv
├── y_pred.csv
└── preprocessed_data.csv
```

## Installation

```bash
git clone https://github.com/Khushipatel5/VascuSense.git
cd VascuSense
pip install -r requirements.txt
```

## Usage

Launch dashboard:
```bash
streamlit run my_web_app/dashboard.py
```

Evaluate model:
```bash
python week_6_roc.py
```

## Tech Stack

- Streamlit
- pandas, numpy
- scikit-learn
- matplotlib, seaborn

## Author

Khushi Patel

## License
'''bash
All rights reserved
'''
