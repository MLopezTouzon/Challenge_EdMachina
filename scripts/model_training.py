import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def preprocess_data(file_path='data/challenge_para_modelo.csv', sep=';'):
    df = pd.read_csv(file_path, sep=sep)
    print(df.columns)  # Imprime las columnas del DataFrame

    # Preparación del dataset
    X = df.drop(columns=[
        'user_uuid', 'course_uuid', 'particion',
        's_created_at', 's_submitted_at', 'nota_final_media',
        'nota_final_mediana', 'nota_final_varianza', 'nota_final_materia'
    ])
    y = df['nota_final_materia']

    # División de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Estandarización
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    # Guardar el scaler
    joblib.dump(scaler, 'models/scaler.pkl')

    return X_train_scaled, X_test_scaled, y_train, y_test


def train_model(X_train_scaled, y_train):
    # Definición del grid de hiperparámetros para Random Forest
    param_grid_rf = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Búsqueda de hiperparámetros
    grid_search_rf = GridSearchCV(RandomForestRegressor(
        random_state=42), param_grid_rf, cv=5, scoring='r2', n_jobs=-1, verbose=2)
    grid_search_rf.fit(X_train_scaled, y_train)

    best_rf = grid_search_rf.best_estimator_

    # Guardar el modelo
    joblib.dump(best_rf, 'models/modelo_random_forest.pkl')

    return best_rf, grid_search_rf


def evaluate_model(model, X_test_scaled, y_test):
    y_pred = model.predict(X_test_scaled)
    mse_test = mean_squared_error(y_test, y_pred)
    r2_test = r2_score(y_test, y_pred)

    print(f"Mean Squared Error (Test): {mse_test:.4f}")
    print(f"R^2 Score (Test): {r2_test:.4f}")


if __name__ == "__main__":
    # Cargar y preparar datos
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data()

    # Entrenar el modelo
    best_rf, grid_search_rf = train_model(X_train_scaled, y_train)

    # Evaluar el modelo
    evaluate_model(best_rf, X_test_scaled, y_test)
