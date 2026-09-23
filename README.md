# Base Vectorial

Aplicación en Python para crear una base vectorial a partir del contenido de un archivo PDF.

El programa:

1. Extrae el texto del PDF.
2. Limpia el texto.
3. Lo divide en fragmentos.
4. Genera un embedding para cada fragmento mediante un servidor local.
5. Crea un índice vectorial utilizando FAISS.
6. Guarda los fragmentos y el índice vectorial en disco.

La aplicación está diseñada como un componente de una arquitectura RAG. **No realiza búsquedas RAG ni consultas al modelo de lenguaje**; su función principal es construir la base vectorial.

## Arquitectura

```text
PDF
 │
 ▼
LectorPDF
 │
 ▼
Estrategia
 │
 ▼
Servidor de embeddings
 │
 ▼
Embeddings
 │
 ▼
BaseVectorial (FAISS)
 │
 ├──────────────┐
 ▼              ▼
JSON           FAISS
```

El servidor de embeddings se ejecuta como un componente independiente.

## Requisitos

* Python 3.10 o superior.
* Un servidor compatible con el endpoint:

```text
/v1/embeddings
```

* Un modelo de embeddings cargado en dicho servidor.
* Las dependencias Python indicadas en `requirements.txt`.

### Servidor de embeddings

Este proyecto necesita que el servidor de embeddings esté ejecutándose antes de crear la base vectorial.

Se puede utilizar el proyecto:

[IA-Servidor](https://github.com/Ging1991/IA-Servidor?utm_source=chatgpt.com)

Ese proyecto permite levantar un servidor local de embeddings utilizando `llama.cpp`.

El servidor debe estar disponible en la dirección configurada en `configuracion.json`. Por ejemplo:

```text
http://127.0.0.1:8081
```

El endpoint utilizado por esta aplicación es:

```text
http://127.0.0.1:8081/v1/embeddings
```

## Instalación

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd BASE_VECTORIAL
```

Se recomienda crear un entorno virtual:

```bash
python -m venv venv
```

Activar el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Estructura del proyecto

```text
BASE_VECTORIAL/
│
├── app/
│   ├── almacenamiento.py
│   ├── base_vectorial.py
│   ├── estrategia.py
│   ├── lector_pdf.py
│   ├── servidor_embeddings.py
│   ├── vectorizador.py
│   └── verificador.py
│
├── datos/
│   └── guion.pdf
│
├── configuracion.json
├── main.py
└── requirements.txt
```

## Configuración

La aplicación utiliza `configuracion.json` para definir sus parámetros.

Ejemplo:

```json
{
	"ruta_pdf": "datos/guion.pdf",
	"salida_documentos": "datos/documentos.json",
	"salida_faiss": "datos/documentos.faiss",
	"longitud": 600,
	"solapamiento": 200,
	"url_servidor_embeddings": "http://127.0.0.1:8081"
}
```

### Parámetros

| Parámetro                 | Descripción                                                       |
| ------------------------- | ----------------------------------------------------------------- |
| `ruta_pdf`                | Ruta del PDF que se utilizará como fuente.                        |
| `salida_documentos`       | Archivo JSON donde se almacenarán los fragmentos.                 |
| `salida_faiss`            | Archivo donde se almacenará el índice FAISS.                      |
| `longitud`                | Cantidad de caracteres de cada fragmento.                         |
| `solapamiento`            | Cantidad de caracteres compartidos entre fragmentos consecutivos. |
| `url_servidor_embeddings` | Dirección del servidor local de embeddings.                       |

Por ejemplo, con:

```json
"longitud": 600,
"solapamiento": 200
```

cada fragmento tendrá hasta 600 caracteres y compartirá 200 caracteres con el fragmento siguiente.

## Ejecución

Antes de ejecutar la aplicación, asegurarse de que el servidor de embeddings esté levantado.

Luego ejecutar:

```bash
python main.py
```

Se mostrará un menú:

```text
1 - Revisar configuración
2 - Crear base vectorial
```

### 1. Revisar configuración

Muestra los valores cargados desde `configuracion.json`.

Ejemplo:

```text
Configuración cargada:
ruta_pdf: datos/guion.pdf
salida_documentos: datos/documentos.json
salida_faiss: datos/documentos.faiss
longitud: 600
solapamiento: 200
url_servidor_embeddings: http://127.0.0.1:8081
```

### 2. Crear base vectorial

Ejecuta todo el proceso:

```text
PDF
 ↓
Extracción y limpieza
 ↓
División en fragmentos
 ↓
Generación de embeddings
 ↓
Creación del índice FAISS
 ↓
Guardado de archivos
```

Durante la generación de embeddings se muestra el progreso cada 10 fragmentos para indicar que el proceso continúa ejecutándose.

Al finalizar se informa la cantidad de vectores almacenados.

## Archivos generados

Al crear la base vectorial se generan dos archivos.

### `documentos.json`

Contiene los fragmentos de texto utilizados para generar los embeddings.

La posición de cada fragmento corresponde con la posición de su vector en FAISS:

```text
documentos.json       documentos.faiss
     [0]       ↔            [0]
     [1]       ↔            [1]
     [2]       ↔            [2]
     ...
```

### `documentos.faiss`

Contiene el índice vectorial generado mediante FAISS.

La aplicación utiliza `IndexFlatL2` para almacenar los vectores.

## Verificación de la base

La clase `Verificador` también permite inspeccionar una base vectorial existente.

La información disponible actualmente incluye:

* Cantidad de vectores.
* Dimensión de los vectores.
* Cantidad de fragmentos almacenados.

Por ejemplo:

```text
Base vectorial:
Vectores: 242
Dimensión: 768
Fragmentos: 242
```

La cantidad de vectores y fragmentos debería coincidir, ya que cada fragmento tiene asociado un único embedding.

## Flujo de trabajo completo

```text
1. Clonar el proyecto
        ↓
2. Crear entorno virtual
        ↓
3. Instalar requirements.txt
        ↓
4. Preparar el PDF
        ↓
5. Configurar configuracion.json
        ↓
6. Levantar el servidor de embeddings
        ↓
7. Ejecutar main.py
        ↓
8. Seleccionar "Crear base vectorial"
        ↓
9. Se generan:
       ├── documentos.json
       └── documentos.faiss
```

## Dependencia con IA-Servidor

Este proyecto y `IA-Servidor` tienen responsabilidades separadas:

```text
IA-Servidor
    │
    └── Ejecuta y expone el modelo de embeddings
                  │
                  ▼
            BASE_VECTORIAL
                  │
                  └── Construye y almacena la base vectorial
```

Por lo tanto, **IA-Servidor debe estar funcionando antes de ejecutar la opción "Crear base vectorial"**.
