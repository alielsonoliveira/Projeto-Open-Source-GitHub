from selenium import webdriver


# Certifique-se de que o caminho esteja correto
navegador = webdriver.Chrome()
navegador.get('https://time.is/pt_br/Rome')


navegador.find_element(By.NAME, 'Q').send_keys("tempo agora")
