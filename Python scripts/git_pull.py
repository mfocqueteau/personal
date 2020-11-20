import os


for elemento in os.listdir():
    try:
        if "Repo" in os.listdir(elemento):
            print(f"\nHaciendo pull a {elemento}...")
            os.system(f"cd '{elemento}/Repo/' && git pull")
    except Exception:
        pass
