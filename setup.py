from setuptools import setup, find_packages

setup(
    name="RETO4",
    version="0.1.0",
    description="Proyecto de Data Engineering - ETL y procesamiento de datos",
    author="Melany Montero",
    author_email="melanymontero@example.com",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.1.0",
        "numpy>=1.24.3",
        "sqlalchemy>=2.0.20",
        "requests>=2.31.0",
        "pydantic>=2.3.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.9.1",
            "pylint>=2.17.5",
            "isort>=5.12.0",
        ],
        "jupyter": [
            "jupyter>=1.0.0",
            "notebook>=7.0.0",
            "ipykernel>=6.25.0",
        ],
    },
)
