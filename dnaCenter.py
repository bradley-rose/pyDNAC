from dnacentersdk import DNACenterAPI as dnacAPI

class dnac:
    def __init__(self, *, dnacUrl, username, password):
        self.api = dnacAPI(
            base_url = dnacUrl,
            username = username,
            password = password
        )

    def getAllDevices(self):
        runOffset = False
        offsetVar = 0
        allDevices = []

        while True:
            if runOffset:
                offsetVar += 500
                devices = self.api.devices.get_device_list(
                    offset = offsetVar
                )
            else:
                devices = self.api.devices.get_device_list()
            
            allDevices += devices['response']
            if len(devices['response']) < 500:
                break
            else:
                runOffset = True

        return allDevices