# Security 

## Password

We are using Django's default password settings. The password attribute of a User object is a string of several component, separated by dollar sign:  

`<algorithm>$<iterations>$<salt>$<hash>`

The components are a hashing algorithm, the number of algorithm iterations, the random salt and the resulting password hash.
By default, Django uses the PBKDF2 algorithm, a SHA256 hash and a password stretching algorithm recommended by NIST.  

Alternatively to using Django's in-built password management, it's possible to either use Argon2 or bcrypt.
Argon2 currently seems to be the most secure and efficient library. However, considering the relatively small value of Crc's data, we see the in-built password setting as sufficient for our purposes.  

## Password validation

Your password can't be too similar to your other personal information.
Your password must contain at least 8 characters.
Your password can't be a commonly used password.
Your password can't be entirely numeric.

https://docs.djangoproject.com/en/2.1/topics/auth/passwords/

## Form sanitation

username: Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.