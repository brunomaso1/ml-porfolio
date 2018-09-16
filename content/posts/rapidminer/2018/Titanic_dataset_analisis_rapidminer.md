Title: ANÁLISIS DEL DATASET TITANIC - RAPIDMINER
Date: 2018-08-30 12:00
Modified: 2018-08-30 12:00
Category: Posts, Rapidminer
Tags: Rapidminer, Titanic
Slug: posts/rapidminer/2018/Titanic_dataset_analisis_rapidminer
Authors: me
Summary: Análisis de los datos del Titanic para luego ser procesados por un modelo de ML.

<br />
<div id="toc_container">
<p class="toc_title">Tabla de contenido</p>
<ul class="toc_list">
	<li><a href="#1-bullet">1. Entendimiento del negocio</a></li>
	<li><a href="#2-bullet">2. Preparación de los datos</a>
		<ul>
			<li><a href="#2.1-bullet">2.1. Importaciones</a></li>
			<li><a href="#2.2-bullet">2.2. Cargar los datos</a></li>
			<li><a href="#2.3-bullet">2.3. Tratamiento de los datos</a>
				<ul>
					<li><a href="#2.3.1-bullet">2.3.1. Chequear valores faltantes</a></li>
					<li><a href="#2.3.2-bullet">2.3.2. Eliminar faltantes</a></li>
					<li><a href="#2.3.3-bullet">2.3.3. Imputar faltantes</a></li>
				</ul>
			</li>
			<li><a href="#2.4-bullet">2.4. Visualización de los datos</a></li>
			<li><a href="#2.5-bullet">2.5. Feature Engineering (Ingeniería de Características)</a></li>
		</ul>
	</li>
	<li><a href="#3-bullet">3. Modelado</a>
		<ul>
			<li><a href="#3.1-bullet">3.1. Preparación del modelado</a></li>
			<li><a href="#3.2-bullet">3.2. Entrenamiento de los modelos</a>
				<ul>
					<li><a href="#3.2.1-bullet">3.2.1. SVC</a></li>
					<li><a href="#3.2.2-bullet">3.2.2. Linear SVC</a></li>
					<li><a href="#3.2.3-bullet">3.2.3. Random Forest</a></li>
					<li><a href="#3.2.4-bullet">3.2.4. Logistic Regression</a></li>
					<li><a href="#3.2.5-bullet">3.2.5. KNeighbors</a></li>
					<li><a href="#3.2.6-bullet">3.2.6. GaussianNB</a></li>
					<li><a href="#3.2.7-bullet">3.2.7. DecisionTree</a></li>
				</ul>
			</li>
			<li><a href="#3.3-bullet">3.3. Comparación de modelos</a></li>
		</ul>
	</li>
	<li><a href="#4-bullet">4. Evaluación</a></li>
</ul>
</div>

## Entendimiento del negocio <a class="anchor" id="1-bullet"></a>
---

