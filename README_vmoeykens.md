# Software Testing Lab
Vincent Moeykens
## How to Run
Setup your Python environment >=3.8 and place `test_authentication.py` in the same directory as `authentication.py`. 
Then, run `python3 test_authentication.py` to see the output of the tests.
## Test Case Explanation

### Database Testing
For these test cases, we use an additional helper function called `get_user_credentials()` that returns the json object
of user credentials to prevent code duplication.
#### Test 1 (Registered User)
In this test, we create a list of pairs of all registered usernames, and their associated passwords and authenticate them 
against the database to make sure that all valid users can authenticate. 
#### Test 2 (Not Registered User)
In this test, we construct two lists of equal size, one of fake usernames and one of fake passwords and iterate through 
the list of these pairs. First we check to make sure the username isn't somehow in the database, then if it isn't we 
verify that when trying to authenticate it the authentication fails.
#### Test 3 (Password Validation)
For this final test, we take a list of fake passwords whose length is equal to or greater than the number of real 
usernames. We then pair fake passwords up with real usernames and verify that they don't authenticate.  

### Password Testing
For all of the password tests, we follow the structure of create a password that shouldn't pass (based on the type of 
test), and then we additionally test that when appending the rest of the requirements to make it pass that it does pass
the password validation. 
#### Test 1 (Minimum Length)
For this test we construct a password that is one character short of the minimum password length (but has all other 
requirements). We verify it fails then append one digit and verify it passes.
#### Test 2 (Maximum Length)
For this test we take a password that has all requirements except it is one character too long. We verify it fails and
then we create a new password that is the same as the previous, except one character shorter. We verify that this passes.
#### Test 3 (More than letters)
For this test we create a password that has only letters (both uppercase and lowercase) and we verify that it fails
password validation. Then we append a digit and a special character and verify that the password passes.
#### Test 4 (More than digits)
For this test we create a password that just has digits. We verify it doesn't pass validation, and then we append 
uppercase and lowercase letters, as well as a special character. We then verify this passes. 
#### Test 5 (At least one uppercase)
For this test we construct a password that has all requirements except an uppercase letter. We verify it fails and then 
we append one uppercase letter and verify it passes. 
#### Test 6 (At least one lowercase)
For this test we construct a password that has all requirements except a lowercase letter. We verify it fails and then 
append a lowercase letter and verify it passes. 
#### Test 7 (Basic Password)
This test is the easiest: we construct a password that meets all criteria and verify it passes. 