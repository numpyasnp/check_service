import os
import subprocess
import time


def check_service(delay, service_name):
    while True:
        p = subprocess.Popen(
            ["systemctl", "is-active", service_name], stdout=subprocess.PIPE
        )
        (output, err) = p.communicate()
        output = output.decode("utf-8")
        print("Answer = ", output, type(output))
        if "inactive" in output:
            print("deactivate")
            command = "systemctl restart gunicorn.service"
            p = os.system("echo %s|sudo -S %s" % ("Root Password", command)) # You must fill in the root password 
            print("Restart service")
            time.sleep(2) # waiting for it to restart
            p = subprocess.Popen(
                ["systemctl", "is-active", service_name], stdout=subprocess.PIPE
            )
            (outoput, err) = p.communicate()
            output = outoput.decode("utf-8")
            print(output)
        else:
            print("everything is okey")
   
        time.sleep(delay)


check_service(3, "gunicorn")
