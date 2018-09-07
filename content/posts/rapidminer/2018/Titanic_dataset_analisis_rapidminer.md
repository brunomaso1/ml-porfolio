Title: ANÁLISIS DEL DATASET "TITANIC" - RAPIDMINER
Date: 2018-08-30 12:00
Modified: 2018-08-30 12:00
Category: Rapidminer
Tags: crisp-dm, process, models, algorithms
Slug: posts/rapidminer/2018/Titanic_dataset_analisis_rapidminer
Authors: Bruno Masoller
Summary: Analisis de los datos del titanic para luego ser procesados por un modelo de ML.

## Tabla de contenido:
1. [Entendimiento del negocio](#1-bullet)
2. [Preparación de los datos](#2-bullet)
    1. [Importaciones](#2.1-bullet)
    2. [Cargar los datos](#2.2-bullet)
    3. [Tratamiento de los datos](#2.3-bullet)
        1. [Chequear valores faltantes](#2.3.1-bullet)
        2. [Eliminar faltantes](#2.3.2-bullet)
        3. [Imputar faltantes](#2.3.3-bullet)
    4. [Visualizacion de los datos](#2.4-bullet)
    5. [Feature Engineering (Ingeniería de Características)](#2.5-bullet)
3. [Modelado](#3-bullet)
    1. [Preparación del modelado](#3.1-bullet)
    2. [Entrenamiento de los modelos](#3.2-bullet)
        1. [SVC](#3.2.1-bullet)
        2. [Linear SVC](#3.2.2-bullet)
        3. [Random Forest](#3.2.3-bullet)
        4. [Logistic Regression](#3.2.4-bullet)
        5. [KNeighbors](#3.2.5-bullet)
        6. [GaussianNB](#3.2.6-bullet)
        7. [DecisionTree](#3.2.7-bullet)
    3. [Comparación de modelos]((#3.3-bullet))
4. [Evaluación](#4-bullet)

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

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_1.PNG" alt="drawing" width="10%" height="10%"/></div>

Una vez que corremos el proceso (F11), podemos ver que los datos se han cargado correctamente.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_2.PNG" alt="drawing" width="80%" height="80%"/></div>

Para obtener estadísticas, simplemente cambiamos a la pestaña "Statistics".
En esta pestaña podemos ver todos los datos estadísticos de los atributos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_3.PNG" alt="drawing" width="80%" height="80%"/></div>

### Tratamiento de los datos <a class="anchor" id="2.3-bullet"></a>

#### Chequear valores faltantes <a class="anchor" id="2.3.1-bullet"></a>

Para chequear los valores faltantes en Rapidminer, en la pestaña de estadísticas, nos podemos fijar en el campo "Average".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_4.PNG" alt="drawing" width="80%" height="80%"/></div>

#### Eliminar faltantes <a class="anchor" id="2.3.2-bullet"></a>

En este caso podemos ver que hay muchos atributos faltantes en edad y cabina. En este contexto:

- Edad es muy importante y no lo podemos eliminar.
- Cabina si la podemos eliminar, ya que no aporta información relevante sobre el problema.
- Tampoco lo aporta ticket, así que lo eliminamos también.

Para eliminar las columnas, podemos utilizar el bloque ```Select Attributes```, en el parámetro *attribute filter type* seleccionamos "subset", seleccionamos *"Cabin"* y *"Ticket"* en el combo-box y chequeamos el parámetro *invert selection*. Esto eliminará solamente las columnas "Cabin" y "Ticket" de nuestro conjunto.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_5.PNG" alt="drawing" width="30%" height="30%"/></div>

Una vez que ejecutamos, podemos ver que ambos atributos han sido sacados.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_6.PNG" alt="drawing" width="80%" height="80%"/></div>

#### Imputar faltantes <a class="anchor" id="2.3.3-bullet"></a>

Como la edad es muy importante para eliminar, tenemos que decidir por que valor sustituir. Para eso podemos ver la grafica para saber la distribución que siguen los datos sin dichos atributos faltantes.
Primeramente utilizamos el bloque ```Filter Examples```, seleccionamos el parámetro *condition class* a "no_missing_attributes" y ejecutamos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_7.PNG" alt="drawing" width="30%" height="30%"/></div>

Podemos ver que se han filtrado los atritubos faltantes.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_8.PNG" alt="drawing" width="80%" height="80%"/></div>

Como podemos ver, los datos tienen una distribución cuasi-normal, por lo tanto, podemos sustituir los faltantes por la media. Para sustituir los faltantes, podemos utilizar el bloque ```Replace Missing Values```. Seleccionamos el parámetro *attribute filter type* en "single", ingresamos el valor "Age" y dejamos el valor por defecto en "average" para el parámetro *default*.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_9.PNG" alt="drawing" width="30%" height="30%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_10.PNG" alt="drawing" width="80%" height="80%"/></div>

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

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_11.PNG" alt="drawing" width="80%" height="80%"/></div>

Resumen de datos:

- El total de personas que sobrevivieron es: 342
	- Mujeres: 0.6812865497076024
	- Hombres: 0.31871345029239767

Podemos ver que el sexo es un atributo importante para la predicción.
Ahora chequearemos si la clase también es importante.
Para esto, realizamos el mismo procedimiento.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_12.PNG" alt="drawing" width="80%" height="80%"/></div>

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

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_13.PNG" alt="drawing" width="80%" height="80%"/></div>

También lo podemos hacer de forma inversa, o sea, la clase en función del sexo.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_14.PNG" alt="drawing" width="80%" height="80%"/></div>

En los ejemplos podemos ver que tanto el sexo como la clase son importantes. Si eras de clase 1, tenias mas probabilidad de salvarte que si fueras de alguna otra clase.
Podemos realizar el mismo análisis sobre el atributo "Age".
En este caso también queremos analizar los que no sobrevivieron, para esto conectamos la salida del resto del bloque ```Filter Examples```, lo cual nos devuelve los que no sobrevivieron ("Survived=0").

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_15.PNG" alt="drawing" width="80%" height="80%"/></div>

Una vez corremos el proceso, podemos fijarnos en ambos gráficos según la salida.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_16.PNG" alt="drawing" width="80%" height="80%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_17.PNG" alt="drawing" width="80%" height="80%"/></div>

Podemos utilizar un "stripplot" para ver la distribución de los datos. Por ejemplo, para ver la distribución de los que sobrevivieron con respecto a la edad.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_18.PNG" alt="drawing" width="80%" height="80%"/></div>

Podemos ver que los pasajeros jovenes tenian mas posibilidades de salvarse.
También Rapidminer nos brinda una matriz para ver todos los gráficos juntos.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_19.PNG" alt="drawing" width="80%" height="80%"/></div>

### Feature Engineering (Ingeniería de Características)  <a class="anchor" id="2.5-bullet"></a>

Como sexo y embarcación son atributos categóricos, los tenemos que pasar a números, ya que varios algoritmos utilizan los atributos en números. Para esto utilizamos el bloque  ```Nominal to Numeric```.
Para esto seleccionamos los siguientes parámetros en el bloque:

- *Attribute filter type* $\rightarrow$ "single".
- *attribute* $\rightarrow$ "Name".
- *invert selection* $\rightarrow$ "Checked".
- *coding type* $\rightarrow$ "unique integers".

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_20.PNG" alt="drawing" width="80%" height="80%"/></div>

Con estos parámetros, el bloque transformará todos los atributos a enteros, asignandole un valor a cada clase. Por ejemplo male=1 y female=0.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_21.PNG" alt="drawing" width="80%" height="80%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_22.PNG" alt="drawing" width="80%" height="80%"/></div>

También podemos combinar el atributo SibSp y Parch, para saber cuan grande es la familia. Para esto utilizamos el bloque ```Generate Attributes```. Concetamos la salida del bloque ```Nominal to Numeric``` al bloque ```Generate Attributes``` y seteamos los parámetros de éste bloque con los siguientes valores:

- *function descriptions*:
	- *attribute name* $\rightarrow$ "FamSize".
	- *function expressions* $\rightarrow$ "SibSp + Parch + 1".
	
Esta unión de los atributos (con el objetivo de encontrar un atributo que clasifique mejor las instancias o reducir la complejidad) la podemos hacer ya que tenemos un entendimiento claro del negocio. Sin embargo, no siempre la podemos hacer si no entendemos bien el negocio. Podríamos estar introduciendo un error en el modelo.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_23.PNG" alt="drawing" width="80%" height="80%"/><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_24.PNG" alt="drawing" width="80%" height="80%"/></div>

Otro atributo interesante, es saber si se estaba solo o no. Podemos aplicar el mismo bloque con este objetivo con los siguientes parámetros:

- *function descriptions*:
	- *attribute name* $\rightarrow$ "IsAlone".
	- *function expressions* $\rightarrow$ "if(FamSize, 1, 0)".
	
<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_25.PNG" alt="drawing" width="80%" height="80%"/></div>

Una característica que en principio no parece importante es el nombre, pero de éste podemos extraer información. Utilizando los indicadores de la persona podemos deducir su estatus en la sociedad. Por ejemplo: Señor, Señora, Señorita, etc.
Utilizamos el bloque ```Generate Extract``` (este bloque es hecho por la comunidad, pero Rapidminer una vez que se da cuenta que no se encuentra, nos pregunta si lo deseamos bajar), que utiliza una expresión regular para, de un atributo, generar otro.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_26.PNG" alt="drawing" width="80%" height="80%"/></div>

Para generar el atributo, seleccionamos los siguientes parámetros:

- *source attribute* $\rightarrow$ "Name".
- *query type* $\rightarrow$ "Regular Expression".
- *regular expression queries*:
	- *attribute name* $\rightarrow$ "Title".
	- *query expression* $\rightarrow$ "([A-Za-z]+)\."
	
De este modo obtenemos el siguiente resultado.

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_27.PNG" alt="drawing" width="80%" height="80%"/></div>

## Modelado <a class="anchor" id="3-bullet"></a>
---

### Preparación del modelado <a class="anchor" id="3.1-bullet"></a>

### Entrenamiento de los modelos <a class="anchor" id="3.2-bullet"></a>

#### SVC <a class="anchor" id="3.2.1-bullet"></a>

#### Linear SVC <a class="anchor" id="3.2.2-bullet"></a>

#### Random Forest <a class="anchor" id="3.2.3-bullet"></a> 

#### Logistic Regression <a class="anchor" id="3.2.4-bullet"></a> 

#### KNeighbors <a class="anchor" id="3.2.5-bullet"></a> 

#### GaussianNB <a class="anchor" id="3.2.6-bullet"></a>

#### DecisionTree <a class="anchor" id="3.2.7-bullet"></a>

### Comparación de modelos <a class="anchor" id="3.3-bullet"></a>

### Mejorar los parametros del mejor modelo <a class="anchor" id="3.4-bullet"></a>

## Evaluación <a class="anchor" id="4-bullet"></a>
---

Podemos obtener el proceso entero en el siguiente link:
- [Rapidminer-Process]({filename}/posts/rm-processes/analisis_del_dataset_titanic-rapidminer.rmp)