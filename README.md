# RETO4 - Proyecto Data Engineering

## 📋 Descripción
Proyecto de Data Engineering para ETL y procesamiento de datos con buenas prácticas de ingeniería.

## 📁 Estructura del Proyecto

```
RETO4/
├── data/
│   ├── raw/              # Datos crudos sin procesar
│   ├── processed/        # Datos procesados y listos para análisis
│   └── external/         # Datos externos de terceros
├── scripts/
│   ├── etl/              # Scripts de procesos ETL
│   ├── analytics/        # Scripts de análisis
│   └── utils/            # Funciones utilitarias reutilizables
├── notebooks/            # Jupyter notebooks para exploración
├── src/                  # Código fuente principal
├── tests/                # Tests unitarios
├── config/               # Configuración de la aplicación
├── logs/                 # Registros de ejecución
├── docs/                 # Documentación del proyecto
├── requirements.txt      # Dependencias Python
├── setup.py              # Configuración del paquete
└── README.md             # Este archivo
```

## 🔧 Instalación

### Requisitos previos
- Python 3.8+
- pip
- Git

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/melanymontero-eng/RETO4.git
cd RETO4
```

### Paso 2: Crear ambiente virtual
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### Paso 3: Instalar dependencias
```bash
pip install -r requirements.txt
```

## 📊 Uso

### Ejecutar ETL
```bash
python scripts/etl/main.py
```

### Ejecutar análisis
```bash
python scripts/analytics/analysis.py
```

### Ejecutar tests
```bash
pytest tests/
```

## 🔄 Workflow Git

### Crear rama para nuevas features
```bash
git checkout -b feature/nombre-feature
```

### Hacer commit
```bash
git add .
git commit -m "tipo: descripción breve"
```

### Hacer push
```bash
git push origin feature/nombre-feature
```

### Crear Pull Request
- Ir a GitHub y crear PR a `main`

## 📝 Convenciones

- **Nombrado de ramas**: `feature/`, `bugfix/`, `hotfix/`
- **Commit messages**: Seguir formato: `tipo: descripción`
  - `feat`: Nueva feature
  - `fix`: Bug fix
  - `docs`: Cambios en documentación
  - `refactor`: Refactorización
  - `test`: Añadir tests

## 👤 Autor
Melany Montero

## 📄 Licencia
MIT