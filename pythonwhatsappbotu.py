import pywhatkit as kit

number = "00000000000" #telefon numarası
msg = "Mesaj yazılacak kısım"
hour = 1
minute = 28
seconds = 10

kit.sendwhatmsg(number,msg,hour,minute,seconds)