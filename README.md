Proceso de Desarrollo
Análisis Inicial:

Exploración del Dataset: Comencé con un análisis exploratorio para comprender la estructura del dataset, las variables presentes y su distribución. Identifiqué valores nulos y la necesidad de limpiar los datos.
Estadísticas Descriptivas: Realicé estadísticas descriptivas para entender mejor las notas finales, notas parciales y scores, y su relación entre sí.
Creación de Nuevas Características:

Ingeniería de Características: Agrupé los datos por user_uuid, course_uuid y particion, creando nuevas variables como medias, medianas y varianzas de las notas, así como la frecuencia de tareas y exámenes.
Análisis de Tendencias: Analicé cómo las notas finales varían a lo largo del tiempo mediante visualizaciones, lo que me ayudó a identificar patrones relevantes.
Preparación del Dataset para Modelado:

Selección de Características: Eliminé columnas irrelevantes y mantuve las nuevas características que podrían impactar el rendimiento del modelo. La variable objetivo fue definida como nota_final_materia.
División de Datos: Dividí el dataset en conjuntos de entrenamiento y prueba para asegurar una evaluación objetiva del modelo.
Modelado y Comparación de Modelos:

Selección de Modelos: Evalué varios modelos (Regresión Logística, Árboles de Decisión, Random Forest, Gradient Boosting) para encontrar el más adecuado para el problema.
Evaluación de Modelos: Utilicé métricas como Accuracy, Precision, Recall, F1 Score, Mean Squared Error y R^2 Score para comparar el rendimiento de cada modelo.
Optimización de Hiperparámetros:

Grid Search: Implementé la búsqueda de hiperparámetros para ajustar los modelos y mejorar su rendimiento, centrándome en la Regresión Logística como modelo final.
Selección del Modelo Final:

Modelo Elegido: Elegí la Regresión Logística por su simplicidad y resultados consistentes, con un R^2 Score alto y un error cuadrático medio bajo en los conjuntos de validación y prueba.
Decisiones Tomadas
Selección de Características: Opté por incluir variables como medias y varianzas de notas, ya que estas aportan información sobre el rendimiento de los estudiantes a lo largo del tiempo, lo que es crucial para predecir la nota final.

Elección de Modelos: La selección de múltiples modelos se basó en la necesidad de comparar enfoques simples y complejos, permitiendo una evaluación exhaustiva. La Regresión Logística fue priorizada por su capacidad de interpretabilidad y eficiencia.

Optimización: La decisión de usar Grid Search para la Regresión Logística fue tomada para maximizar el rendimiento del modelo, garantizando que se consideraran diferentes combinaciones de hiperparámetros.

Evaluación Final: La verificación del rendimiento en el conjunto de prueba fue fundamental para asegurar que el modelo no solo se ajustara bien a los datos de entrenamiento, sino que también tuviera una buena generalización.