from main import User

try:
    user_name = input("Enter Your name \n")
    user_email = input("Enter your email \n")
    user_password = input("Enter your Password \n")

    User.create(name=user_name, email=user_email, password=user_password)
    print("Registered successfully")

except:
    print("Registration failed. Use a different email")
