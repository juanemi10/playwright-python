# Playwright Python Automation Framework 🚀


Este repositorio contiene un framework de automatización de pruebas de extremo a extremo (E2E) desarrollado con **Python** y **Playwright**. El proyecto está diseñado bajo el patrón de diseño **Page Object Model (POM)** y preparado para ser ejecutado en entornos aislados mediante **Docker**.


## 🛠️ Tecnologías utilizadas


* **Lenguaje:** Python 3.14+

* **Framework de Pruebas:** Pytest

* **Herramienta de Automatización:** Playwright

* **Contenerización:** Docker & Docker Compose

* **Reportes:** Pytest-html (opcional)


## 🏗️ Estructura del Proyecto


```text
AUTOMATIONPYTHON/

├── pages/              # Definición de Page Objects (Locators y Acciones)
│   └── sandbox_page.py

├── tests/              # Scripts de prueba funcionales
│   └── test_sandbox.py

├── venv/               # Entorno virtual de Python

├── Dockerfile          # Configuración de imagen Docker

├── docker-compose.yml  # Orquestación de contenedores

├── pytest.ini          # Configuración global de Pytest

└── requirements.txt    # Dependencias del proyecto