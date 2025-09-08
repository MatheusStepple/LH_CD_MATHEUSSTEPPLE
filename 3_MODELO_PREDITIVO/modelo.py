import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

print("Criando modelo...")

df = pd.read_csv('../desafio_indicium_imdb.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

df['Runtime_numeric'] = df['Runtime'].str.extract('(\d+)').astype(float)
df['Gross_numeric'] = df['Gross'].str.replace(',', '').str.replace('$', '')
df['Gross_numeric'] = pd.to_numeric(df['Gross_numeric'], errors='coerce')
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')

df['Decade'] = (df['Released_Year'] // 10) * 10
df['Is_Recent'] = (df['Released_Year'] >= 2000).astype(int)
df['No_of_Votes_log'] = np.log1p(df['No_of_Votes'])
df['Gross_numeric_log'] = np.log1p(df['Gross_numeric'].fillna(0))

features = ['Runtime_numeric', 'Released_Year', 'Meta_score', 'Decade', 'Is_Recent', 'No_of_Votes_log', 'Gross_numeric_log']
X = df[features].fillna(0)
y = df['IMDB_Rating']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE: {rmse:.3f}")
print(f"R²: {r2:.3f}")

joblib.dump(model, 'modelo_imdb.pkl')
print("Modelo salvo!")

movie = {
    'Series_Title': 'The Shawshank Redemption',
    'Released_Year': 1994,
    'Runtime': '142 min',
    'Meta_score': 80.0,
    'No_of_Votes': 2343110,
    'Gross': '28,341,469'
}

df_test = pd.DataFrame([movie])
df_test['Runtime_numeric'] = df_test['Runtime'].str.extract('(\d+)').astype(float)
df_test['Gross_numeric'] = df_test['Gross'].str.replace(',', '').str.replace('$', '')
df_test['Gross_numeric'] = pd.to_numeric(df_test['Gross_numeric'], errors='coerce')
df_test['Released_Year'] = pd.to_numeric(df_test['Released_Year'], errors='coerce')
df_test['Decade'] = (df_test['Released_Year'] // 10) * 10
df_test['Is_Recent'] = (df_test['Released_Year'] >= 2000).astype(int)
df_test['No_of_Votes_log'] = np.log1p(df_test['No_of_Votes'])
df_test['Gross_numeric_log'] = np.log1p(df_test['Gross_numeric'].fillna(0))

X_test_movie = df_test[features].fillna(0)
prediction = model.predict(X_test_movie)[0]

print(f"Filme: {movie['Series_Title']}")
print(f"Nota Real: 9.3")
print(f"Nota Predita: {prediction:.2f}")
print(f"Erro: {abs(9.3 - prediction):.2f}")

# Feito por Matheus Stepple