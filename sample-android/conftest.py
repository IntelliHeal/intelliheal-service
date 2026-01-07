import pytest
from configs.drivers import create_driver


@pytest.fixture
def driver():
    """
    Driver fixture that creates and manages Android driver instance
    """
    # Create driver
    driver_instance = create_driver()

    # Yield driver for test use
    yield driver_instance

    # Cleanup after test
    try:
        # Close the app before quitting driver
        driver_instance.terminate_app("com.loginmodule.learning")
    except Exception as e:
        print(f"Warning: Could not terminate app: {e}")
    finally:
        driver_instance.quit()
