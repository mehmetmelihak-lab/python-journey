def email_slicer():
    email=input('Enter your email please:').strip()
    if "@" not in email:
        print("Error:there must be @ in the email")
        return
    try:
        username,domain=email.split("@")
        provider,extension=domain.split(".")
    except ValueError:
        print('Error:Wrong format.Example:name@example.com')


    print(f"Username={username}")
    print(f"Domain={domain}")
    print(f"Provider={provider}")
    print(f"extension={extension}")
email_slicer()