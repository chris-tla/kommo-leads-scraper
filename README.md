# 🧲 Kommo Leads Scraper

Este proyecto **automatiza la extracción de leads desde Kommo CRM usando Selenium**. Permite obtener información estructurada directamente desde la vista de lista del CRM, sin necesidad de intervención manual, y guardarla en un archivo Excel para facilitar el análisis, el seguimiento comercial o la integración con otros sistemas.

---

## 🚀 ¿Qué hace este scraper?

Este scraper te permite:

✅ Abrir el navegador automáticamente (Chrome o Brave)  
✅ Iniciar sesión manualmente en Kommo  
✅ Recorrer múltiples páginas de leads  
✅ Extraer automáticamente:

- ID del lead
- URL de detalle
- Nombre del cliente
- Teléfono

✅ Guardar los resultados en `leads_data.xlsx` para análisis posterior

> Ideal para equipos comerciales, analistas o procesos de recuperación/contactabilidad.

---

## 📦 Requisitos

- Python 3.8 o superior
- Google Chrome o Brave (recomendado: Chrome)
- Acceso activo a Kommo CRM
- Dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del proyecto

```text
kommo-leads-scraper/
├── notebooks/
│   ├── 01_scrap_leads_list.ipynb          ← Extracción de leads (vista de lista)
│   ├── 02_scrap_lead_conversations.ipynb  ← (en desarrollo)
│   └── 03_scrap_first_replies.ipynb       ← Extracción de primeras respuestas
├── utils/                                 ← Módulos funcionales reutilizables
│   ├── driver.py                          ← Configura el navegador con Selenium
│   ├── extraction.py                      ← Lógica para extraer leads
│   ├── conversations.py                   ← Scraping de respuestas en el detalle del lead
│   ├── excel.py                           ← Limpieza y guardado en Excel
│   └── settings.py                        ← Parámetros globales
├── leads_data.xlsx                        ← Archivo generado con los leads
├── requirements.txt                       ← Librerías necesarias
├── .gitignore                             ← Exclusiones del repositorio
└── README.md                              ← Este archivo
```

---

## 🧪 ¿Cómo usarlo?

1.	Ejecuta notebooks/01_scrap_leads_list.ipynb
2.	Inicia sesión manualmente cuando el navegador se abra
3.	Una vez estés en la lista de leads, vuelve al notebook y presiona ENTER
4.	Se recorrerán todas las páginas de leads y se generará el archivo leads_data.xlsx

---

## 🧠 Mejoras futuras

-	Scraping de conversaciones lead por lead
-	Exportación paralela a CSV
-	Visualización de métricas con pandas + seaborn
-	Automatización periódica con cron o scheduler
-	Login automático por cookies/token


---

## ✨ Créditos

Creado con 💚 por [Christian Olarte](https://github.com/chris-tla)

Con soporte técnico de ChatGPT 🤖 y mucha cafeína ☕️
