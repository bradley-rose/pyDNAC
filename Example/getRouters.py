from dnaCenter import dnac
dnacApi = dnac(
    dnacUrl = "",  # Insert DNAC URL
    username = "", # Insert username
    password = ""  # Insert password
)
devices = dnacApi.getAllDevices()
for device in devices:
    if device['family'] == "Routers":
        print(device['hostname'].split(".")[0].upper())