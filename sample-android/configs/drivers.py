import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


def create_driver():
    """
    Create Android driver

    Returns:
        webdriver.Remote: Android driver instance
    """
    # Check if app is installed
    app_package = "com.loginmodule.learning"
    app_path = os.path.join(
        os.path.dirname(__file__), "..", "apps", "application_test.apk"
    )

    # Basic desired capabilities
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "Android Emulator"
    options.udid = ""  # Device UDID - change this for your device
    options.app_package = app_package
    options.app_activity = "com.loginmodule.learning.activities.LoginActivity"

    # Check if app exists and set app path for installation
    if os.path.exists(app_path):
        options.app = app_path
        options.no_reset = True
        options.full_reset = False  # Keep app data between sessions
    else:
        print(
            f"Warning: App not found at {app_path}, assuming app is already installed"
        )
        options.no_reset = True  # Don't reinstall if app not found

    options.auto_grant_permissions = True
    options.new_command_timeout = 300

    # Create and return driver
    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4723/wd/hub", options=options
    )

    # Set implicit wait
    driver.implicitly_wait(10)

    return driver
