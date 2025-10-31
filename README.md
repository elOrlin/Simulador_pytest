# 🧪 Simulador Pytest

[![codecov](https://codecov.io/gh/elorlin/simulador_pytest/branch/master/graph/badge.svg)](https://codecov.io/gh/elorlin/simulador_pytest)

**Tests:** Haciendo pruebas unitarias con **Pytest** y **cobertura 100%**  
**CI/CD:** Ejecutado automáticamente con **GitHub Actions**

---

## 🚀 Descripción

Este proyecto demuestra un entorno profesional de **testing en Django/Python** usando:

- **Pytest** como framework principal  
- **Cobertura** con `pytest-cov`  
- **Integración continua (CI/CD)** con GitHub Actions  
- Configuración sin Docker (entorno virtual `.venv`)  

El objetivo es mantener un **pipeline limpio, rápido y automatizado** para asegurar la calidad de código en cada push o PR.

---

## ⚙️ Ejecución local

```bash
# Activar entorno virtual
source .venv/bin/activate   # Linux/macOS
# o
.\.venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar tests con cobertura
pytest --ds=simulador_pytest.settings --cov=apps --cov-report=term-missing --cov-report=html

