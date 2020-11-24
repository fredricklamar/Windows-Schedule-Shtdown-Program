import os
class Shutdown:
    def __init__(self):
        pass
    def ByMinutes(minute=6):
        minute = int(minute * 60)
        os.system('shutdown /s /t {} /c "THE SYSTEM WILL SHUTDOWN IN THE NEXT {} MINUTES (Fredrick_Lamar)"'.format(minute, int(minute/60)))
    def ByHours(hour=60):
        hour = int(hour * 60 * 60 )
        os.system('shutdown /s /t {} /c "THE SYSTEM WILL SHUTDOWN IN THE NEXT {} HOURS (Fredrick_Lamar)"'.format(hour, int(hour/3600)))
    def Abort():
        os.system('shutdown /a')
