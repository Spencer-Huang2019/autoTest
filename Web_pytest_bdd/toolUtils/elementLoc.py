from selenium.webdriver.common.by import By

def eleLoc(driver, type, eleLoc):
    ele = None
    try:
        if type == "id":
            ele = driver.find_element(By.ID, eleLoc)
        elif type == "class_name":
            ele = driver.find_element(By.CLASS_NAME, eleLoc)
        elif type == "xpath":
            ele = driver.find_element(By.XPATH, eleLoc)
        elif type == "name":
            ele = driver.find_element(By.NAME, eleLoc)
        elif type == "css_selector":
            ele = driver.find_element(By.CSS_SELECTOR, eleLoc)
        elif type == "link_text":
            ele = driver.find_element(By.LINK_TEXT, eleLoc)
        elif type == "partial_link_text":
            ele = driver.find_element(By.PARTIAL_LINK_TEXT, eleLoc)
        else:
            ele = driver.find_element(By.TAG_NAME, eleLoc)
    except Exception:
        ele = None
    finally:
        return ele