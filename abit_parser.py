from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from data_table import DataTable
from faculty import Faculty


class AbitParser:

    def __init__(self, faculties):
        self.faculties = faculties
        self.driver: WebDriver = None
        self.applicants_data_tables = []


    def set_webdriver(self):
        print('STARTED!')

        opts = Options()
        opts.headless = True
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
        print('webdriver options have been set')


    def parse_faculties(self):
        for i in range(len(self.faculties)):
            faculty: Faculty = self.faculties[i]
            print(f'\n{i + 1}. {faculty.name} - {faculty.get_link()}')

            self.driver.get(faculty.get_link())
            print('website page has been loaded')
            time.sleep(1)

            button_clicked_counter = 0
            while self._requests_load_button_exists():
                self.driver.find_element(by=By.ID, value='requests-load').click()
                button_clicked_counter += 1
                print(f'requests-load button has been clicked ({button_clicked_counter})')
                time.sleep(1)

            soup = BeautifulSoup(self.driver.page_source, 'html.parser')

            data_table = DataTable(faculty=faculty, html=soup.prettify())
            self.applicants_data_tables.append(data_table)
            print('data table has been saved')
            time.sleep(1)

        self.driver.close()
        print('\nDONE!')


    def show_table(self, index):
        data_table = self.applicants_data_tables[index]
        data_table.show_info()


    def _requests_load_button_exists(self):
        try:
            self.driver.find_element(by=By.ID, value='requests-load')
        except NoSuchElementException:
            return False

        return True
