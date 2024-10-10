# Car-Dekho-Price-Prediction
This Project Focuses on Building An Optimized Price Prediction Machine Learning Model for Car Dekho Website and to build an interactive StreamLit based web application for both customers and sales representatives to use seamlessly.

Approach:

1.Convert Unstructured Dataset to Structured Dataset

2.Data Cleaning and Pre-Processing

3.A Detailed Exploratory Data Analysis

4.Model Training and Evaluation

5.Model Selection and Optimisation

6.Building StreamLit Web Application

Project Deliverables:

1.Source code for data preprocessing and model development.

2.Documentation detailing the methodology, models used, and evaluation results.

3.Visualizations and analysis reports derived from the exploratory data analysis.

4.Final predictive model with a user guide.

5.Deployed Streamlit application for price prediction.

6.Should give justification for the method of approach and model selection.

Files Attached: Attached 6 codes(5 .ipynb files and 1 .py file) , 4 Documents as User Guide Documentation(.md) , Raw Unstructured Dataset (6 .xlsx files) and Cleaned Dataset(1.xlsx) included:

1.All Citywise Raw Datasets (6 .xlsx files) and Cleaned Dataset (1 .xlsx file)

2.Source code for Unstructured to Structured Transformation: Unstructured_to_Structured.ipynb

3.Source Code for Data Cleaning: Data_Cleaning.ipynb

4.Source Code for Detailed EDA: EDA_CarDekho.ipynb

5.Source Code for Model Development and Training(Without Outlier Removal): Training_1.ipynb

6.Source Code for Optimized Model Development and Training : Final_ML_Modeling.ipynb

7.Source Code for Streamlit App Creation and Deployment: App.py

8.User Guide for Data Cleaning and Transformation

9.User Guide for EDA

10.User Guide for Machine Learning Model Development 

11.User Guide for StreamLit App Development

Results:

Model Comparison:

![Optimized_Results](https://github.com/user-attachments/assets/53cefdd8-dc3e-41b1-99e2-9c5d441e362d)

TESTING MAE-MSE-R2:

1.Testing MAE:

![Testing_MAE](https://github.com/user-attachments/assets/bb0284f8-0927-4944-84b7-51b8369dee55)

Performance: LightGBM>XGBoost>GradientBoost>CatBoost>RandomBoost

2.Testing MSE:

![Testing_MSE](https://github.com/user-attachments/assets/aae49ceb-3455-415e-99cc-62dd3bf677b4)

Performance: LightGBM>XGBoost>GradientBoost>CatBoost>RandomBoost

3.Testing R2:

![Testing_R2](https://github.com/user-attachments/assets/c10b3f2c-70cb-4fc8-8427-1a614156c19e)

Performance: LightGBM>XGBoost>GradientBoost>CatBoost>RandomBoost

CROSS VALIDATED MAE-MSE-R2:

1.CV MAE:

![CV_MAE](https://github.com/user-attachments/assets/fd078116-eb51-4533-a1ac-f4488e6158fb)

Performance:XGBoost>GradientBoost> LightGBM>CatBoost>RandomBoost

2.CV MSE:

![CV_MSE](https://github.com/user-attachments/assets/6531297e-9582-4e44-89ab-1ab13e9c0cfd)

Performance:XGBoost>GradientBoost> LightGBM>CatBoost>RandomBoost

3.CV R2:

![CV_R2](https://github.com/user-attachments/assets/b333b6cf-c655-4b99-bdd5-ff64f47ce1ce)

Performance:XGBoost>GradientBoost> LightGBM>CatBoost>RandomBoost

Inferences:

1.LightGBM Performs well in testing Data but when cross validated it performs poorly comparatively with XGBoost.

2.XGBoost Algorithm Performs Consistently even after cross validation with Good Results.

Hence XGBoost Algorithm is Selected for Deployment.

Streamlit UI:

1.Welcome Page:

![stwelcome](https://github.com/user-attachments/assets/546175a7-a721-4640-8062-e95499086677)


2.Prediction Page:

![stpredicted](https://github.com/user-attachments/assets/567cd664-e6f5-435d-b6d6-38db059df8fc)

Contact (MailID) : sirpi1996@gmail.com for further queries and details.





