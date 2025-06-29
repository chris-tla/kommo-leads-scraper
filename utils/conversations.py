import pandas as pd
import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_first_reply(driver, lead_url):
    try:
        driver.get(lead_url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.message__text"))
        )
        time.sleep(1.5)

        mensajes = driver.find_elements(By.CSS_SELECTOR, "div.message__text")
        for m in mensajes:
            texto = m.text.strip()
            if texto:
                return texto

        return "[Sin respuesta encontrada]"

    except Exception as e:
        logging.error(f"Error extrayendo mensaje de {lead_url}: {e}")
        return "[Error al cargar]"


def scrap_first_replies(driver, input_file="leads_data.xlsx", output_file="leads_with_replies.xlsx"):
    try:
        df = pd.read_excel(input_file)
        if "url" not in df.columns:
            raise ValueError("La columna 'url' no fue encontrada en el archivo.")

        respuestas = []
        for i, row in df.iterrows():
            url = row["url"]
            logging.info(f"Procesando lead {row['lead_id']}...")
            respuesta = get_first_reply(driver, url)
            respuestas.append(respuesta)

        df["primera_respuesta"] = respuestas
        df.to_excel(output_file, index=False)
        logging.info(f"Archivo guardado en {output_file}")

    except Exception as e:
        logging.error(f"Error general en scrap_first_replies: {e}")