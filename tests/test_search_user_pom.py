from data.users_data import USER_WITH_UNIQUE_LAST_NAME


def test_search_user_pom(create_users, main_page):
    actual_search_last_name = main_page.go_to_search_page().type_last_name(USER_WITH_UNIQUE_LAST_NAME).click_search().get_last_name_td_text()

    assert actual_search_last_name == USER_WITH_UNIQUE_LAST_NAME
