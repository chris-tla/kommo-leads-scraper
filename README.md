# 🧲 Kommo Leads Scraper

Este proyecto **automatiza la extracción de leads desde Kommo CRM usando Selenium**. Extrae información clave de la vista de lista y la guarda en formato Excel, lista para análisis o seguimiento comercial.

---

## 🚀 ¿Qué hace este scraper?

✅ Abre el navegador (Chrome o Brave)  
✅ Inicia sesión manualmente en Kommo  
✅ Recorre múltiples páginas de leads  
✅ Extrae:
- ID del lead
- URL del detalle
- Nombre del cliente
- Teléfono  
✅ Guarda todo en `leads_data.xlsx`

---

## 📦 Requisitos

- Python 3.8 o superior
- Google Chrome o Brave
- Kommo con acceso a leads

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 📂 Estructura del proyecto

kommo-leads-scraper/
├── notebooks/
│   ├── 01_scrap_leads_list.ipynb         ← Extracción de leads
│   └── 02_scrap_lead_conversations.ipynb ← (en desarrollo)
├── utils/                                ← Funciones reutilizables
│   ├── driver.py                         ← Configura el navegador
│   ├── extraction.py                     ← Extracción de leads por página
│   ├── excel.py                          ← Limpieza y guardado en Excel
│   ├── settings.py                       ← Parámetros globales
├── leads_data.xlsx                       ← Archivo generado
├── requirements.txt                      ← Librerías necesarias
├── .gitignore                            ← Archivos excluidos
└── README.md                             ← Este archivo

---

## 🧪 ¿Cómo usarlo?

  1.	Ejecuta notebooks/01_scrap_leads_list.ipynb
  2.	Inicia sesión manualmente cuando se abra el navegador
  3.	Presiona ENTER cuando estés en la lista de leads
  4.	Se recorrerán todas las páginas y se guardará la data en Excel

---

## 🧠 Mejoras futuras

•	Scraping de conversaciones lead por lead
•	Exportación paralela a CSV
•	Análisis con pandas y visualización de métricas
•	Automatización periódica
•	Login con cookies o token


---

## ✨ Créditos

Creado con 💚 por [Christian Olarte] (https://github.com/chris-tla)
Con soporte técnico de ChatGPT 🤖 xd
