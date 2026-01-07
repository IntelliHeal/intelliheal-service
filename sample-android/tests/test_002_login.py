from intelliheal.interactions.mobile import mobile
from intelliheal.interactions.assertions import asserts

from object_repository import login as login_objects
from data import login as login_data

interact = mobile(30)
assertion = asserts(30)


def test_valid_login(driver):
    """
    Test valid login
    """
    # Launch app and perform login
    interact.send_keys(
        login_objects.LoginLocators.email_input, login_data.LoginInput.exists_email
    )
    interact.send_keys(
        login_objects.LoginLocators.password_input,
        login_data.LoginInput.exists_password,
    )
    interact.click(login_objects.LoginLocators.login_button)

    # Assert successful login by checking presence of a specific element
    assertion.element_is_displayed(login_objects.LoginLocators.login_success)
