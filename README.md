# Proceso de Desarrollo

## Análisis Inicial

### Exploración del Dataset

Comencé con un análisis exploratorio para entender la estructura del dataset y las variables presentes. Identifiqué valores nulos y realicé limpieza inicial de datos.

### Estadísticas Descriptivas

Utilicé estadísticas descriptivas para analizar las notas finales, notas parciales y scores, explorando sus distribuciones y relaciones.

## Creación de Nuevas Características

### Ingeniería de Características

Agrupé los datos por `user_uuid`, `course_uuid`, y `particion`, creando nuevas variables como medias, medianas y varianzas de las notas. También calculé la frecuencia de tareas y exámenes como características adicionales.

### Análisis de Tendencias

El análisis de tendencias revela que un buen rendimiento durante el curso, medido a través de las notas parciales, el score de tareas y exámenes, está fuertemente asociado con un buen rendimiento en el examen final. Por lo tanto, fomentar un desempeño constante y alto a lo largo del curso puede ser una estrategia efectiva para mejorar los resultados finales de los estudiantes.

## Preparación del Dataset para Modelado

### Selección de Características

Eliminé columnas irrelevantes y seleccioné las nuevas características generadas como variables predictoras. La variable objetivo fue definida como `nota_final_materia`.

### División de Datos

Dividí el dataset en conjuntos de entrenamiento y prueba. Utilicé técnicas de estandarización para asegurar que los datos estuvieran preparados adecuadamente para el modelado.

## Modelado y Comparación de Modelos

### Selección de Modelos

Probé varios modelos incluyendo Decision Tree, Linear Regression, Random Forest y Gradient Boosting para encontrar el más adecuado.

### Evaluación de Modelos

Utilicé métricas como R^2 Score y Mean Squared Error para comparar y seleccionar el mejor modelo basado en su rendimiento.

Model: Decision Tree
Cross-Validated R^2 Score: 0.8884 ± 0.0156

Model: Linear Regression
Cross-Validated R^2 Score: 0.6625 ± 0.0203

Model: Random Forest
Cross-Validated R^2 Score: 0.9049 ± 0.0186

Model: Gradient Boosting
Cross-Validated R^2 Score: 0.8958 ± 0.0124



## Optimización de Hiperparámetros

Implementé Grid Search para ajustar los hiperparámetros del modelo seleccionado y mejorar su capacidad predictiva.

## Selección del Modelo Final

### Modelo Elegido

Decidí utilizar Random Forest debido a su capacidad para manejar datos complejos , reducir el riesgo de overfitting y su buen rendimiento en las métricas evaluadas.

Best Parameters: {'max_depth': 10, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 200}

Mean Squared Error: 0.1385

R^2 Score: 0.9520

### Decisiones Tomadas

- **Selección de Características:** Incluí variables como medias y varianzas de notas debido a su relevancia para predecir la nota final.

- **Elección de Modelos:** Prioricé Random Forest por su capacidad para capturar relaciones complejas y su rendimiento en las métricas seleccionadas.

- **Optimización:** Utilicé Grid Search para encontrar la combinación óptima de hiperparámetros del modelo Random Forest.

- **Evaluación Final:** Verifiqué el rendimiento del modelo en el conjunto de prueba para asegurar su generalización.

# Ejemplos para probar el Endpoint Predict

### Nota más cercana a 8 y a 3:

```json
{
  "nota_parcial_media": 7,
  "nota_parcial_mediana": 8,
  "score_media": 6,
  "score_mediana": 7,
  "frecuencia_tareas": 2,
  "frecuencia_examenes": 2,
  "tiempo_entrega": 11
}



{
  "nota_parcial_media": 2,
  "nota_parcial_mediana": 3,
  "score_media": 2,
  "score_mediana": 2,
  "frecuencia_tareas": 1,
  "frecuencia_examenes": 1,
  "tiempo_entrega": 5
}




