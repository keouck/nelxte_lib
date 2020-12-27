# Nelxte

Nelxte is a fast and open source python library for checking password strength. It comes with features such as, "Check for common passwords", "Special character checker", etc. All this can be done in just 2 lines of code and only takes 0.098 seconds(Most cases).

To use this library:

```python

from nelxte.password import check

strength = check(password)

```

This library has optional parameters such as min_length, max_length, special_chars, numbers, upper_case, lower_case and common_password.

Please note that all parameters take in boolean values except min_length and max_length, they take in integers.

min_length - Minimum length of the password(8 by default)

max_length - Minimum length of the password(200 by default)

special_chars - Check for special characters in the password(ie-[@`_!#$%^&*()<>?=+/|}{~:], 8 by default)

numbers - Check for numbers in the input(True by default)

upper_case-Check for upper case characters in the input(True by default)

lower_case-Check for lower case characters in the input(True by default)

common_password-This makes sure that the password isn't a very common one. This helps against brute force attacks and makes it more secure. Examples of some common passwords are-0987654321, computer, aaaaaa, etc.(True by default)

#Sample program:

```python

from nelxte.password import check

password = input('Please enter a password: ')
strength = check(password, min_length=8, max_length= 16, special_chars=True, numbers=True, upper_case=True, common_password=True)
print(strength)

```
#Output

```python

Please enter a password: 12341234
Password must contain atleast one special character.

```

Now, if we run the same program with a much stronger password,

```python

Please enter a password: gTh6@gtfRs)
OK


```

As you can see, it returns an, 'OK.'