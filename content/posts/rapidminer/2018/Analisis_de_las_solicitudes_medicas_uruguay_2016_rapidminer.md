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
					<li><a href="#3.4.2-bullet">3.4.2. Tratamiento de datos faltantes</a></li>
                    <li><a href="#3.4.3-bullet">3.4.3. Tratamiento de outliers</a></li>
                    <li><a href="#3.4.4-bullet">3.4.4. Correlación de atributos</a></li>
                    <li><a href="#3.4.5-bullet">3.4.5. Feature extraction</a></li>
                    <li><a href="#3.4.6-bullet">3.4.6. Dimension reduction</a></li>
                    <li><a href="#3.4.7-bullet">3.4.7. Transformaciones de los datos</a></li>
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
                    <li><a href="#4.2.2-bullet">4.2.2. Linear Discriminant Analysis</a></li>
					<li><a href="#4.2.3-bullet">4.2.3. Decision Tree</a></li>
					<li><a href="#4.2.4-bullet">4.2.4. Naive Bayes</a></li>
					<li><a href="#4.2.5-bullet">4.2.5. k-NN</a></li>
					<li><a href="#4.2.6-bullet">4.2.6. SVM</a></li>
					<li><a href="#4.2.7-bullet">4.2.7. Neural Net</a></li>
					<li><a href="#4.2.8-bullet">4.2.8. Random Forest</a></li>
					<li><a href="#4.2.9-bullet">4.2.9. Gradient Boosting Trees</a></li>
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
- ```Paciente``` $\Rightarrow$ En este caso, el numero de paciente lo tratamos como un identificador, por lo que para el entrenamiento no es importante. <span style="color:blue">IDENTIFICADOR</span>
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
			5. Atributos numéricos.
			
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
			1. Atributos numéricos.

