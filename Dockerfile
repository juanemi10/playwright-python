# Usamos la imagen oficial de Playwright que ya trae los navegadores
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Carpeta donde vivirá el código dentro del contenedor
WORKDIR /app

# Copiamos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Instalamos los navegadores (solo Chromium para que sea más rápido)
RUN playwright install chromium

# Copiamos todo nuestro código al contenedor
COPY . .

# Comando para ejecutar los tests al iniciar
CMD ["pytest", "-v"]