[Entendimiento del negocio: ANÁLISIS DEL DATASET "TITANIC" - PYTHON]({filename}/posts/jupyter-notebooks/2018/Correlación_de_atributos_python.ipynb#1-bullet)

## Preparación de los datos <a class="anchor" id="2-bullet"></a>
---

### Importaciones <a class="anchor" id="2.1-bullet"></a>

En Rapidminer no precisamos importar librerías, en este punto solamente abrimos la herramienta.

### Cargar los datos <a class="anchor" id="2.2-bullet"></a>

Para cargar los datos en Rapidminer, lo realizamos dinámicamente porque así nos queda la ruta relativa a donde tenemos el conjunto de datos. La carga dinámica puede ser incluso a través de una URL.
Para cargar dinámicamente los datos utilizamos el bloque ```Read CSV```. Y en parámetro *colum separators* ponemos una "," (esto indica que el archivo viene separado por comas).
Abrimos ambos conjuntos, el de test y el de training.

- Test $\Rightarrow$ **../../post-datasets/titanic_raw_test.csv**
- Train $\Rightarrow$ **../../post-datasets/titanic_raw_train.csv**

Cada vez que ejecutemos, Rapidminer va a ir a buscar los datos a la dirección del archivo.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_1.PNG" alt="drawing" width="12%" height="12%"/></div>
<br/>

Una vez que corremos el proceso (F11), podemos ver que los datos se han cargado correctamente.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_2.PNG" alt="drawing" width="80%" height="80%"/></div>
<br/>

Para obtener estadísticas, simplemente cambiamos a la pestaña "Statistics".
En esta pestaña podemos ver todos los datos estadísticos de los atributos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_3.PNG" alt="drawing" width="80%" height="80%"/></div>
<br/>

### Tratamiento de los datos <a class="anchor" id="2.3-bullet"></a>

#### Chequear valores faltantes <a class="anchor" id="2.3.1-bullet"></a>

Para chequear los valores faltantes en Rapidminer, en la pestaña de estadísticas, nos podemos fijar en el campo "Average".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_4.PNG" alt="drawing" width="80%" height="80%"/></div>
<br/>

#### Eliminar faltantes <a class="anchor" id="2.3.2-bullet"></a>

En este caso podemos ver que hay muchos atributos faltantes en edad y cabina. En este contexto:

- Edad es muy importante y no lo podemos eliminar.
- Cabina si la podemos eliminar, ya que no aporta información relevante sobre el problema.
- Tampoco lo aporta ticket, así que lo eliminamos también.

Para eliminar las columnas, podemos utilizar el bloque ```Select Attributes```, en el parámetro *attribute filter type* seleccionamos "subset", seleccionamos *"Cabin"* y *"Ticket"* en el combo-box y chequeamos el parámetro *invert selection*. Esto eliminará solamente las columnas "Cabin" y "Ticket" de nuestro conjunto.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_5.PNG" alt="drawing" width="25%" height="25%"/></div>
<br/>

Una vez que ejecutamos, podemos ver que ambos atributos han sido sacados.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_6.PNG" alt="drawing" width="80%" height="80%"/></div>
<br/>

#### Imputar faltantes <a class="anchor" id="2.3.3-bullet"></a>

Como la edad es muy importante para eliminar, tenemos que decidir por que valor sustituir. Para eso podemos ver la grafica para saber la distribución que siguen los datos sin dichos atributos faltantes.
Primeramente utilizamos el bloque ```Filter Examples```, seleccionamos el parámetro *condition class* a "no_missing_attributes" y ejecutamos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_7.PNG" alt="drawing" width="30%" height="30%"/></div>
<br/>

Podemos ver que se han filtrado los atritubos faltantes.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_8.PNG" alt="drawing" width="80%" height="80%"/></div>
<br/>

Como podemos ver, los datos tienen una distribución cuasi-normal, por lo tanto, podemos sustituir los faltantes por la media. Para sustituir los faltantes, podemos utilizar el bloque ```Replace Missing Values```. Seleccionamos el parámetro *attribute filter type* en "single", ingresamos el valor "Age" y dejamos el valor por defecto en "average" para el parámetro *default*.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_9.PNG" alt="drawing" width="30%" height="30%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_10.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Como podemos ver, ahora no hay atributos faltantes.
También realizamos lo mismo con el atributo "Embarked" y "Fare" (el conjunto de testing tiene algunas instancias de "Fare" vacías).

### Visualizacion de los datos <a class="anchor" id="2.4-bullet"></a>

Para visualizar relaciones, utilizamos graficas especificas para cada caso. Por ejemplo, podemos graficar el sexo en función de la variable objetivo para ver si existe alguna relación.
Para esto, conectamos la salida del bloque ```Replace Missing Values``` a un bloque ```Filter Examples```, seleccionamos el parámetro *condition class* a "custom_filters" y filtramos la con la siguiente regla: "Survived=1". Este filtrado nos dará todas las instancias donde "Survived=1", o sea, todas las personas que han sobrevivido. 
Luego que filtramos y corremos el proceso, vamos a la pestaña "Charts" y seleccionamos los siguientes parámetros:

- *Chart Style* $\rightarrow$ "Bars".
- *Group-By Column* $\rightarrow$ "None".
- *Legend Column* $\rightarrow$ "Sex".
- *Value Column* $\rightarrow$ "Survived".
- *Aggregation* $\rightarrow$ "count".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_11.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Resumen de datos:

- El total de personas que sobrevivieron es: 342
	- Mujeres: 0.6812865497076024
	- Hombres: 0.31871345029239767

Podemos ver que el sexo es un atributo importante para la predicción.
Ahora chequearemos si la clase también es importante.
Para esto, realizamos el mismo procedimiento.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_12.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Resumen de datos:

- El total de personas que sobrevivieron es: 342
	- Clase 1: 0.39766081871345027
	- Clase 2: 0.2543859649122807
	- Clase 3: 0.347953216374269

Como ya estamos filtrando por las personas que sobrevivieron, para relacionar ambos atributos, simplemente seleccionamos los siguientes parámetros:

- *Chart Style* $\rightarrow$ "Bars".
- *Group-By Column* $\rightarrow$ "None".
- *Legend Column* $\rightarrow$ "Sex".
- *Value Column* $\rightarrow$ "PClass".
- *Aggregation* $\rightarrow$ "count".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_13.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

También lo podemos hacer de forma inversa, o sea, la clase en función del sexo.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_14.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En los ejemplos podemos ver que tanto el sexo como la clase son importantes. Si eras de clase 1, tenias mas probabilidad de salvarte que si fueras de alguna otra clase.
Podemos realizar el mismo análisis sobre el atributo "Age".
En este caso también queremos analizar los que no sobrevivieron, para esto conectamos la salida del resto del bloque ```Filter Examples```, lo cual nos devuelve los que no sobrevivieron ("Survived=0").

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_15.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez corremos el proceso, podemos fijarnos en ambos gráficos según la salida.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_16.PNG" alt="drawing" width="80%" height="80%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_17.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Podemos utilizar un "stripplot" para ver la distribución de los datos. Por ejemplo, para ver la distribución de los que sobrevivieron con respecto a la edad.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_18.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Podemos ver que los pasajeros jovenes tenian mas posibilidades de salvarse.
También Rapidminer nos brinda una matriz para ver todos los gráficos juntos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_19.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

### Feature Engineering (Ingeniería de Características)  <a class="anchor" id="2.5-bullet"></a>

Como sexo y embarcación son atributos categóricos, los tenemos que pasar a números, ya que varios algoritmos utilizan los atributos en números. Para esto utilizamos el bloque  ```Nominal to Numeric```.
Para esto seleccionamos los siguientes parámetros en el bloque:

- *Attribute filter type* $\rightarrow$ "single".
- *attribute* $\rightarrow$ "Name".
- *invert selection* $\rightarrow$ "Checked".
- *coding type* $\rightarrow$ "unique integers".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_20.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

Con estos parámetros, el bloque transformará todos los atributos a enteros, asignandole un valor a cada clase. Por ejemplo male=1 y female=0.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_21.PNG" alt="drawing" width="50%" height="50%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_22.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

También podemos combinar el atributo SibSp y Parch, para saber cuan grande es la familia. Para esto utilizamos el bloque ```Generate Attributes```. Concetamos la salida del bloque ```Nominal to Numeric``` al bloque ```Generate Attributes``` y seteamos los parámetros de éste bloque con los siguientes valores:

- *function descriptions*:
	- *attribute name* $\rightarrow$ "FamSize".
	- *function expressions* $\rightarrow$ "SibSp + Parch + 1".
	
Esta unión de los atributos (con el objetivo de encontrar un atributo que clasifique mejor las instancias o reducir la complejidad) la podemos hacer ya que tenemos un entendimiento claro del negocio. Sin embargo, no siempre la podemos hacer si no entendemos bien el negocio. Podríamos estar introduciendo un error en el modelo.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_23.PNG" alt="drawing" width="50%" height="50%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_24.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

Otro atributo interesante, es saber si se estaba solo o no. Podemos aplicar el mismo bloque con este objetivo con los siguientes parámetros:

- *function descriptions*:
	- *attribute name* $\rightarrow$ "IsAlone".
	- *function expressions* $\rightarrow$ "if(FamSize, 1, 0)".
	
<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_25.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

Una característica que en principio no parece importante es el nombre, pero de éste podemos extraer información. Utilizando los indicadores de la persona podemos deducir su estatus en la sociedad. Por ejemplo: Señor, Señora, Señorita, etc.
Utilizamos el bloque ```Generate Extract``` (este bloque es hecho por la comunidad, pero Rapidminer una vez que se da cuenta que no se encuentra, nos pregunta si lo deseamos bajar), que utiliza una expresión regular para, de un atributo, generar otro.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_26.PNG" alt="drawing" width="60%" height="60%"/></div><br/>

Para generar el atributo, seleccionamos los siguientes parámetros:

- *source attribute* $\rightarrow$ "Name".
- *query type* $\rightarrow$ "Regular Expression".
- *regular expression queries*:
	- *attribute name* $\rightarrow$ "Title".
	- *query expression* $\rightarrow$ "([A-Za-z]+)\."
	
De este modo obtenemos el siguiente resultado.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_27.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

## Modelado <a class="anchor" id="3-bullet"></a>
---

En esta sección probamos varios modelos de machine learning.
Utilizaremos los siguientes modelos de Rapidminer:

- ```Support Vector Machine``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/support_vector_machines/support_vector_machine_libsvm.html)
- ```Random Forest``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_random_forest.html)
- ```Logistic Regression``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/logistic_regression/logistic_regression.html)
- ```k-NN``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/lazy/k_nn.html)
- ```Naive Bayes``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/bayesian/naive_bayes.html)
- ```Decision Tree``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_decision_tree.html)