- **Ensambles**:
	- *[Random Forest](https://es.wikipedia.org/wiki/Random_forest)*
		- Restricciones:
			1. Sin restricciones.
	- *[Gradient Boosting Trees](https://en.wikipedia.org/wiki/Gradient_boosting)*
		- Restricciones:
			1. Sin restricciones.

### 3.1. Importación de librerías <a class="anchor" id="3.1-bullet"></a>

<div style="text-align:center"><img src="https://1xltkxylmzx3z8gd647akcdvov-wpengine.netdna-ssl.com/wp-content/uploads/2016/06/rapidminer-logo-retina.png" alt="drawing" width="60%" height="60%"/></div><br/>

En este caso, no se importan librerías ya que se usa [Rapidminer](https://rapidminer.com/).

### 3.2. Importación de los datos <a class="anchor" id="3.2-bullet"></a>

Importamos el conjunto dentro de rapidminer (mediante la opción "Import Data"):

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_1.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez que importamos los datos en rapidminer, seleccionamos el identificador de persona como ID y el atributo *estado_solicitud* como label utilizando el operador ```Set Role```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_2.PNG" alt="drawing" width="50%" height="50%"/></div><br/>

Podemos ver, luego que ejecutamos que rapidminer nos identifica el ID y label:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_3.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En este punto también filtramos los atributos que analizamos anteriormente y detectamos (con el conocimiento del negocio actual) que no soy relevantes para el problema en cuestión. Para esto utilizamos el operador ```Select Attributes```. 
Estos atributos son:

- *fecha_solicitud*
- *fecha_autorizacion*
- *prestacion_desc*

Para realizar esto en rapidminer, seleccionamos los atributos en las propiedades del operador y luego seleccionamos la propiedad de "invert selection" para que nos deje solo el resto de los atributos:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_4.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

### 3.3. Visualización de los datos <a class="anchor" id="3.3-bullet"></a>

Podemos visualizar los datos una vez que ejecutamos el proceso:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_6.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Como resultado podemos ver que se tienen 24138 datos con atributos del tipo:

- Enteros $\rightarrow$ 2 (3 si contamos el identificador).
- Nominales $\rightarrow$  11 (12 si contamos la variable dependiente).

Para visualizar los datos utilizamos la pestaña "Statistics" de rapidminer que nos brinda resúmenes de los datos:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_5.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

### 3.4. Tratamiento de los datos <a class="anchor" id="3.4-bullet"></a>

En este punto se realizan las transformaciones de los datos que se adecuan a los modelos a utilizar.

#### 3.4.1. Sanitizar los datos <a class="anchor" id="3.4.1-bullet"></a>

La sanitización de los datos se utiliza ya que pueden haber instancias que estén mal, en relación al tipo de dato. Este análisis es más a nivel de negocio que de dato, ya que el negocio implica reglas que los datos deben cumplir.
Primeramente, podemos observar que el atributo *Sexo* tiene una clase "U". Esta clase no debería existir, ya que estamos hablando solamente de mujeres ("F") y hombres ("M"). No estamos teniendo en cuenta los que no se han definido todavía ("U"). Por lo tanto, declaramos esta clase como un valor faltante, para luego ser tratada. 
Lo mismo pasa con el atributo *prestador_departamento*, la clase "SIN DATO" la tomamos como un dato faltante.

Para declarar estos datos como faltantes, utilizamos el operador ```Declare Missing Value```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_7.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En este caso, podemos ver que el atributo *prestacion_cod* debemos re-declararlo como nominal, ya que es nuestra definición del negocio. Para esto utilizamos el operador ```Numerical to Polynominal```, y seleccionamos el atributo en cuestión:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_8.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Nota (atributos duplicados): En este caso no hay atributos duplicados, ya que cada paciente es distinto, por lo que pueden haber solicitudes iguales pero pacientes distintos.

#### 3.4.2. Tratamiento datos faltantes <a class="anchor" id="3.4.2-bullet"></a>

Los datos faltantes son inadmisibles para muchos modelos. El tratamiento de los datos faltantes implica imputar un valor, eliminar dichos datos o eliminar el atributo.

El atributo *medico_solicitante* tiene muchos faltantes, pero estos faltantes nos importan, ya que son los casos en donde no hubo un medico involucrado en realizar la solicitud. Es por esto, que imputamos estos atributos faltantes con una nueva clase "SIN MEDICO" para así tener una comprensión de que pasa con las solicitudes que no tienen un médico como solicitante. Esta operación la realizamos con el operador ```Replace Missing Values```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_9.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Esta acción nos ha generado una nueva clase que como podemos observar es la mayor, lo que implica que la mayor cantidad de solicitudes se envían sin un médico solicitante. Luego podremos ver si es importante o no el médico solicitante:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_10.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Para el resto de los datos, como son pocos, simplemente filtramos los atributos que no tienen datos faltantes mediante el operador ```Filter examples```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_11.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Luego de filtrado los atributos faltantes, nos quedan **24135** datos (luego de los tratamientos, habían unicamente 3 faltantes).

#### 3.4.3. Tratamiento de outliers <a class="anchor" id="3.4.3-bullet"></a>

Hay muchos modelos en los cuales los outliers reducen la performance o inducen un sesgo indeseado. Por eso, se debe detectar y tratar los outliers para evitar este tipo de problemas.

En este caso, ya hemos filtrado outliers que se sospecha que han sido mal ingresados por el sistema, sin embargo, un paso futuro sería aplicar algún algoritmo de detección de outliers para datos categóricos (como por ejemplo HBOS).

#### 3.4.4. Correlación de atributos <a class="anchor" id="3.4.4-bullet"></a>

Hay muchos (como los modelos lineales) que la correlación de los atributos influye fuertemente en los modelos. Es por esto, que muchas veces se debe chequear la correlación de los atributos para así eliminar los que están altamente correlacionados. Previamente, convertimos los valores a numéricos utilizando un en codeado simple (asigna a cada clase un número entero). Para esto utilizamos el operador ```Nominal to Numerical```:


<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_12.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

El resultado nos quedaría:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_13.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Para calcular la matriz de correlación utilizamos el operador ```Correlation Matrix```:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_14.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Una vez que ejecutamos, obtenemos la siguiente matriz de correlación:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_15.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Si seleccionamos las correlaciones mayores al 0.5, tenemos las siguientes:

- prestacion_cod vs area $\rightarrow$ 0.94934017096856
- prestacion_cod vs imae $\rightarrow$ 0.8779232011993128
- area vs imae $\rightarrow$ 0.8523444883137807
- medico_solicitante vs prestacion_cod $\rightarrow$ 0.8311839275581686
- tipo_prestacion vs area $\rightarrow$ 0.8169807912406536
- tipo_prestacion vs imae $\rightarrow$ 0.7981221562193258
- prestacion_cod vs tipo_prestacion $\rightarrow$ 0.7807664805402255
- medico_solicitante vs imae $\rightarrow$ 0.7602177011564148

En este punto podemos ver que hay varias relaciones, que desde el negocio tienen lógica, por ejemplo, el atributo *prestacion_cod* está altamente relacionado con el atributo *área*, ya que cada prestación (acto médico o medicamento) pertenece únicamente a un área:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_16.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En este sentido, podemos eliminar el atributo *area* (prestacion_cod nos brinda información más detallada sobre el problema). Vamos a dividir el conjunto en los datos filtrados por la correlación y los datos no filtrados.

Podemos realizar la misma suposición con respecto a los otros atributos (de un modo u otro, *area*, *imae*, *tipo_prestacion* y *medico_solicitante* son generalizaciones de *prestacion_cod*).

Por lo tanto, un conjunto tiene todos los atributos luego de la preparación de los datos y el otro tiene los siguientes atributos filtrados:

- *area*
- *imae*
- *medico_solicitante*
- *tipo_prestacion*

#### 3.4.5. Feature extraction <a class="anchor" id="3.4.5-bullet"></a>

Muchas veces se puede "diseñar" un atributo que es combinación de otros atributos (lineal o no lineal) para así obtener más información. Tal vez, este atributo generado es un mejor predictor y se mejora la solución.

En este caso no se ve a simple vista algún nuevo atributo que se pueda generar y que pueda mejorar la predicción.

#### 3.4.6. Dimension reduction <a class="anchor" id="3.4.6-bullet"></a>

Si las dimensiones son muy grandes, podemos aplicar técnicas que reduzcan la dimensionalidad de los atributos.

Sin embargo este no es el caso, ya que luego de los análsiis tenemos dos conjuntos para probar, uno con 11 atributos y otro con 7.

#### 3.4.7. Transformaciones de los datos <a class="anchor" id="3.4.7-bullet"></a>

En este punto se realizan las transformaciones necesarias de los datos. Las transformaciones incluyen desde transformaciones para reducir el sesgo o ajustar distribuciones de los datos hasta transformar los datos a valores numéricos o a valores categóricos. También en este punto se incluye la estandarización y normalización si se debe hacer.

Podríamos realizar las transformaciones necesarias, como una logarítmica para el atributo *prestador_departamento* (hay mucha diferencia entre Montevideo y los otros departamentos), pero rapidminer, en la mayoría de sus modelos utiliza, o podemos indicarle que utilice, dichas transformaciones.

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_17.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

## 4. Modelado <a class="anchor" id="4-bullet"></a>
---

En esta sección probamos varios modelos de machine learning. Utilizamos modelos predefinidos en rapdiminer.

Utilizaremos los siguientes modelos:

- ```Logistic Regression``` $\Rightarrow$  [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/logistic_regression/logistic_regression.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/logistic_regression/logistic_regression.html)
- ```Linear Discriminant Analysis``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/discriminant_analysis/linear_discriminant_analysis.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/discriminant_analysis/linear_discriminant_analysis.html)
- ```Decision Tree``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_decision_tree.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_decision_tree.html)
- ```Naive Bayes``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/bayesian/naive_bayes.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/bayesian/naive_bayes.html)
- ```k-NN``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/lazy/k_nn.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/lazy/k_nn.html)
- ```SVM``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/support_vector_machines/support_vector_machine.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/support_vector_machines/support_vector_machine.html)
- ```Neural Net``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/neural_nets/neural_net.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/neural_nets/neural_net.html)
- ```Random Forest``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_random_forest.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/parallel_random_forest.html)
- ```Gradient Boosting Trees``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/gradient_boosted_trees.html](https://docs.rapidminer.com/latest/studio/operators/modeling/predictive/trees/gradient_boosted_trees.html)

Y para chequear la performance de nuestros modelos utilizamos:

- ```Apply Model``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/scoring/apply_model.html](https://docs.rapidminer.com/latest/studio/operators/scoring/apply_model.html)
- ```Cross Validation``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/validation/cross_validation.html](https://docs.rapidminer.com/latest/studio/operators/validation/cross_validation.html)
- ```Performance``` $\Rightarrow$ [https://docs.rapidminer.com/latest/studio/operators/validation/performance/performance.html](https://docs.rapidminer.com/latest/studio/operators/validation/performance/performance.html)


Utilizaremos ```Optimize Parameters (Evolutionary)``` [https://docs.rapidminer.com/latest/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html](https://docs.rapidminer.com/latest/studio/operators/modeling/optimization/parameters/optimize_parameters_evolutionary.html) para la optimización del modelo basado en algoritmos evolutivos.

### 4.1. Preparación del modelado <a class="anchor" id="4.1-bullet"></a>

Los conjuntos a utilizar en el modelado son dos, uno con los atributos correlacionados y otro sin los atributos correlacionados.

### 4.2. Entrenamiento de los modelos <a class="anchor" id="4.2-bullet"></a>

En esta sección se entrenan los modelos especificados anteriormente para ver cuál es el que realiza la mejor predicción.

#### 4.2.1. Logistic Regression <a class="anchor" id="4.2.1-bullet"></a> 

Entrenamiento utilizando regresión logística:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_18.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_19.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_20.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **93%**.

#### 4.2.2. Linear Discriminant Analysis <a class="anchor" id="4.2.2-bullet"></a> 

En este caso, debemos convertir los valores a números utilizando "dummy encoding", ya que es un requerimiento del algoritmo (no maneja valores nominales y rapidminer tampoco los convierte automáticamente). Para esto utilizamos el operador ```Nominal to Numerical``` con la propiedad *dummy coding*

Dentro del proceso de validación cruzada, convertimos los datos a números, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_21.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_22.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **89.77%**.

En este caso podemos ver que el modelo tiene los siguientes parámetros:

*Linear Discriminant Model*
__Apriori probabilities:__
- AUTORIZADO $\Rightarrow$ 0.8977
- NO AUTORIZADO $\Rightarrow$ 0.1023

El modelo nos da que todos los valores deben ser clasificados como AUTORIZADO, ya que la prioridad Apriori es muy superior que la NO AUTORIZADO. Esto se debe a que la prioridad Apriori es muy alta en comparación con la de NO AUTORIZADO y las probabilidades condicionales no son lo suficientemente grandes para que algún ejemplo se clasifique como NO AUTORIZADO.

#### 4.2.3. Decision Tree <a class="anchor" id="4.2.3-bullet"></a> 

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_23.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_24.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **89.98%**.

#### 4.2.4. Naive Bayes <a class="anchor" id="4.2.4-bullet"></a> 

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_25.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_26.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **91.72%**.

#### 4.2.5. k-NN <a class="anchor" id="4.2.5-bullet"></a> 

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_27.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_28.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **88.08%**.

#### 4.2.6. SVM <a class="anchor" id="4.2.6-bullet"></a> 

Dentro del proceso de validación cruzada, convertimos los valores a numéricos, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_29.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_---.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **-----%**.

#### 4.2.7. Neural Net <a class="anchor" id="4.2.7-bullet"></a> 

Dentro del proceso de validación cruzada, convertimos los valores a numéricos, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_30.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_---.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **-----%**.

#### 4.2.8. Random Forest <a class="anchor" id="4.2.8-bullet"></a> 

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_31.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_---.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **-----%**.

#### 4.2.9. Gradient Boosting Trees <a class="anchor" id="4.2.9-bullet"></a> 

Dentro del proceso de validación cruzada, colocamos el modelo y los operadores para chequear el performance:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_32.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Los parámetros utilizados son los estándar de rapidminer.
Una vez entrenamos el modelo, obtenemos los siguientes resultados:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_---.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

En resumen tenemos una precisión de un **-----%**.

### 4.3. Comparación de modelos <a class="anchor" id="4.3-bullet"></a>

Una vez que tenemos las precisiones de los modelos, podemos comparar las performance de los modelos:

<div style="text-align:center"><img src="{filename}/posts/post-img/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer_33.PNG" alt="drawing" width="80%" height="80%"/></div><br/>

Para el caso de los modelos con los atributos correlaciones filtrados:

| Modelo              | Performance |
|---------------------|-------------|
| Random Forest       | 84.70       |
| Naive Bayes         | 82.84       |
| Logistic Regression | 80.97       |
| Decision Tree       | 79.85       |
| Linear SVC          | 78.73       |
| SVC                 | 71.73       |
| k-NN                | 61.94       |

Para el caso de los modelos con los atributos correlaciones no filtrados:

| Modelo              | Performance |
|---------------------|-------------|
| Random Forest       | 84.70       |
| Naive Bayes         | 82.84       |
| Logistic Regression | 80.97       |
| Decision Tree       | 79.85       |
| Linear SVC          | 78.73       |
| SVC                 | 71.73       |
| k-NN                | 61.94       |

Podemos ver que el algoritmo que nos birnda la mejor precision es la Regresión Logistica, y que filtrando los atributos correlacionados nos brinda una mejor predicción.

### 4.4. Feature selection <a class="anchor" id="4.4-bullet"></a>

Una vez que tenemos el modelo que nos de la mejor perdición, realizamos la selección de atributos utilizando algoritmos evolutivos para observar si se mejora en la predicción o no. En si, esto se debería realizar para cada algoritmo, y luego compararlos, pero consume mucho tiempo este tipo de procesos.

### 4.5. Optimización <a class="anchor" id="4.5-bullet"></a>

En esta sección se optimiza el modelo para utilizarlo en la puesta a producción.

## 5. Evaluación <a class="anchor" id="5-bullet"></a>
---

Podemos obtener el proceso entero en el siguiente link:

- [Rapidminer-Process]({filename}/posts/rm-processes/Analisis_de_las_solicitudes_medicas_uruguay_2016_rapidminer.rmp)

## 6. Puesta en producción <a class="anchor" id="6-bullet"></a>
---