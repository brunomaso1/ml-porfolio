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

</center><small><a href="https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos">https://catalogodatos.gub.uy/dataset/solicitudes_2016_fondo-nacional-de-recursos</a></small></center>

<div style="text-align:center"><img src="http://www.fnr.gub.uy/sites/all/themes/fnrpb2013/logo.png" alt="drawing" width="100%" height="100%"/></div><br/>

El **Fondo Nacional de Recursos** (FNR) es una institución creada por el decreto *Ley 14.897* con carácter de persona pública no estatal, que brinda cobertura financiera a procedimientos de medicina altamente especializada y a medicamentos de alto precio para toda la población que se radique en el país y que sea usuaria del Sistema Nacional Integrado de Salud.

En el caso de los procedimientos cubiertos estos se efectúan a través de los Institutos de Medicina Altamente Especializada (IMAE) que son prestadores públicos o privados, que cuentan con la habilitación del Ministerio de Salud Pública para su realización.

<div style="text-align:center"><img src="https://fee.org/media/24118/health-care_mini.jpg?anchor=center&mode=crop&width=1920&rnd=131497055300000000" alt="drawing" width="100%" height="100%"/></div><br/>

### 1.1. Contexto <a class="anchor" id="1.1-bullet"></a>

Actualmente, los medicamentos y actos médicos (de alto costo) necesitan una aprovación previa del FNR para su realización, por lo que cada caso es evaluado para luego tomar una decisión si birndar el apoyo económico o no.

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

- ```tipo_prestacion```: Tipo de prestación (String) $\Rightarrow$ El tipo de prestación es un dato importante ya que indica si es un acto médico o un medicamento. <span style="color:green">IMPORTANTE</span>
- ```area```: Área de la prestación (String) $\Rightarrow$ El área de prestación es importante, ya que indica el tipo de tratamiento que se ha realizado. <span style="color:green">IMPORTANTE</span>
- ```prestacion_cod```: Código de la prestación (Integer) $\Rightarrow$ El código de prestación es el tipo de tratamiento. <span style="color:green">IMPORTANTE</span>
- ```prestacion_desc```: Descripción de la prestación (String) $\Rightarrow$ Es la descripción de la presentación. Es el mismo atributo que prestacion_cod. <span style="color:red">NO IMPORTANTE</span>
- ```fecha_solicitud```: Fecha de solicitud (Date) $\Rightarrow$ Es la descripción de la presentación. Es el mismo atributo que prestacion_cod <span style="color:red">NO IMPORTANTE</span>
- ```estado_solicitud```: Estado de la solicitud (String) $\Rightarrow$
- ```fecha_autorizacion```: Fecha de autorización (Date) $\Rightarrow$
- ```Paciente```: Número de paciente (Integer) $\Rightarrow$
- ```Edad_años```: Edad en años (Integer) $\Rightarrow$
- ```Sexo```: Sexo (String) $\Rightarrow$
- ```Departamento_residencia```: Departamento de residencia del paciente (String) $\Rightarrow$
- ```prestador_salud```: Prestador de salud (String) $\Rightarrow$
- ```prestador_departamento```: Departamento del prestador de salud (String) $\Rightarrow$
- ```prestador_tipo```: Tipo de prestador (String) $\Rightarrow$
- ```medico_solicitante```: Médico solicitante (String) $\Rightarrow$
- ```imae```: IMAE (String) $\Rightarrow$

## 3. Preparación de los datos <a class="anchor" id="3-bullet"></a>

En esta sección se preparan los datos para ser utilizados por varios modelos. Se tiene en cuenta las restricciones de los modelos, por lo que se pueden preparar varios conjuntos para distintos modelos.

- Como se enfocan estos problemas usualmente.
- Tipos de algoritmos a utilizar.
- Restricciones de los datos para dichos algoritmos.

Ej, para la resgresión lineal:
Requerimientos de los atributos para la regresión lineal:

1. Asumir una relación lineal entre los datos.
2. Remover el ruido.
3. Remover atributos correlacionados.
4. Distribución gaussiana.
5. Normalizar entradas.

### 3.1. Importación de librerías <a class="anchor" id="3.1-bullet"></a>