Y para chequear la performance de nuestros modelos utilizamos:

- ```Apply Model``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/scoring/apply_model.html)
- ```Performance``` $\Rightarrow$ (https://docs.rapidminer.com/latest/studio/operators/validation/performance/performance.html)

Utilizaremos el bloque ```Cross Validation``` para realizar validación cruzada.

### Preparación del modelado <a class="anchor" id="3.1-bullet"></a>

Ahora debemos definir los atributos que utilizaremos para entrenar. O sea, que atributos son importantes para el contexto del problema. Por ejemplo, sabemos que el nombre no es importante para el contexto del problema (en si, no era importante, pero nos sirvió para obtener un mejor atributo ("Title") a partir del nombre). También definimos la variable objetivo mediante el bloque ```Set role```.
Inicialmente aplicamos todas las transformaciones de los datos, lo cual incluye las transformaciones anteriores y eliminar en nombre. Para esto creamos un subproceso y lo aplicamos a los datos de entrenamiento. Cuando vayamos a realizar las predicciones, también tendríamos que aplicar este subproceso a los datos a predecir.
Rapidminer nos permite, mediante el bloque ```Split Validation```, crear el conjunto de test automáticamente, por lo que no necesitamos dividir los datos entre entrenamiento y test manualmente.
El proceso quedaría de la siguiente forma:

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_28.PNG" alt="drawing" width="80%" height="80%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_29.PNG" alt="drawing" width="60%" height="60%"/></div><br/>

### Entrenamiento de los modelos <a class="anchor" id="3.2-bullet"></a>

En esta sección se entrenan los modelos especificados anteriormente para ver cual es el que realiza la mejor predicción.
El proceso es el siguiente:

1. Se transforman los datos (subproceso creado anteriormente).
2. Se ejecuta el modelo dentro del bloque de ```Split Validation```.
3. Se valida la performance dentro del bloque también.
4. Se muestra la performance.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_30.PNG" alt="drawing" width="70%" height="70%"/></div><br/>

#### SVC <a class="anchor" id="3.2.1-bullet"></a>

Perfomance: **71.73%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_31.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### Linear SVC <a class="anchor" id="3.2.2-bullet"></a>

Perfomance: **78.73%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_32.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### Random Forest <a class="anchor" id="3.2.3-bullet"></a> 

Perfomance: **84.70%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_33.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### Logistic Regression <a class="anchor" id="3.2.4-bullet"></a> 

Perfomance: **80.97%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_34.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### KNeighbors <a class="anchor" id="3.2.5-bullet"></a> 

Perfomance: **61.94%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_35.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### GaussianNB <a class="anchor" id="3.2.6-bullet"></a>

Perfomance: **82.84%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_36.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

#### DecisionTree <a class="anchor" id="3.2.7-bullet"></a>

Perfomance: **79.85%**

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_37.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

### Comparación de modelos <a class="anchor" id="3.3-bullet"></a>

Podemos ver que el modelo de mejor performance es Random Forest:

| Modelo              | Performance |
|---------------------|-------------|
| Random Forest       | 84.70       |
| Naive Bayes         | 82.84       |
| Logistic Regression | 80.97       |
| Decision Tree       | 79.85       |
| Linear SVC          | 78.73       |
| SVC                 | 71.73       |
| k-NN                | 61.94       |

### Mejorar los parametros del mejor modelo <a class="anchor" id="3.4-bullet"></a>

En los modelos paramétricos (los modelos anteriores) se realizan varias suposiciones en la función a predecir. Por ejemplo, en los modelos lineales se asume que existe una función lineal que logra separar correctamente las instancias, o sea, que los datos siguen una distribución lineal.
En este tipo de modelos, no se trata de aprender la función en sí (o sea, la relación de los datos) sino más bien se trata de aprender cuales son los mejores coeficientes para dichos modelos.
En este sentido, podemos optimizar dichos parámetros para un mejor rendimiento del modelo. Como Random Forest es el que mejor predicción nos proporciona, lo elegimos a éste para optimizar sus parámetros.
*Nota: También se puede optimizar los parámetros de cada modelo y luego compararlos, sería algo más lógico, pero el costo computacional crece mucho.*
La optimización en Rapidminer se puede realizar mediante el bloque ```Optimize Parameters (Grid)```. Este optimizador buscará la mejor configuración de los parámetros.
Una vez que incluimos el bloque, ponemos el modelo dentro del bloque, ejecutamos el optimizador y podemos ver que la performance ha mejorado.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_38.PNG" alt="drawing" width="60%" height="60%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_39.PNG" alt="drawing" width="40%" height="40%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_40.PNG" alt="drawing" width="70%" height="70%"/></div><br/>

## Evaluación <a class="anchor" id="4-bullet"></a>
---

Podemos obtener el proceso entero en el siguiente link:

- [Rapidminer-Process]({filename}/posts/rm-processes/analisis_del_dataset_titanic-rapidminer.rmp)