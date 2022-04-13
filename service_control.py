import subprocess
import os
import time

service = "gunicorn"

while True:
    p = subprocess.Popen(["systemctl","is-active",service], stdout=subprocess.PIPE)
    (output,err) = p.communicate()
    output = output.decode('utf-8')
    print("cevap = " , output , type(output))
    if "inactive" in output:
        print("aktif değil")
        command = "systemctl restart gunicorn.service"
        p = os.system('echo %s|sudo -S %s' % ("Recep123", command))
        print("tekrar başlatılıyor..")
        time.sleep(2)
        p = subprocess.Popen(["systemctl","is-active",service], stdout=subprocess.PIPE)
        (outoput,err) = p.communicate()
        output = outoput.decode('utf-8')
        print(output)
   

    else:
        print("everything is okey")

       
    time.sleep(3)

