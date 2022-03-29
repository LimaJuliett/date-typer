from datetime import datetime
import keyboard

today = datetime.now()

keyboard.write(today.strftime('%Y-%m-%d'))