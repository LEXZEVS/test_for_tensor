from selenium.webdriver.common.by import By


class FormPageLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_SUGGEST = (By.CSS_SELECTOR, ".mini-suggest__item.mini-suggest__item_type_fulltext")
    LOCATOR_YANDEX_SEARCH_RESULT_TABLE = (By.ID, "search-result")
    LOCATOR_YANDEX_SEARCH_RESULT_LINKS = (By.CSS_SELECTOR, "#search-result>li>div>div>a")

    LOCATOR_YANDEX_BUTTON_ALL_SERVICES = (By.XPATH, "//a[@data-statlog = 'services_suggest.more']")
    LOCATOR_YANDEX_BUTTON_IMAGES = (By.XPATH, "//a[@data-statlog = 'services-more-popup.item.images']")
    LOCATOR_YANDEX_FIRST_CATEGORY = (By.XPATH, "//div[contains(@class, 'PopularRequestList-Item_pos_0')]")
    LOCATOR_YANDEX_CLOSE_BANNER_ADS = (By.XPATH, "//div[@id = 'distr-pcode-container']//a")
    LOCATOR_YANDEX_SEARCH_FIELD_IMAGES = (By.XPATH, "//input[contains(@class, 'input__control')]")
    LOCATOR_YANDEX_FIRST_IMAGE = (By.XPATH, "//div[contains(@class, 'justifier__item_first')]//a")
    LOCATOR_YANDEX_CURRENT_IMAGE = (By.CLASS_NAME, 'MMImage-Origin')
    LOCATOR_YANDEX_IMG_BUTTON_PREV = (By.XPATH, "//div[contains(@class, 'MediaViewer-ButtonPrev')]")
    LOCATOR_YANDEX_IMG_BUTTON_NEXT = (By.XPATH, "//div[contains(@class, 'MediaViewer-ButtonNext')]")
