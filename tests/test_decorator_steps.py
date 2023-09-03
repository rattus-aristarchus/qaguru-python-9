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
    open_main_page()
    search_repo("eroshenkoam/allure-example")
    follow_link("eroshenkoam/allure-example")
    open_issues_tab()
    issue_is_present()


@allure.step("открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("ищем репозиторий {repo}")
def search_repo(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys(repo)
    s("#query-builder-test").submit()


@allure.step("переходим по ссылке репозитория {link}")
def follow_link(link):
    s(by.link_text(link)).click()


@allure.step("открываем tab issues")
def open_issues_tab():
    s("#issues-tab").click()


@allure.step("проверяем наличие issue")
def issue_is_present():
    s(by.partial_text("#76")).should(be.visible)
