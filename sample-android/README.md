# IntelliHeal Android Automation Sample

This sample demonstrates how to use IntelliHeal pytest plugin for Android mobile test automation with AI-powered self-healing capabilities.

## 📁 Project Structure

```
sample-android/
├── .env.example              # Environment configuration template
├── requirements.txt          # Python dependencies
├── conftest.py              # Pytest fixtures and configuration
├── configs/
│   └── drivers.py           # Appium driver creation function
├── data/
│   ├── login.py            # Login test data classes
│   └── register.py         # Registration test data classes
├── object_repository/
│   ├── login.py            # Login page locators
│   └── register.py         # Registration page locators
├── tests/
│   ├── test_001_register.py # Registration test cases
│   └── test_002_login.py    # Login test cases
└── apps/
    └── application_test.apk  # Android APK file for testing
```

## 🚀 Quick Setup

### 1. Prerequisites
- Python 3.10+
- Appium Server
- Android SDK/ADB
- Android Device or Emulator

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API keys and settings
```

### 4. Start Appium Server
```bash
appium
```

### 5. Run Tests
```bash
pytest tests/
```

## 🔧 Configuration

### Environment Variables

Copy `.env.example` to `.env` and configure:

**IntelliHeal AI Configuration:**
- `AI_HEALING_APP_TYPE=MOBILE`
- `AI_HEALING_PLATFORM=ANDROID`
- `AI_HEALING_MAX_RETRIES=2`

**Project Metadata:**
- `PROJECT_NAME=Sample Android App`
- `PILLAR_NAME=Mobile Automation`

**AI Provider (choose one):**
- `AI_HEALING_PROVIDER=anthropic`
- `ANTHROPIC_API_KEY=your_api_key`

**Database Settings:**
- `AI_HEALING_DB_ENABLED=true`
- `DB_HOST=localhost`
- `DB_PORT=5432`

### Driver Configuration

The driver configuration in `configs/drivers.py` includes:
- App package: `com.loginmodule.learning`
- App activity: `com.loginmodule.learning.activities.LoginActivity`
- Automatic APK installation from `apps/application_test.apk`
- Device UDID configuration
- 10-second implicit wait

## 📱 Test Application

The sample tests the login module learning app with package `com.loginmodule.learning`. The APK is included in the `apps/` directory.

## 🧪 Test Cases

### Registration Tests (`test_001_register.py`)

**test_valid_register:**
- Navigates to registration page
- Fills registration form with existing user data
- Verifies registration success

**test_valid_register_II:**
- Navigates to registration page
- Fills registration form with new user data (Faker)
- Verifies registration success message

### Login Tests (`test_002_login.py`)

**test_valid_login:**
- Enters valid email and password
- Clicks login button
- Verifies successful login

## 🔍 IntelliHeal Usage

### Mobile Interactions
```python
from intelliheal.interactions.mobile import mobile

interact = mobile(30)
interact.send_keys(locator_dict, "text")
interact.click(locator_dict)
interact.get_text(locator_dict)
```

### Assertions
```python
from intelliheal.interactions.assertions import asserts

assertion = asserts(30)
assertion.element_is_displayed(locator_dict)
assertion.text_is_displayed("expected text")
assertion._equal(actual, expected)
```

### Locator Format
```python
locator_dict = {
    "ANDROID": [By.ID, "com.example:id/element"],
    "IOS": [By.ID, "com.example:id/element"]
}
```

## 📊 Test Data Structure

### Login Data (`data/login.py`)
```python
class LoginInput:
    exists_email = "test@intelliheal.com"
    exists_password = "Test@1234"
    wrong_email = Faker().email()
    wrong_password = Faker().password()

class LoginError:
    wrong_email_password_error = "Wrong Email or Password"
```

### Registration Data (`data/register.py`)
```python
class RegisterInput:
    exists_name = "Test Intelliheal"
    exists_email = "test@intelliheal.com"
    name = Faker().name()
    email = Faker().email()

class RegisterSuccess:
    success_message = "Registration Successful"
```

## 🎯 Page Object Model

### Login Locators (`object_repository/login.py`)
- `email_input` - Email input field
- `password_input` - Password input field
- `login_button` - Login button
- `register_button` - Register navigation button
- `login_success` - Success indicator element

### Registration Locators (`object_repository/register.py`)
- `name_input` - Name input field
- `email_input` - Email input field
- `password_input` - Password input field
- `confirm_password_input` - Confirm password field
- `register_button` - Register button
- `register_snackbar` - Success/error message display

## 🔄 Driver Management

The `conftest.py` provides a `driver` fixture that:
- Creates Android driver using `create_driver()`
- Automatically manages app lifecycle
- Terminates app after each test
- Handles driver cleanup

## 🏃‍♂️ Running Tests

### Run All Tests
```bash
pytest tests/
```

### Run Specific Test
```bash
pytest tests/test_001_register.py::test_valid_register
```

### Run with Verbose Output
```bash
pytest -v tests/
```

### Run with Custom Markers
```bash
pytest -m "registration" tests/
```

## 📋 Dependencies

The `requirements.txt` includes:
- `IntelliHeal` - AI-powered test healing
- `pytest` - Testing framework
- `selenium` - WebDriver bindings

## 🤖 AI Healing Features

IntelliHeal automatically:
- Heals broken locators using AI
- Records healing actions to database
- Provides intelligent element recovery
- Supports multiple AI providers (Anthropic, OpenAI, Gemini, Groq)

## 🔧 Troubleshooting

### Common Issues

**App Installation:**
- Ensure APK exists in `apps/application_test.apk`
- Check device connection with `adb devices`

**Appium Connection:**
- Verify Appium server is running on `http://127.0.0.1:4723`
- Check device UDID in driver configuration

**Environment Setup:**
- Ensure all required environment variables are set
- Verify AI provider API keys are valid

### Test Execution

The framework will:
1. Create driver with app installation check
2. Run test with IntelliHeal interactions
3. Terminate app and quit driver after each test

## 📝 Notes

- Tests use existing user credentials from `LoginInput` and `RegisterInput`
- Faker library generates dynamic test data for new user scenarios
- All locators support both Android and iOS platforms
- IntelliHeal automatically heals broken selectors during test execution
