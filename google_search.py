import pytest
import selene
from selene import browser, be, have

@pytest.fixture(scope="session")
def setting_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 768

@pytest.fixture(scope='session')
def brows_open():
    browser.open('https://duckduckgo.com/')

    yield
    browser.quit()

def test_search_result_links(setting_browser, brows_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('html').should(have.text('Selene: User-Oriented Web UI Browser Tests in Python'))

def test_search_result_unsuccessful(setting_browser, brows_open):
    browser.element('[name="q"]').clear().type('рдаимдлоываагшдрашдтадлотаидлвыимдф').press_enter()
    browser.element('html').should(have.text('No results found for'))