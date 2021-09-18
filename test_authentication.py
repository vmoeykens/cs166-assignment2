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
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
