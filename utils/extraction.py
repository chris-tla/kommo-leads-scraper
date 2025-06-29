import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_lead_data(driver):
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[data-id]"))
        )
        elements = driver.find_elements(By.CSS_SELECTOR, "[data-id]")
        data = []
        seen_ids = set()

        for el in elements:
            lead_id = el.get_attribute("data-id")
            if not lead_id or not lead_id.strip().isdigit() or lead_id in seen_ids:
                continue

            seen_ids.add(lead_id.strip())
            url = f"https://terandes1.kommo.com/leads/detail/{lead_id}"

            # Nombre del cliente
            try:
                name_tag = el.find_element(By.CSS_SELECTOR, 'a.js-navigate-link[title]')
                nombre = name_tag.get_attribute("title").strip()
            except:
                nombre = "Sin nombre"

            # Teléfono
            try:
                phone_tag = el.find_element(By.CSS_SELECTOR, '[data-action-code="phone"]')
                telefono = phone_tag.get_attribute("data-value").strip()
            except:
                telefono = "Sin teléfono"

            data.append((lead_id.strip(), url, nombre, telefono))

        return data
    except Exception as e:
        logging.error(f"Error extrayendo datos de leads: {e}")
        return []

def extract_all_pages(driver, base_url, max_pages=50):
    all_data = []
    seen_ids = set()

    for page in range(1, max_pages + 1):
        url = base_url if page == 1 else f"{base_url}page/{page}/?skip_filter=Y"
        logging.info(f"Cargando página {page}: {url}")
        driver.get(url)
        time.sleep(2)

        page_data = extract_lead_data(driver)

        # Evita duplicados
        page_data_unique = [lead for lead in page_data if lead[0] not in seen_ids]
        if not page_data_unique:
            logging.info(f"No se encontraron nuevos leads en la página {page}. Fin del proceso.")
            break

        for lead in page_data_unique:
            seen_ids.add(lead[0])
            all_data.append(lead)

    return all_data