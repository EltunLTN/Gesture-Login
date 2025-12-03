from gesture_recognizer import recognize_gesture

PASSWORD_GESTURE = "V-sign"

def login():
    print("Giriş üçün əl jestini göstərin (✌️):")
    gesture = recognize_gesture()
    if gesture == PASSWORD_GESTURE:
        print("✅ Giriş uğurlu!")
    else:
        print("❌ Yanlış jest! Giriş imtina edildi.")

if __name__ == "__main__":
    login()
