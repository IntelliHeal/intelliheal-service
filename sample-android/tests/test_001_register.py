from intelliheal.interactions.mobile import mobile
from intelliheal.interactions.assertions import asserts

from object_repository.login import LoginLocators
from object_repository.register import RegisterLocators
from data.register import RegisterInput, RegisterSuccess

interact = mobile(30)
assertion = asserts(30)


def test_valid_register(driver):
    """
    Test valid register
    """
    # Launch app and perform register
    interact.click(LoginLocators.register_button)
    interact.send_keys(RegisterLocators.name_input, RegisterInput.exists_name)
    interact.send_keys(RegisterLocators.email_input, RegisterInput.exists_email)
    interact.send_keys(RegisterLocators.password_input, RegisterInput.exists_password)
    interact.send_keys(
        RegisterLocators.confirm_password_input,
        RegisterInput.exists_confirm_password,
    )
    interact.click(RegisterLocators.register_button)

    # Assert successful register by checking presence of a specific element
    assertion.element_is_displayed(RegisterLocators.register_snackbar)


def test_valid_register_II(driver):
    """
    Test valid register
    """
    # Launch app and perform register
    interact.click(LoginLocators.register_button)
    interact.send_keys(RegisterLocators.name_input, RegisterInput.name)
    interact.send_keys(RegisterLocators.email_input, RegisterInput.email)
    interact.send_keys(RegisterLocators.password_input, RegisterInput.password)
    interact.send_keys(
        RegisterLocators.confirm_password_input,
        RegisterInput.confirm_password,
    )
    interact.click(RegisterLocators.register_button)

    # Assert successful register by checking presence of a specific element
    assertion.element_is_displayed(RegisterLocators.register_snackbar)
    register_text = interact.get_text(RegisterLocators.register_snackbar)
    assertion._equal(register_text, RegisterSuccess.success_message)
    assertion.text_is_displayed(RegisterSuccess.success_message)
