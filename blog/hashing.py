# for password hashing first need to import the passlib.context import CryptContext (pip install passlib)
from passlib.context import CryptContext

pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
# the pip install bcrypt -> is used for the schemes=["bcrypt"]
# the function bcrypt(is not from bcrypt)
class Hash():
    def bcrypt(password: str):
        hashedPassword=pwd_cxt.hash(password)
        return hashedPassword
    