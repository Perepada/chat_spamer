import pyautogui, time

print("Программа запущенна")

message = input("Сообщение: ")
words = message.split()

seconds = 5

while seconds >= 0:
    print("До запуска ", seconds, " секунд")
    seconds -= 1
    time.sleep(1)

while True:
    for word in words:
        pyautogui.typewrite(word.strip())
        pyautogui.press('enter')
        time.sleep(0.75)