Las librerías a utilizar son las siguientes:

- ```numpy``` $\rightarrow$ NumPy es el paquete fundamental para la informática científica con Python (http://www.numpy.org/).
- ```pandas``` $\rightarrow$ Pandas provee herramientas para la importación y el fácil análisis de los datos (https://pandas.pydata.org/).
- ```matplotlib``` $\rightarrow$ Matplotlib permite graficar los datos (https://matplotlib.org/).
- ```seaborn``` $\rightarrow$ Seaborn permite una linda visualización estadística de los datos, en conjunción con matplotlib (https://seaborn.pydata.org/).
- ```pandas_profiling``` $\rightarrow$ Brinda un completo resumen de los datos (https://github.com/pandas-profiling/pandas-profiling).


```python
import numpy as np 
import pandas as pd 

import seaborn as sns
from matplotlib import pyplot as plt
%matplotlib inline
sns.set_style("whitegrid")

import pandas_profiling

import warnings
warnings.filterwarnings('ignore')
```

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas_profiling\plot.py:15: UserWarning: 
    This call to matplotlib.use() has no effect because the backend has already
    been chosen; matplotlib.use() must be called *before* pylab, matplotlib.pyplot,
    or matplotlib.backends is imported for the first time.
    
    The backend was *originally* set to 'module://ipykernel.pylab.backend_inline' by the following code:
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\runpy.py", line 193, in _run_module_as_main
        "__main__", mod_spec)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\runpy.py", line 85, in _run_code
        exec(code, run_globals)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel_launcher.py", line 16, in <module>
        app.launch_new_instance()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\traitlets\config\application.py", line 658, in launch_instance
        app.start()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\kernelapp.py", line 486, in start
        self.io_loop.start()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\tornado\platform\asyncio.py", line 132, in start
        self.asyncio_loop.run_forever()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\asyncio\base_events.py", line 422, in run_forever
        self._run_once()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\asyncio\base_events.py", line 1434, in _run_once
        handle._run()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\asyncio\events.py", line 145, in _run
        self._callback(*self._args)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\tornado\platform\asyncio.py", line 122, in _handle_events
        handler_func(fileobj, events)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\tornado\stack_context.py", line 300, in null_wrapper
        return fn(*args, **kwargs)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\zmq\eventloop\zmqstream.py", line 450, in _handle_events
        self._handle_recv()
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\zmq\eventloop\zmqstream.py", line 480, in _handle_recv
        self._run_callback(callback, msg)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\zmq\eventloop\zmqstream.py", line 432, in _run_callback
        callback(*args, **kwargs)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\tornado\stack_context.py", line 300, in null_wrapper
        return fn(*args, **kwargs)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\kernelbase.py", line 283, in dispatcher
        return self.dispatch_shell(stream, msg)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\kernelbase.py", line 233, in dispatch_shell
        handler(stream, idents, msg)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\kernelbase.py", line 399, in execute_request
        user_expressions, allow_stdin)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\ipkernel.py", line 208, in do_execute
        res = shell.run_cell(code, store_history=store_history, silent=silent)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\ipykernel\zmqshell.py", line 537, in run_cell
        return super(ZMQInteractiveShell, self).run_cell(*args, **kwargs)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 2662, in run_cell
        raw_cell, store_history, silent, shell_futures)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 2785, in _run_cell
        interactivity=interactivity, compiler=compiler, result=result)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 2901, in run_ast_nodes
        if self.run_code(code, result):
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 2961, in run_code
        exec(code_obj, self.user_global_ns, self.user_ns)
      File "<ipython-input-20-b994aea22841>", line 6, in <module>
        get_ipython().run_line_magic('matplotlib', 'inline')
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 2131, in run_line_magic
        result = fn(*args,**kwargs)
      File "<decorator-gen-108>", line 2, in matplotlib
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\magic.py", line 187, in <lambda>
        call = lambda f, *a, **k: f(*a, **k)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\magics\pylab.py", line 99, in matplotlib
        gui, backend = self.shell.enable_matplotlib(args.gui)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\interactiveshell.py", line 3049, in enable_matplotlib
        pt.activate_matplotlib(backend)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\IPython\core\pylabtools.py", line 311, in activate_matplotlib
        matplotlib.pyplot.switch_backend(backend)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\matplotlib\pyplot.py", line 231, in switch_backend
        matplotlib.use(newbackend, warn=False, force=True)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\matplotlib\__init__.py", line 1422, in use
        reload(sys.modules['matplotlib.backends'])
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\importlib\__init__.py", line 166, in reload
        _bootstrap._exec(spec, module)
      File "c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\matplotlib\backends\__init__.py", line 16, in <module>
        line for line in traceback.format_stack()
    
    
      matplotlib.use(BACKEND)
    

### 3.2. Importación de los datos <a class="anchor" id="3.2-bullet"></a>

Para importar los datos utilizamos Pandas (```pd.read_csv()```), con los cual los cargamos en la estructura de datos **Dataframe** de Pandas. En este punto también se realiza los joins necesarios para obtener un conjunto con el que trabajar.


```python
# Datos de entrenamiento.
training = pd.read_csv("datasettraining.csv")

# Datos para testing.
testing = pd.read_csv("datasettesting.csv")
```


    ---------------------------------------------------------------------------

    FileNotFoundError                         Traceback (most recent call last)

    <ipython-input-21-7f790f5735e2> in <module>()
          1 # Datos de entrenamiento.
    ----> 2 training = pd.read_csv("datasettraining.csv")
          3 
          4 # Datos para testing.
          5 testing = pd.read_csv("datasettesting.csv")
    

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas\io\parsers.py in parser_f(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, escapechar, comment, encoding, dialect, tupleize_cols, error_bad_lines, warn_bad_lines, skipfooter, doublequote, delim_whitespace, low_memory, memory_map, float_precision)
        676                     skip_blank_lines=skip_blank_lines)
        677 
    --> 678         return _read(filepath_or_buffer, kwds)
        679 
        680     parser_f.__name__ = name
    

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas\io\parsers.py in _read(filepath_or_buffer, kwds)
        438 
        439     # Create the parser.
    --> 440     parser = TextFileReader(filepath_or_buffer, **kwds)
        441 
        442     if chunksize or iterator:
    

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas\io\parsers.py in __init__(self, f, engine, **kwds)
        785             self.options['has_index_names'] = kwds['has_index_names']
        786 
    --> 787         self._make_engine(self.engine)
        788 
        789     def close(self):
    

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas\io\parsers.py in _make_engine(self, engine)
       1012     def _make_engine(self, engine='c'):
       1013         if engine == 'c':
    -> 1014             self._engine = CParserWrapper(self.f, **self.options)
       1015         else:
       1016             if engine == 'python':
    

    c:\programdata\anaconda3\envs\ml-porfolio\lib\site-packages\pandas\io\parsers.py in __init__(self, src, **kwds)
       1706         kwds['usecols'] = self.usecols
       1707 
    -> 1708         self._reader = parsers.TextReader(src, **kwds)
       1709 
       1710         passed_names = self.names is None
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader.__cinit__()
    

    pandas\_libs\parsers.pyx in pandas._libs.parsers.TextReader._setup_parser_source()
    

    FileNotFoundError: File b'datasettraining.csv' does not exist



```python
# Obtenemos el Id de los datos.
testID = testing['Id']

# Creamos un conjunto data que tiene ambos conjuntos, para así realizar las transformaciones a ambos también.
data = pd.concat([training.drop('SalePrice', axis=1), testing], keys=['train', 'test'])

# Eliminamos el índice.
data.drop(['Id'], axis=1, inplace=True)
```

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

#### 3.3.1. Pandas-profiling <a class="anchor" id="3.3.1-bullet"></a>


```python
# Generar resumen y mostrar.
pandas_profiling.ProfileReport(training)
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

- [Rapidminer-Process]({filename}/posts/rm-processes/sdfsdfsd.rmp)

## 6. Puesta en producción <a class="anchor" id="6-bullet"></a>
---

<div style="text-align:center"><img src="{filename}/posts/post-img/Titanic_dataset_analisis_rapidminer_30.PNG" alt="drawing" width="70%" height="70%"/></div><br/>
