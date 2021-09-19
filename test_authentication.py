import unittest
import json
import sys

import authentication as auth

JSON_USER_FILE = 'database.json'

FAKE_USERNAME_LIST = ['kbradbury0', 'dthewys1', 'bniccols2', 'dcrocumbe3', 'mcorteney4', 'kmoar5', 'ldepinna6',
                 'gmessent7', 'kludwig8', 'aguillford9', 'fcicchinellia', 'rrubinowiczb', 'rmatyushkinc',
                 'bjanssond', 'omillione', 'nfeaksf']
FAKE_PASSWORD_LIST = ['CKC8qfN', 'eQFY7JqCshZj', '0prECH', 'GrKjjtoF8GTp', 'Cfznf07', 'BCUjjO', 'paaVkz6Xr',
                 '4lOAsm8Ws', 'H8Dkd8An4Sll', 'BWHWaSpZ', '4cNRS2wu3Gn', 'EVAcXGrVd5Y', 'B1V61B', 'VkDs1S2kNgL',
                 'okfZ4okFX9b', '5dEHRiwZ3XV']


def get_user_credentials():
    try:
        f = open(JSON_USER_FILE, "r")
        credentials = json.load(f)
        f.close()
        return credentials
    except IOError:
        print("Error reading file. Aborting...")
        sys.exit()
    except json.decoder.JSONDecodeError:
        print("Error reading file. Aborting...")
        sys.exit()


class TestDatabase(unittest.TestCase):

    def test_resgistered_user(self):
        """Get all registered users and their passwords and verify each validates with the database."""
        credentials = get_user_credentials()
        for user in credentials:
            valid_user = auth.database(user, credentials[user])
            self.assertTrue(valid_user)

    def test_not_registered_user(self):
        """Set up a list of fake usernames and passwords, make sure the human did the job correct and they are the
        same length, and then for each set of usernames and passwords verify first that it doesn't exist in the
        database, and then that it doesn't validate.
        """
        credentials = get_user_credentials()

        assert len(FAKE_USERNAME_LIST) == len(FAKE_PASSWORD_LIST)

        for username, password in zip(FAKE_USERNAME_LIST, FAKE_PASSWORD_LIST):
            if username not in credentials:
                valid_user = auth.database(username, password)
                self.assertFalse(valid_user)

    def test_password_validation(self):
        """Get the list of real credentials, verify we don't have more real users than fake passwords (if so
        we need more fake passwords), and then for each pair of real username/fake password, ensure the database
        does not verify.
        """
        credentials = get_user_credentials()

        assert len(credentials) <= len(FAKE_PASSWORD_LIST)

        for i, user in enumerate(credentials):
            valid_user = auth.database(user, FAKE_PASSWORD_LIST[i])
            self.assertFalse(valid_user)


class TestPasswordStrength(unittest.TestCase):
    def test_minimum_length(self):
        """Create a password that satisfies all requirements except min length, then append a character to make it
        the min length. Make sure both conform with the password min length constant, and then run the password
        verifier to make sure it is correct.
        """
        too_short_password = 'Msh#2jd'
        correct_password = too_short_password + '4'
        assert len(too_short_password) < auth.PASSWORD_MIN_LENGTH
        assert len(correct_password) >= auth.PASSWORD_MIN_LENGTH
        self.assertFalse(auth.password_strength(too_short_password))
        self.assertTrue(auth.password_strength(correct_password))

    def test_maximum_length(self):
        """Create a password that satisfies all requirements except max length, then strip a character to make it
        the max length. Make sure both conform with the password max length constant, and then run the password
        verifier to make sure it is correct.
        """
        too_long_password = 'sNb#N0lnXPB8kl8nWpX9uV9ZF8NEkBg3DxRRXg3vSae2vnafXUX'
        correct_password = too_long_password[:len(too_long_password) - 1]
        assert len(too_long_password) > auth.PASSWORD_MAX_LENGTH
        assert len(correct_password) <= auth.PASSWORD_MAX_LENGTH
        self.assertFalse(auth.password_strength(too_long_password))
        self.assertTrue(auth.password_strength(correct_password))

    def test_contains_more_than_letters(self):
        """Create a password with only lower and uppercase letters and verify that it doesn't authenticate, then
        append special characters and numbers and verify it authenticates.
        """
        only_letters_password = 'jkljiofasSDFASDf'
        correct_password = only_letters_password + '3@'
        self.assertFalse(auth.password_strength(only_letters_password))
        self.assertTrue(auth.password_strength(correct_password))

    def test_contains_more_than_digits(self):
        """Create a password with only numbers and verify that it doesn't authenticate, then
        append special characters and upper and lowercase letters and verify it authenticates.
        """
        only_numbers_password = '1234123412'
        correct_password = only_numbers_password + 'adDs$'
        self.assertFalse(auth.password_strength(only_numbers_password))
        self.assertTrue(auth.password_strength(correct_password))

    def test_at_least_one_uppercase(self):
        pass

    def test_at_least_one_lowercase(self):
        pass

    def test_basic_password_validation(self):
        pass


if __name__ == '__main__':
    unittest.main()
