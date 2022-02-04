
#This is second part of the script. This downloads Wizcli, pulls mongo image and allows to select a scan to run
import os
os.system("curl -o wizcli https://wizcli.app.wiz.io/wizcli")
os.system("chmod 744 ./wizcli")
os.system("WIZ_ENV=demo ./wizcli auth --id o4w93hqq6YsUjS3wyhGrKlKacYY6nyhk --secret K8ABbG09CES6KX63r06aWHK8skPBo-3VEJgdAw4UzrSfa6XV2ZiSuWJ5FwiOXgd6")
os.system("docker pull mongo")

while(True):
    userin = ""
    while(True):
        userin = input('MENU\n1: Container Image Pass\n2: VM Pass\n3: VM Image Pass\n4: IaC Pass\n5: Container Image Fail\n6: VM Fail\n7: VM Image Fail\n8: IaC Fail\n0: Exit\nPlease select a scan for WizCLI: ')
        if(userin == "0" or userin == "1" or userin == "2" or userin == "3" or userin == "4" or userin == "5" or userin == "6" or userin == "7" or userin == "8"):
            break
        else:
            print("Invalid Selection")
    if(userin == "0"):
        break

    if userin == "1":
        os.system("WIZ_ENV=demo ./wizcli docker scan --image mongo:latest")
    elif userin == "2":
        os.system("WIZ_ENV=demo ./wizcli vm scan --id i-0d9c58ebee2327420")
    elif userin == "3":
        os.system("WIZ_ENV=demo ./wizcli vm-image scan --id ami-00052165 --region us-east-2 --subscriptionId 984186218765")
    elif userin == "4":
        os.system("WIZ_ENV=demo ./wizcli iac scan --path fail_cf.tf")
    elif userin == "5":
        os.system("WIZ_ENV=demo ./wizcli docker scan --image mongo:latest -p SreeJenkinsPolicy")
    elif userin == "6":
        os.system("WIZ_ENV=demo ./wizcli vm scan --id i-0d9c58ebee2327420 -p SreeJenkinsPolicy")
    elif userin == "7":
        os.system("WIZ_ENV=demo ./wizcli vm-image scan --id ami-00052165 --region us-east-2 --subscriptionId 984186218765 -p SreeJenkinsPolicy")
    elif userin == "8":
        os.system("WIZ_ENV=demo ./wizcli iac scan --path fail_cf.tf -p iacscanning")