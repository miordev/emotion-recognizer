# **Sistemas Inteligentes**  
  
**Fecha:** 4 de Febrero del 2021  

**Universidad:** Universidad de La Laguna  
**Facultad:** Escuela Superior de Ingeniería y Tecnología  
**Grado:** Ingeniería en Informática  
**Asignatura:** Sistemas Inteligentes  
**Curso:** 4º    

---

## 📄 **Índice de Contenidos** 

- [ Directorios ](#directories)
- [ Objetivo ](#objective)
- [ Lenguaje ](#language)
- [ Preparación ](#preparation)
- [ Ejecución ](#execution)
- [ Pruebas ](#test)
- [ Autores ](#authors)


<a name="directories"></a>
## 📁 **Directorios** 

* bin ➡️ Script para descargar modelos
* csv ➡️ Clasificación de las fotos con sus emociones 
* code ➡️ Código fuente 

<a name="objective"></a>
## 🎯 **Objetivo** 

Reconocimiento de emociones de distintas maneras como lo son:

* Tiempo real
* Video
* Imagen

<a name="language"></a>
## 💻 **Lenguaje** 

Python versión 3

<a name="preparation"></a>
## 🔌 **Preparación** 

Una vez clonado el repo, como se ve a continuación

```bash
../<directorio-local> » git clone git@github.com:miguel141097/emotion-recognizer.git
```

Se debe instalar las dependencias, que se encuentran en el fichero [requirements.txt](./requirements.txt). Para instalarlas se utiliza con el siguiente comando:

```bash
../<directorio-local> » cd emotion-recognizer
../<directorio-local>/emotion-recognizer » pip install -r requirements.txt
```

Luego se pueden cargar los modelos con el siguiente comando, lo cual los descargará desde una carpeta comprimida en google drive

```bash
../<directorio-local>/emotion-recognizer » ./bin/models.sh
```

<a name="execution"></a>
## 🚀 **Ejecución**  

Para ejecutarlo desde terminal, se debe ejecuta el siguiente comando

```bash
../<directorio-local>/emotion-recognizer » cd src
../<directorio-local>/emotion-recognizer/src » python main.py
```

Lo cual mostrará el siguinete menú, donde cada argumento indica como se debe ejecutar el programa

```bash
Run the program with one of the following arguments
  -h --help                Help to run the programme
  -i --interface           Run the program interface
  -t --test                Execute the validation of the models
```

Por ejemplo, para ejecutar el programa con la interfáz de usuario sería

```bash
../<directorio-local>/emotion-recognizer/src » python main.py -i
```

En este momento se abre la interfáz gráfico y se selecciona el método deseado

<a name="test"></a>
## ⚗️ **Pruebas** 

Para ejecutar las pruebas se debe ejecutar el programa con el siguiente comando

```bash
../<directorio-local>/emotion-recognizer/src » python main.py -t
```

Lo cual ejecutará el modelo seleccionado con distintos valores de filtros y buscará el mejor valor y porcentaje para el reconocimiento de rostros 

<a name="authors"></a>
## ✒️ **Autores** 

* Miguel Ángel Ordoñez Morales - [miguel141097](https://github.com/miguel141097) 
* Óscar Moreira Estévez - [omorest](https://github.com/omorest)
* Adal Díaz Fariña - [AdalDiazFarina](https://github.com/AdalDiazFarina)