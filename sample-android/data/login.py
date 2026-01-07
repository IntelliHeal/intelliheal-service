from faker import Faker


class LoginInput:
    exists_name = "Test Intelliheal"
    exists_email = "test@intelliheal.com"
    exists_password = "Test@1234"
    exists_confirm_password = exists_password

    wrong_email = Faker().email()
    wrong_password = Faker().password()


class LoginError:
    wrong_email_password_error = "Wrong Email or Password"
