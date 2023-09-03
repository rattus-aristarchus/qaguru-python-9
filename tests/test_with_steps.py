import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(severity_level=Severity.CRITICAL)
@allure.label("owner", 'lankinma')
@allure.feature("Задачи")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_github(setup_browser):
    with allure.step("открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("ищем репозиторий"):
        s(".search-input").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("открываем tab issues"):
        s("#issues-tab").click()

    with allure.step("проверяем наличие issue"):
        s(by.partial_text("#76")).should(be.visible)
