import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

print('======= LOGIN DO LINKEDIN =======')
email = input('Digite o email: ')
password = input('Digite a senha: ')

print('======= BOT DE NETWORKING LINKEDIN =======\n')
search = input('Digite o filtro de busca: ')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com')
driver.maximize_window()

email_field = driver.find_element(By.ID, value='session_key')
email_field.click()
email_field.send_keys(email)

password_field = driver.find_element(By.ID, value='session_password')
password_field.click()
password_field.send_keys(password)

submit_button = driver.find_element(By.CSS_SELECTOR, value='[data-id="sign-in-form__submit-btn"]')
submit_button.click()

time.sleep(2)

search_field = driver.find_element(By.CLASS_NAME, value='search-global-typeahead__input')
search_field.click()

search_field.send_keys(search)

ActionChains(driver).send_keys_to_element(search_field, Keys.ENTER).perform()

time.sleep(5)

people_button = driver.find_element(By.XPATH, '//button[text()="People"]')
people_button.click()

time.sleep(5)

people = driver.find_elements(By.CSS_SELECTOR, value='.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view.search-primary-action__state-action-btn--omit-icon')

for p in range(len(people)):
    time.sleep(2)

    if people[p].text == 'Connect':
        people[p].click()

        note = driver.find_element(By.CSS_SELECTOR, value='[aria-label="Add a note"]')
        note.click()

        connection_name = driver.find_element(By.ID, value='send-invite-modal').text

        textarea = driver.find_element(By.ID, value='custom-message')
        textarea.click()
        textarea.send_keys(f'Olá {connection_name.split(" ")[1]}! Vi que temos habilidades em comum. Por isso, gostaria de me conectar com você. Desde já, agradeço.')

        send_button = driver.find_element(By.CSS_SELECTOR, value='[aria-label="Send now"]')
        send_button.click()
