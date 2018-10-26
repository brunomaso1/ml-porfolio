Title: ANÁLISIS DE LAS SOLICITUDES MEDICAS URUGUAY 2016 - RAPIDMINER
Date: 2018-10-25 12:00
Modified: 2018-10-25 12:00
Category: Posts, Rapidminer
Tags: Rapidminer, Solicitudes, Uruguay
Slug: posts/rapidminer/2018/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer
Authors: me
Summary: Análisis de las solicitudes medicas de Uruguay del año 2016.


<br />
<div id="toc_container">
<p class="toc_title">Tabla de contenido</p>
<ul class="toc_list">
	<li><a href="#1-bullet">1. Entendimiento del negocio</a>
        <ul>
            <li><a href="#1.1-bullet">1.1. Contexto</a></li>
            <li><a href="#1.2-bullet">1.2. DataSet</a></li>
            <li><a href="#1.3-bullet">1.3. Objetivo</a></li>
        </ul>
    </li>
    <li><a href="#2-bullet">2. Entendimiento de los datos</a>
        <ul>
            <li><a href="#2.1-bullet">2.1. Atributos</a></li>
            <li><a href="#2.2-bullet">2.2. Análisis de los atributos</a>
                <ul>
                    <li><a href="#2.2.1-bullet">2.2.1. Importancia</a></li>
                </ul>
            </li>
        </ul>
    </li>
	<li><a href="#3-bullet">3. Preparación de los datos</a>
        <ul>
            <li><a href="#3.1-bullet">3.1. Importación de librerías</a></li>
            <li><a href="#3.2-bullet">3.2. Importación de los datos</a></li>
            <li><a href="#3.3-bullet">3.3. Visualización de los datos</a></li>
            <li><a href="#3.4-bullet">3.4. Tratamiento de los datos</a>
                <ul>
                    <li><a href="#3.4.1-bullet">3.4.1. Sanitizar los datos</a></li>
                    <li><a href="#3.4.2-bullet">3.4.2. Tratamiento de outliers</a></li>
                    <li><a href="#3.4.3-bullet">3.4.3. Tratamiento de datos faltantes</a></li>
                    <li><a href="#3.4.4-bullet">3.4.4. Feature extraction</a></li>
                    <li><a href="#3.4.5-bullet">3.4.5. Dimension reduction</a></li>
                    <li><a href="#3.4.6-bullet">3.4.6. Transformaciones de los datos</a></li>
                </ul>
            </li>
        </ul>
    </li>
	<li><a href="#4-bullet">4. Modelado</a>
        <ul>
            <li><a href="#4.1-bullet">4.1. Preparación del modelado</a></li>
            <li><a href="#4.2-bullet">4.2. Entrenamiento de los modelos</a>
                <ul>
                    <li><a href="#4.2.1-bullet">4.2.1. Linear Regression</a></li>
                    <li><a href="#4.2.1-bullet">4.2.2. Linear Regression, L1 Regularization</a></li>
                </ul>
            </li>
            <li><a href="#4.3-bullet">4.3. Comparación de modelos</a></li>
            <li><a href="#4.4-bullet">4.4. Feature selection</a></li>
            <li><a href="#4.5-bullet">4.5. Optimización</a></li>
        </ul>
    </li>
    <li><a href="#5-bullet">5. Evaluación</a></li>
    <li><a href="#6-bullet">6. Puesta en producción</a></li>
</ul>
</div>

## 1. Entendimiento del negocio <a class="anchor" id="1-bullet"></a>
---

<center><small><a href="https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos">https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos</a></small></center>

<div style="text-align:center"><img src="http://www.fnr.gub.uy/sites/all/themes/fnrpb2013/logo.png" alt="drawing" width="60%" height="60%"/></div><br/>

El **Fondo Nacional de Recursos** (FNR) es una institución creada por el decreto *Ley 14.897* con carácter de persona pública no estatal, que brinda cobertura financiera a procedimientos de medicina altamente especializada y a medicamentos de alto precio para toda la población que se radique en el país y que sea usuaria del Sistema Nacional Integrado de Salud.

En el caso de los procedimientos cubiertos estos se efectúan a través de los Institutos de Medicina Altamente Especializada (IMAE) que son prestadores públicos o privados, que cuentan con la habilitación del Ministerio de Salud Pública para su realización.

### 1.1. Contexto <a class="anchor" id="1.1-bullet"></a>

Actualmente, los medicamentos y actos médicos (de alto costo) necesitan una aprobación previa del FNR para su realización, por lo que cada caso es evaluado para luego tomar una decisión si brindar el apoyo económico o no.

