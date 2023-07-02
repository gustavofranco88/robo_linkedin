from selenium import webdriver

# Defina o caminho para o ChromeDriver
driver_path = 'geckodriver.exe'

# Configure o driver do Firefox
options = webdriver.FirefoxOptions()
options.headless = True  # Opcional: execute o navegador em modo headless para não exibir a interface gráfica

# Inicie o driver do Firefox
driver = webdriver.Firefox(executable_path=driver_path, options=options)