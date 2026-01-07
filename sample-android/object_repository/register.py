from selenium.webdriver.common.by import By


class RegisterLocators:
    name_input = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textInputEditTextName"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextName"],
    }
    email_input = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextEmail"],
    }
    password_input = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextPassword"],
    }

    confirm_password_input = {
        "ANDROID": [
            By.ID,
            "com.loginmodule.learning:id/textInputEditTextConfirmPassword",
        ],
        "IOS": [By.ID, "com.loginmodule.learning:id/textInputEditTextConfirmPassword"],
    }

    register_button = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/appCompatButtonRegister"],
        "IOS": [By.ID, "com.loginmodule.learning:id/appCompatButtonRegister"],
    }

    register_snackbar = {
        "ANDROID": [By.ID, "com.loginmodule.learning:id/snackbar_text"],
        "IOS": [By.ID, "com.loginmodule.learning:id/snackbar_text"],
    }


class RegisterError:
    invalid_name_error = {
        "ANDROID": [By.XPATH, '	//android.widget.TextView[@text="Enter Full Name"]'],
        "IOS": [By.XPATH, '//android.widget.TextView[@text="Enter Full Name"]'],
    }
    password_mismatch_error = {
        "ANDROID": [
            By.XPATH,
            '//android.widget.TextView[@text="Password Does Not Matches"]',
        ],
        "IOS": [
            By.XPATH,
            '//android.widget.TextView[@text="Password Does Not Matches"]',
        ],
    }
