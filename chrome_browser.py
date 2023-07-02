# Importe o webdriver específico para o navegador que deseja usar
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Crie uma instância do webdriver do Chrome
driver = Chrome()

# Abra uma página
driver.get("https://www.linkedin.com")

print('passei aqui 18')
# Fazer login
username = driver.find_element(By.ID, 'session_key')
password = driver.find_element(By.ID, 'session_password')
print('linha 22')

file = open('login.txt', 'r')
username.send_keys(file.read())

file = open('senha.txt', 'r')
password.send_keys(file.read())
password.send_keys(Keys.RETURN)
print('linha 26')

# Aguardar até que a página de feed seja carregada após o login
def document_initialised(driver):
    return driver.execute_script("return initialised")
print('29')

WebDriverWait(driver, 20)#.until(document_initialised)
print('passei 35')

# Pesquisar vagas
search_input = driver.find_element(By.CSS_SELECTOR, '#global-nav-typeahead > input')
WebDriverWait(driver, 20)
search_input.send_keys('desenvolvedor Python')
WebDriverWait(driver, 50)
search_input.send_keys(Keys.RETURN)
print('passei 42')
'''
# Aguardar até que os resultados da pesquisa de vagas sejam carregados
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'jobs-search-results')))

# Extrair informações dos resultados da pesquisa
results = driver.find_elements(By.CLASS_NAME, 'job-card-container')

for result in results:
    title = result.find_element(By.CLASS_NAME, 'job-card-search__title-link').text
    company = result.find_element(By.CLASS_NAME, 'job-card-container__company-name').text
    location = result.find_element(By.CLASS_NAME, 'job-card-container__metadata-item').text

    print("Título: ", title)
    print("Empresa: ", company)
    print("Localização: ", location)
    print("---")
'''
'''
# Enviar uma mensagem para um usuário específico
driver.get('https://www.linkedin.com/in/gustavoosoriofranco')

message_button = driver.find_element(By.CLASS_NAME, 'message-anywhere-button')
message_button.click()

message_input = driver.find_element(By.CLASS_NAME, 'msg-form__contenteditable')
message_input.send_keys('Olá! Esta é uma mensagem automatizada.')

send_button = driver.find_element(By.CLASS_NAME, 'msg-form__send-button')
send_button.click()

# Fechar o navegador
driver.quit()
'''