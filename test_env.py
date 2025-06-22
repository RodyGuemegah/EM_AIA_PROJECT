from dotenv import load_dotenv
import os

load_dotenv()  # N'oublie pas les parenthèses !

print("POLE_EMPLOI_CLIENT_ID =", os.environ.get("POLE_EMPLOI_CLIENT_ID"))
print("POLE_EMPLOI_CLIENT_SECRET =", os.environ.get("POLE_EMPLOI_CLIENT_SECRET"))
