import re


class Validations():
    def validate_password(self, password):
        """
        This method checks for strength of a password.
        :return:password is valid or not.
        """
        is_password_valid = True
        if (len(password) < 6 or len(password) > 12):
            is_password_valid = False
        elif not re.search("[a-z]", password):
            is_password_valid = False
        elif not re.search("[A-Z]", password):
            is_password_valid = False
        elif not re.search("[0-9]", password):
            is_password_valid = False
        elif not re.search("[$#@]", password):
            is_password_valid = False
        return is_password_valid

    def validate_email(self, email):
        """This method checks wheather an email is validate.
           :param:email.
           :returns: email is valid or not."""

        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email, re.IGNORECASE):
            return True
        return False

    def validate_whitespace(self):
        """Validates for whitespaces in data"""
