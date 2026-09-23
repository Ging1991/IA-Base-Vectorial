# IA-Servidor

Servidor local para modelos de lenguaje y modelos de embeddings utilizando `llama.cpp`.

El proyecto permite levantar dos servidores independientes:

* **Servidor de lenguaje:** proporciona una API compatible con OpenAI para generación de texto.
* **Servidor de embeddings:** proporciona una API para generar vectores de embeddings.

La configuración de los modelos, ejecutable, puertos y parámetros se realiza mediante `configuracion.json`.

## Requisitos

* Python 3
* Git
* `llama-server` de `llama.cpp`
* Un modelo compatible con `llama.cpp` en formato GGUF
* Un modelo de embeddings compatible con `llama.cpp` en formato GGUF

Los modelos GGUF pueden obtenerse desde [Hugging Face](https://huggingface.co/models?library=gguf).

## 1. Clonar el repositorio

```bash
git clone https://github.com/Ging1991/IA-Servidor.git
cd IA-Servidor
```

## 2. Crear el entorno virtual

Desde la carpeta raíz del proyecto:

### Windows

```bash
python -m venv venv
```

Activar el entorno virtual:

```bash
venv\Scripts\activate
```

Si la activación fue correcta, la terminal mostrará `(venv)` al comienzo de la línea.

## 3. Instalar las dependencias

Con el entorno virtual activado:

```bash
pip install -r requirements.txt
```

Las dependencias utilizadas actualmente por el proyecto son principalmente las necesarias para realizar las solicitudes HTTP a los servidores.

## 4. Obtener `llama-server`

El proyecto utiliza el ejecutable `llama-server` de `llama.cpp`.

Se puede obtener una versión precompilada desde las releases oficiales de `llama.cpp`:

[Releases de llama.cpp](https://github.com/ggml-org/llama.cpp/releases)

Descargar una versión compatible con el sistema operativo y el hardware utilizado.

El archivo necesario es:

```text
llama-server.exe
```

En Windows, por ejemplo:

```text
C:\llama.cpp\llama-server.exe
```

## 5. Descargar los modelos

Los modelos deben estar disponibles en formato GGUF.

### Modelo de lenguaje

Como modelo de referencia se puede utilizar:

**Dolphin 2.9.4 Llama 3.1 8B Q4_K_M**

Disponible en Hugging Face:

https://huggingface.co/dphn/dolphin-2.9.4-llama3.1-8b-gguf

El archivo utilizado es:

```text
dolphin-2.9.4-llama3.1-8b-Q4_K_M.gguf
```

El modelo ocupa aproximadamente 4.92 GB.

### Modelo de embeddings

Como modelo de referencia se puede utilizar:

**Nomic Embed Text v1.5 Q4_K_M**

Disponible en Hugging Face:

https://huggingface.co/RinaChen/nomic-embed-text-v1.5-Q4_K_M-GGUF

El archivo utilizado es:

```text
nomic-embed-text-v1.5-q4_k_m.gguf
```

## 6. Configurar el proyecto

Antes de ejecutar el programa, modificar `configuracion.json`.

Ejemplo:

```json
{
    "ejecutable": "C://llama.cpp//llama-server.exe",
    "host": "127.0.0.1",
    "contexto": 2048,
    "capas": 999,
    "modelo_lenguaje": "C://Modelos//dolphin-2.9.4-llama3.1-8b-Q4_K_M.gguf",
    "modelo_embeddings": "C://Modelos//nomic-embed-text-v1.5-q4_k_m.gguf",
    "puerto_lenguaje": 8080,
    "puerto_embeddings": 8081
}
```

### Parámetros

| Parámetro           | Descripción                                          |
| ------------------- | ---------------------------------------------------- |
| `ejecutable`        | Ruta al archivo `llama-server.exe`.                  |
| `host`              | Dirección donde se ejecutarán los servidores.        |
| `contexto`          | Tamaño del contexto utilizado por el modelo.         |
| `capas`             | Cantidad de capas que se intentarán ejecutar en GPU. |
| `modelo_lenguaje`   | Ruta al modelo GGUF de lenguaje.                     |
| `modelo_embeddings` | Ruta al modelo GGUF de embeddings.                   |
| `puerto_lenguaje`   | Puerto utilizado por el servidor de lenguaje.        |
| `puerto_embeddings` | Puerto utilizado por el servidor de embeddings.      |

Las URLs de los servicios se generan automáticamente utilizando `host` y el puerto correspondiente.

Por ejemplo:

```text
Servidor de lenguaje:
http://127.0.0.1:8080

Servidor de embeddings:
http://127.0.0.1:8081
```

## 7. Ejecutar

Con el entorno virtual activado:

```bash
python main.py
```

El programa mostrará un menú:

```text
1 - Levantar servidor de embeddings.
2 - Levantar servidor de lenguaje.
3 - Realizar la prueba de verificación para el servidor de embeddings.
4 - Realizar la prueba de verificación para el servidor de lenguaje.
```

### Opciones 1 y 2

Inician el servidor correspondiente utilizando los parámetros definidos en `configuracion.json`.

La ventana de la consola debe permanecer abierta mientras el servidor esté siendo utilizado.

### Opciones 3 y 4

Realizan una prueba de funcionamiento contra un servidor que ya se encuentre iniciado.

La prueba de embeddings genera un vector y comprueba que la respuesta tenga el formato esperado.

La prueba de lenguaje realiza una solicitud al endpoint de generación de texto.

## Notas

Los modelos y el ejecutable `llama-server` **no forman parte del repositorio** debido a su tamaño.

Cada usuario debe descargar los modelos y configurar sus propias rutas en `configuracion.json`.

El proyecto utiliza `llama.cpp` como motor de inferencia y las interfaces HTTP proporcionadas por `llama-server`.
