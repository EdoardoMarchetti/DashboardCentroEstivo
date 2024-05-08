import toml
import streamlit_authenticator as stauth


#--------------------------------------
#--------- AUTHENTICATION -------------
#--------------------------------------
#MARK: AUTHENTICATION

def get_authenticator():
    # Loading credentials from secrets.toml
    with open('.streamlit/secrets.toml', 'r') as file:
        secrets = toml.load(file)

    # Accessing credentials from the TOML file
    credentials = secrets['credentials']
    cookies = secrets['cookie']
    preauth = secrets['preauthorized']
    

    # Creating the authenticator object
    authenticator = stauth.Authenticate(
        credentials,
        cookies['name'],
        cookies['key'],  # Will be managed automatically
        cookies['expiry_days'],  # Will be managed automatically,
        preauth
    )

    return authenticator