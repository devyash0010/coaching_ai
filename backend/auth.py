from passlib.context import CryptContext

def authenticate_teacher(email, password):
    # Check teacher table
    return True

pwd_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)



def hash_password(password):

    return pwd_context.hash(password)




def verify_password(
        plain_password,
        hashed_password
):

    return pwd_context.verify(

        plain_password,

        hashed_password

    )

authenticate_teacher()