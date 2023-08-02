import time

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPageImages(BasePage):

    def get_navigation_bar(self):
        search_field = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD, timeout=20)
        search_field.click()
        navigation_bar = self.find_element(Locators.LOCATOR_YANDEX_BUTTON_ALL_SERVICES)
        assert navigation_bar is not None, 'None вместо меню сервисов - меню сервисов не найдено.'
        print('\nService menu found. OK.')
        return navigation_bar

    def get_button_images(self, navigation_bar):
        navigation_bar.click()
        button_images = self.find_element(Locators.LOCATOR_YANDEX_BUTTON_IMAGES)
        assert button_images is not None, 'None вместо кнопки "Картинки" - кнопка "Картинки" не найдено в меню ' \
                                          'сервисов. '
        print('Image button found. ОК.')
        return button_images

    def go_to_images(self, button_images, images_url):
        button_images.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.driver.current_url
        assert current_url == images_url, f'Переход на страницу {current_url} вместо {images_url}'
        print(f'Switching to {images_url} successfully. OK.')

    def get_first_category(self):
        time.sleep(2)
        first_category = self.find_element(Locators.LOCATOR_YANDEX_FIRST_CATEGORY)
        assert first_category is not None, 'None вместо обьекта первой категории изображений - первая категория ' \
                                           'изображений не найдена '
        print('First category images found. OK.')
        return first_category

    def close_banner(self):
        banner_button_close = self.find_element(Locators.LOCATOR_YANDEX_CLOSE_BANNER_ADS, timeout=3)
        if banner_button_close is not None:
            banner_button_close.click()

    def check_open_category(self, first_category):
        name_first_category = first_category.get_attribute('data-grid-text').lower()
        self.close_banner()
        first_category.click()
        search_value = self.find_element(Locators.LOCATOR_YANDEX_SEARCH_FIELD_IMAGES).get_attribute('value').lower()
        assert name_first_category == search_value, f'"{search_value}" вместо "{name_first_category}" - значение в ' \
                                                    f'поле поиска не соответствует названию первой категории '
        print('Input search text same with chosen category. OK.')

    def load_first_image(self):
        first_image = self.find_element(Locators.LOCATOR_YANDEX_FIRST_IMAGE)
        first_image.click()

    def check_load_images(self):
        assert self.driver.execute_script(
            "return document.getElementsByClassName('MMImage-Origin')[0].naturalWidth") > 0, "Изображение не " \
                                                                                             "загрузилось "
        print('Chosen image opened. OK.')

    def get_first_image(self):
        current_image = self.find_element(Locators.LOCATOR_YANDEX_CURRENT_IMAGE)
        first_image_src = current_image.get_attribute('src')
        return first_image_src

    def go_to_next_image(self):
        button_next = self.find_element(Locators.LOCATOR_YANDEX_IMG_BUTTON_NEXT)
        button_next.click()

    def check_next_image(self, first_image_src):
        current_image = self.find_element(Locators.LOCATOR_YANDEX_CURRENT_IMAGE)
        next_image_src = current_image.get_attribute('src')
        assert first_image_src != next_image_src, 'Ошибка перехода к следующему изображению - переход не осуществлён'
        print('Next image opened. OK.')

    def go_to_prev_image(self):
        button_prev = self.find_element(Locators.LOCATOR_YANDEX_IMG_BUTTON_PREV)
        button_prev.click()

    def check_prev_image(self, first_image_src):
        current_image = self.find_element(Locators.LOCATOR_YANDEX_CURRENT_IMAGE)
        prev_image_src = current_image.get_attribute('src')
        assert first_image_src == prev_image_src, 'Ошибка перехода к предыдущему изображению - переход не осуществлен'
        print('Previous image opened. OK.')
