import time

from pages.form_page_find import FormPageFind
from pages.form_page_images import FormPageImages

YANDEX_URL = 'https://ya.ru/'
IMAGES_URL = 'https://ya.ru/images/'
SEARCH_WORD = 'Тензор'
SEARCH_URL = 'tensor.ru'


class TestFormPage:
    def test_search(self, driver):
        """Tests cases with entered word in Yandex search engine."""

        form_page_find = FormPageFind(driver, YANDEX_URL)
        form_page_find.open()
        search_field = form_page_find.get_search_field()
        form_page_find.enter_word(search_field, SEARCH_WORD)
        form_page_find.check_search_results(search_field)
        link_table = form_page_find.get_link_table()
        form_page_find.check_first_link(link_table, SEARCH_URL)
        print('Test_search completed successfully.', '-'*79, sep='\n')

    def test_search_img(self, driver):
        """Tests cases with images block in given search engine."""

        form_page_images = FormPageImages(driver, YANDEX_URL)
        form_page_images.open()
        navigation_bar = form_page_images.get_navigation_bar()
        button_images = form_page_images.get_button_images(navigation_bar)
        form_page_images.go_to_images(button_images, IMAGES_URL)
        first_category = form_page_images.get_first_category()
        form_page_images.check_open_category(first_category)
        form_page_images.load_first_image()
        # не успевает прогружаться картинка - немного подождем
        time.sleep(2)
        form_page_images.check_load_images()
        first_image = form_page_images.get_first_image()
        form_page_images.go_to_next_image()
        form_page_images.check_load_images()
        form_page_images.check_next_image(first_image)
        form_page_images.go_to_prev_image()
        form_page_images.check_load_images()
        form_page_images.check_prev_image(first_image)
        print('Test_images completed successfully.', '-'*79, sep='\n')

