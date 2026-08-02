import bcrypt


password = "DeepuFabricator@2026"


hashed = bcrypt.hashpw(
    password.encode("utf-8"),
    bcrypt.gensalt()
)


print("Password Hash:")
print(
    hashed.decode("utf-8")
)