<div style="text-align:center"><img src="https://fee.org/media/24118/health-care_mini.jpg?anchor=center&mode=crop&width=1920&rnd=131497055300000000" alt="drawing" width="90%" height="90%"/></div><br/>

### 1.2. DataSet <a class="anchor" id="1.2-bullet"></a>

El conjunto se puede obtener del siguiente link: [Datos](https://catalogodatos.gub.uy/dataset/28b09caf-a138-4942-a597-6c2d0d48c361/resource/ff334d61-a6de-40fe-b663-1cb239443f3c/download/datossolicitudes-2016.csv)

El dataset contiene información de las solicitudes (en Uruguay) de medicamentos de alto costo realizadas al FNR en el año 2016. Este dataset pertenece al gobierno uruguayo y en conjunto con AGESIC (Agencia de Gobierno electrónico y Sociedad de la Información y del Conocimiento) lo han publicado en su página de datos abiertos.

### 1.3. Objetivo <a class="anchor" id="1.3-bullet"></a>

El objetivo en este caso, es predecir si una solicitud de un paciente será APROVADA o NO APROVADA.

En el ámbito de Machine Learning este es un problema supervisado de clasificación binaria.

## 2. Entendimiento de los datos <a class="anchor" id="2-bullet"></a>
---

Antes de comenzar con el análisis y modelado de la solución del problema, debemos entender que explican los atributos.
En este punto se comprenden los atributos y se analiza su importancia para el problema y la solución.

### 2.1. Atributos <a class="anchor" id="2.1-bullet"></a>

Según los [metadatos](https://catalogodatos.gub.uy/dataset/28b09caf-a138-4942-a597-6c2d0d48c361/resource/41f9b26b-4ecc-4802-b0e9-54c6d9f3c2ab/download/metadatosjsonoutput.json) del dataset, el conjunto cuenta con 16 atributos (incluido la variable objetivo o label).

Los atributos y su descripción son:

- ```tipo_prestacion```: Tipo de prestación $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("Acto Médico"; "Inicio de Tratamiento con medicamentos")</span>
- ```area```: Área de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MAC CARDIOLOGÍA"; ACTOS NEFROLOGÍA"; ...)</span>
- ```prestacion_cod```: Código de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("101"; "1201"; ...)</span>
- ```prestacion_desc```: Descripción de la prestación $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("Protesis de rodilla - Implante"; "Cirugía cardíaca adultos"; ...)</span>
- ```fecha_solicitud```: Fecha de solicitud (Date) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("08-11-2016"; "05-08-2016"; ...)</span>
- ```estado_solicitud```: Estado de la solicitud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("AUTORIZADO"; "NO AUTORIZADO")</span>
- ```fecha_autorizacion```: Fecha de autorización (Date) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("08-11-2016"; "05-08-2016"; ...)</span>
- ```Paciente```: Número de paciente (Integer) $\rightarrow$ *Tipo:* <span style="color:orange">**ENTERO**</span>
- ```Edad_años```: Edad en años (Integer) $\rightarrow$ *Tipo:* <span style="color:orange">**ENTERO**</span>
- ```Sexo```: Sexo (String) $\rightarrow$ *Tipo:* <span style="color:orange">**BINOMIAL** ("M"; "F")</span>
- ```Departamento_residencia```: Departamento de residencia del paciente (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MONTEVIDEO"; "FLORES"; ...)</span>
- ```prestador_salud```: Prestador de salud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("CASMU"; "COSEM"; ...)</span>
- ```prestador_departamento```: Departamento del prestador de salud (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("MONTEVIDEO"; "FLORES"; ...)</span>
- ```prestador_tipo```: Tipo de prestador (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("OTRO"; "IMAC"; ...)</span> 
- ```medico_solicitante```: Médico solicitante (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("TOMAS DIESTE FRIEDHEIN"; "BRUNO MASOLLER"; ...)</span>
- ```imae```: IMAE (String) $\rightarrow$ *Tipo:* <span style="color:orange">**POLINOMIAL** ("COMEF"; "CAMOC"; ...)</span>

### 2.2. Análisis de los atributos <a class="anchor" id="2.2-bullet"></a>

En esta sección se hace un análisis previo de los atributos.

#### 2.2.1. Importancia <a class="anchor" id="2.2.1-bullet"></a>

La importancia de los atributos con respecto al contexto es muy importante, ya que atributos que no tienen importancia dado el contexto, pueden afectar la predicción final.

- ```tipo_prestacion``` $\Rightarrow$ El tipo de prestación es un dato importante ya que indica si es un acto médico o un medicamento. <span style="color:green">IMPORTANTE</span>
- ```area``` $\Rightarrow$ El área de prestación es importante, ya que indica el tipo de tratamiento que se ha realizado. <span style="color:green">IMPORTANTE</span>
- ```prestacion_cod``` $\Rightarrow$ El código de prestación es el tipo de tratamiento. <span style="color:green">IMPORTANTE</span>
- ```prestacion_desc``` $\Rightarrow$ Es la descripción de la presentación. Es el mismo atributo que prestacion_cod. <span style="color:red">NO IMPORTANTE</span>
- ```fecha_solicitud``` $\Rightarrow$ Es la fecha de la solicitud, como no estamos tomando en cuenta el tiempo, para este problema no es importante este atributo. <span style="color:red">NO IMPORTANTE</span>
- ```estado_solicitud``` $\Rightarrow$ Es la variable objetivo a predecir en este problema. <span style="color:violet">**IMPORTANTE**</span>
- ```fecha_autorizacion``` $\Rightarrow$ Es la fecha de la autorización, como no estamos tomando en cuenta el tiempo, para este problema no es importante este atributo. <span style="color:red">NO IMPORTANTE</span>
- ```Paciente``` $\Rightarrow$ En este caso, el numero de paciente lo tratamos como un identificador, por lo que para el entrenamiento no es importante. <span style="color:red">NO IMPORTANTE</span>
- ```Edad_años``` $\Rightarrow$ La edad es importante para este problema. <span style="color:green">IMPORTANTE</span>
- ```Sexo``` $\Rightarrow$ ¿Será importante el sexo para decir si autorizar una solicitud? ¿Habrá discriminación de género? XD. <span style="color:green">IMPORTANTE</span>
- ```Departamento_residencia``` $\Rightarrow$ ¿Será importante el departamento de residencia para decir si autorizar una solicitud?. <span style="color:green">IMPORTANTE</span>
- ```prestador_salud``` $\Rightarrow$ Es importante porque este atributo dice de donde viene la solicitud. <span style="color:green">IMPORTANTE</span>
- ```prestador_departamento``` $\Rightarrow$ Es importante porque este atributo dice de que departamento viene la solicitud, lo que no es lo mismo que el departamento de residencia del paciente, aunque pueden estar altamente correlacionados. <span style="color:green">IMPORTANTE</span>
- ```prestador_tipo``` $\Rightarrow$ El tipo de prestador importa, porque no son los mismos las solicitudes privadas que las solicitudes de prestadores públicos. <span style="color:green">IMPORTANTE</span>
- ```medico_solicitante``` $\Rightarrow$ Puede ser que el medico sea importante. <span style="color:green">IMPORTANTE</span>
- ```imae``` $\Rightarrow$ Depende del FNR. <span style="color:green">IMPORTANTE</span>

## 3. Preparación de los datos <a class="anchor" id="3-bullet"></a>

En esta sección se preparan los datos para ser utilizados por varios modelos. Se tiene en cuenta las restricciones de los modelos, por lo que se pueden preparar varios conjuntos para distintos modelos.

Los problemas de este tipo se suelen utilizar modelos que resuelven problemas de clasificación binaria. Los modelos a probar son los siguientes:

- **Algoritmos lineales**:
	- *[Logistic Regression](https://en.wikipedia.org/wiki/Logistic_regression)*
		- Restricciones:
			1. Variable de salida binaria.
			2. Remover el ruido.
			3. Distribución gaussiana de los atributos.
			4. Remover atributos correlacionados.
	- *[Linear Discriminant Analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)*
		- Restricciones:
			1. Variable de salida categórica.
			2. Distribución gaussiana de los atributos.
			3. Remover los outliers.
			4. Misma varianza (estandarizar los datos).
			
- **Algoritmos no lineales**:
	- *[CART](https://en.wikipedia.org/wiki/Decision_tree_learning)*
		- Restricciones:
			1. Sin restricciones.
	- *[Naive Bayes](https://en.wikipedia.org/wiki/Naive_Bayes_classifier)*
		- Restricciones:
			1. Entradas categóricas.
			2. Distribuciones gausianas (para el caso de entradas continuas), se puede utilizar transformaciones o otro kernel.
			3. Variable de salida categórica.
			4. Transformación logarítmica de los datos.
	- *[KNN](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm)*
		- Restricciones:
			1. Re-escalar los datos (normalizar).
			2. Tratamiento de atributos faltantes.
			3. Baja dimensionalidad (se beneficia altamente de poca dimensionalidad, puede ser una opción probar feature selección con este modelo).
	- *[SVM](https://en.wikipedia.org/wiki/Support_vector_machine)*
		- Restricciones:
			1. Atributos numéricos.
	- *[Redes neuronales](https://en.wikipedia.org/wiki/Neural_network)*
		- Restricciones:
			1. Sin restricciones, aunque se sugieren algunas.

- **Ensambles**:
	- *[Random Forest](https://es.wikipedia.org/wiki/Random_forest)*
		- Restricciones:
			1. Sin restricciones.
	- *[Gradient Boosting Trees](https://en.wikipedia.org/wiki/Gradient_boosting)*
		- Restricciones:
			1. Sin restricciones.

### 3.1. Importación de librerías <a class="anchor" id="3.1-bullet"></a>

<div style="text-align:center"><img src="https://1xltkxylmzx3z8gd647akcdvov-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/rapidminer-logo-retina.png" alt="drawing" width="80%" height="80%"/></div><br/>

En este caso, no se importan librerías ya que se usa [Rapidminer](https://rapidminer.com/).

### 3.2. Importación de los datos <a class="anchor" id="3.2-bullet"></a>

Importamos el conjunto dentro de rapidminer (mediante la opcion "Import Data"):

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_1.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez que importamos los datos en rapidminer, seleccionamos el identificador de persona como ID y el atributo *estado_solicitud* como label utilizando el operador ```Set Role```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_2.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Podemos ver, luego que ejecutamos que rapidminer nos identifica el ID y label:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_3.PNG" alt="drawing" width="80%" height="80%"/></div><br/>


### 3.3. Visualización de los datos <a class="anchor" id="3.3-bullet"></a>

Para visualizar los datos podemos utilizar varias de las funciones de Pandas, como lo son:

- ```pd.dataframe.head()```
- ```pd.dataframe.sample(5)```
- ```pd.dataframe.keys()```


```python
# Ver los primeros 5 datos.
data.head()
```


```python
# Ver una muestra aleatoria de 5.
data.sample(5)
```


```python
# Ver los atributos.
data.keys()
```

Podemos ver información sobre el conjunto utilizando ```pd.dataframe.info()```


```python
# Todos los datos.
data.info()
```


```python
# Conjunto de testing.
testing.info()
```

Esta función nos muestra los tipos de datos (enteros, reales, nominales, etc.) y también la cantidad de elementos que tiene el conjunto, así como también cuantos elementos tiene cada atributo.

Como resultado podemos ver que se tienen:

- Enteros $\rightarrow$ 35
- Reales $\rightarrow$ 3
- Nominales $\rightarrow$ 43

Podemos visualizar las estadísticas de los datos con la funcionalidad ```pd.dataframe.describe()``` de Pandas.


```python
# Ver estadísticas simples de los datos.
data.describe()
```

### 3.4. Tratamiento de los datos <a class="anchor" id="3.4-bullet"></a>

En este punto se realizan las transformaciones de los datos que se adecuan a los modelos a utilizar.

#### 3.4.1. Sanitizar los datos <a class="anchor" id="3.4.1-bullet"></a>

La sanitización de los datos se utiliza ya que pueden haber instancias que estén mal, en relación al tipo de dato. Este análisis es más a nivel de negocio que de dato, ya que el negocio implica reglas que los datos deben cumplir.

#### 3.4.2. Tratamiento de outliers <a class="anchor" id="3.4.2-bullet"></a>

Hay muchos modelos en los cuales los outliers reducen la performance o inducen un sesgo indeseado. Por eso, se debe detectar y tratar los outliers para evitar este tipo de problemas.

#### 3.4.3. Tratamiento datos faltantes <a class="anchor" id="3.4.3-bullet"></a>

Los datos faltantes son inadmitibles para muchos modelos. El tratamiento de los datos faltantes implica imputar un valor, eliminar dichos datos o eliminar el atributo.

#### 3.4.4. Feature extraction <a class="anchor" id="3.4.4-bullet"></a>

Muchas veces se puede "diseñar" un atributo que es combinación de otros atributos (lineal o no lineal) para así obtener más información. Tal vez, este atrubto generado es un mejor predictor y se mejora la solución.

#### 3.4.5. Dimension reduction <a class="anchor" id="3.4.5-bullet"></a>

Si las dimensiones son muy grantes, podemos aplicar técnicas que reduzcan la dimensionalidad de los atributos.

#### 3.4.6. Transofrmaciones de los datos <a class="anchor" id="3.4.6-bullet"></a>

En este punto se realizan las transofrmaciones necesarias de los datos. Las transformaciones incluyen desde transformaciones para reducir el sesgo o ajustar distribuciones de los datos hasta transformar los datos a valores numericos o a valores categóricos. También en este punto se incluye la estandarización y normalización si se debe hacer.

## 4. Modelado <a class="anchor" id="4-bullet"></a>
---

En esta sección probamos varios modelos de machine learning. Utilizamos la librería **sklearn**.

Utilizaremos los siguientes modelos:
- ```sklearn.linear_model.LinearRegression``` $\Rightarrow$ http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- ```sklearn.linear_model.LassoCV``` $\Rightarrow$ http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LassoCV.html


```python
# Modelos a utilizar:
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
```

Y para chequear la performance de nuestros modelos utilizamos:
* ```sklearn.metrics.make_scorer``` $\Rightarrow$ http://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html
* ```sklearn.metrics.accuracy_score``` $\Rightarrow$ http://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html
* ```sklearn.model_selection.cross_val_score``` $\Rightarrow$ http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html


```python
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import cross_val_score
```

Utilizaremos ```sklearn.model_selection.GridSearchCV``` (http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) para la optimización del modelo basado en fuerza bruta o ```sklearn-deap.evolutionary_search.EvolutionaryAlgorithmSearchCV``` (https://github.com/rsteca/sklearn-deap) para la optimización del modelo basado en algoritmos evolutivos.


```python
from sklearn.model_selection import GridSearchCV
from evolutionary_search import EvolutionaryAlgorithmSearchCV
```

Utilizaremos ```sklearn.feature_selection.SelectFromModel``` (http://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectFromModel.html#sklearn.feature_selection.SelectFromModel) para la optimización de los parámetros.


```python
from sklearn.feature_selection import SelectFromModel
```

### 4.1. Preparación del modelado <a class="anchor" id="4.1-bullet"></a>

Los conjuntos a utilizar en el modelado son:


```python
print('X_test:', len(X_test))
print('X_train:', len(X_train))
print('y_train:', len(y_train))
```

### 4.2. Entrenamiento de los modelos <a class="anchor" id="4.2-bullet"></a>

En esta sección se entrenan los modelos especificados anteriormente para ver cuál es el que realiza la mejor predicción.

#### 4.2.1. Linear Regression <a class="anchor" id="4.2.1-bullet"></a> 


```python
# Cargamos el modelo.
linreg_clf = LinearRegression()

# Entrenamos el modelo.
linreg_clf.fit(X_train, y_train)

# Validación cruzada.
acc_linreg = cross_val_score(linreg_clf, X_train, y_train, cv=10).mean()
print(acc_linreg)
```

#### 4.2.2. Linear Regression, L1 Regularisation <a class="anchor" id="4.2.2-bullet"></a> 


```python
# Cargamos el modelo.
linl1_clf = LassoCV()

# Entrenamos el modelo.
linl1_clf.fit(X_train, y_train)

# Validación cruzada.
acc_linl1 = cross_val_score(linl1_clf, X_train, y_train, cv=10).mean()
print(acc_linl1)
```

### 4.3. Comparación de modelos <a class="anchor" id="4.3-bullet"></a>

Una vez que tenemos las precisiones de los modelos, podemos comparar las performance de los modelos.


| Modelo              | Performance |
|---------------------|-------------|
| Random Forest       | 84.70       |
| Naive Bayes         | 82.84       |
| Logistic Regression | 80.97       |
| Decision Tree       | 79.85       |
| Linear SVC          | 78.73       |
| SVC                 | 71.73       |
| k-NN                | 61.94       |

### 4.4. Feature selection <a class="anchor" id="4.4-bullet"></a>

Una vez que tenemos el modelo que nos de la mejor predición, realizamos la selección de atributos utilizando algoritmos evolutivos para observar si se mejora en la predicción o no. En si, esto se debería realizar para cada algoritmo, y luego compararlos, pero consume mucho tiempo este tipo de procesos.

### 4.5. Optimización <a class="anchor" id="4.5-bullet"></a>

En esta sección se optimiza el modelo para utilizarlo en la puesta a producción.

## 5. Evaluación <a class="anchor" id="5-bullet"></a>
---

Podemos obtener el proceso entero en el siguiente link:

- [Rapidminer-Process]({filename}/posts/rm-processes/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer.rmp)

## 6. Puesta en producción <a class="anchor" id="6-bullet"></a>
---