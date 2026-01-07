from selenium.webdriver.common.by import By


class LoginLocators:
    email_input = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"],
    }
    password_input = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"],
    }
    login_button = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/appCompatButtonLogin"],
        "IOS": [By.ID, "com.loginmodule.learning:id/appCompatButtonLogin"],
    }
    register_button = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textViewLinkRegister"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textViewLinkRegister"],
    }

    login_success = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textViewName"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textViewName"],
    }


class LoginError:
    invalid_email_error = {
        "ANDROID": [By.XPATH, '//android.widget.TextView[@text="Enter Valid Email"]'],
        "IOS": [By.XPATH, '//android.widget.TextView[@text="Enter Valid Email"]'],
    }
    wrong_email_password_error = {
        "ANDROID": [By.XPATH, "com.loginmodule.learning:id/snackbar_text"],
        "IOS": [By.XPATH, "com.loginmodule.learning:id/snackbar_text"],
    }
