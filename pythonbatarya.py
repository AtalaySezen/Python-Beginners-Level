import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

des = str(percent) + "%Pil azalıyor!\n"

if plugged:
    des += "Sarj Oluyor"

if percent >=30:
    Notification(
        title="Batarya Bildirimi",
        description = des,
        duration=10,
        urgency="Geçmiş olsun kardeş",
    ).send()
