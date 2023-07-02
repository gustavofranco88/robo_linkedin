from selenium import webdriver

# Defina o caminho para o ChromeDriver
driver_path = 'chromedriver.exe'

# Configure o ChromeDriver
options = webdriver.ChromeOptions()
#options.headless = True  # Opcional: execute o navegador em modo headless para não exibir a interface gráfica

# Inicie o driver do Chrome
driver = webdriver.Chrome()
