from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def sorgula_ip(ip_adresi):
    # Web sürücüsü başlatma (örneğin, Chrome WebDriver kullanıyoruz)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)  # 10 saniyeye kadar bekleyin

    try:
        # IP sorgulama sitesine gidin
        driver.get("https://www.ipaddress.com/")

        # İlgili giriş alanını bulun ve IP adresini gönderin
        input_field = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/header/form/input")))
        input_field.click()
        input_field.send_keys(ip_adresi)
        input_field.submit()

        # Sonuçları bulun ve ekrana yazdırın
        result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/section[1]/table/tbody")))
        print(result_element.text)

        with open ("info.txt","w",encoding="utf-8") as file :
            info=file.write(result_element.text)

    except Exception as e:
        print("Hata oluştu:", e)

    finally:
        # Web sürücüsünü kapatın
        driver.quit()


if __name__ == "__main__":
    ip_address = input("Sorgulanacak IP adresini girin: ")
    sorgula_ip(ip_address)
