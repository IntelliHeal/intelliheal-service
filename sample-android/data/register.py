from faker import Faker


class RegisterInput:
    exists_name = "Test Intelliheal"
    exists_email = "test@intelliheal.com"
    exists_password = "Test@1234"
    exists_confirm_password = exists_password

    name = Faker().name()
    email = Faker().email()
    password = Faker().password()
    confirm_password = password


class RegisterSuccess:
    success_message = "Registration Successful"


class RegisterError:
    email_exists_error = "Email Already Exists"
