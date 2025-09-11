from passlib.context import CryptContext  # type: ignore


pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto") # pyright: ignore[reportUndefinedVariable]

class Hash():
   def bcrypt(password: str):
     return pwd_cxt.hash(password) # pyright: ignore[reportUndefinedVariable]
 