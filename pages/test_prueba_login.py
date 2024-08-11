# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# def test_elemet_by_id():
#     driver = webdriver.Chrome()
#     driver.get("https://www.domestika.org/auth/login?locale=es")
    
#     driver.implicitly_wait(10)
    
#     driver.find_element(By.ID , "user_email").send_keys("202010703@itla.edu.do")
#     driver.find_element(By.ID, "user_password").send_keys("Metano04")
   
#     buton = driver.find_element(By.CSS_SELECTOR, ".t-login-button.flex-shrink-0")
#     buton.click()
    
#     driver.save_screenshot('./data/LoginPositivo.jpg')
    
#     driver.quit();