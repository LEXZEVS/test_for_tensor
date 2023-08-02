from urllib.parse import urlparse
from selenium.webdriver import Keys
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageFind(BasePage):

    def get_search_field(self):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD, timeout=20)
        assert search_field is not None, 'None вместо объекта - поисковая строка не найдена.'
        print('\nInput search field found. OK.')
        return search_field

    def enter_word(self, search_field, word):
        search_field.click()
        search_field.send_keys(word)
        suggest_table = self.find_elements(Locators.LOCATOR_YANDEX_SEARCH_SUGGEST)
        assert suggest_table is not None, 'None вместо подсказки - таблица вариантов не найдена.'
        print('Table with suggestions for searching found. OK.')

    def check_search_results(self, search_field):
        search_field.send_keys(Keys.ENTER)
        search_result = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_RESULT_TABLE)
        assert search_result is not None, 'None вместо результатов поиска - таблица результатов поиска не обнаружена.'
        print('Table with results found. OK.')

    def get_link_table(self):
        result_links = self.find_elements(Locators.LOCATOR_YANDEX_SEARCH_RESULT_LINKS)
        assert result_links is not None, 'None вместо ссылок на результаты поиска - таблица ссылок не найдена.'
        return result_links

    def check_first_link(self, result_links, url):
        link = urlparse(result_links[0].get_attribute('href')).netloc
        assert link == url, f'Первая ссылка {link} вместо ссылки {url} - первая ссылка в поиске ' \
                            f'не соответствует {url} '
        print('Looking for link found in given range. OK.')
