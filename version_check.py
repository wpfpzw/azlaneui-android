from packaging.version import Version
import requests,sys

res=requests.get("https://api.github.com/repos/MetaCubeX/metacubexd/tags").json()

version_list=[Version(i["name"]) for i in res]
with open("version","r") as f:
    now_version=Version(f.read())
latest_version=max(version_list)
if latest_version>now_version:
    with open("version","w") as f:
        f.write(str(latest_version))
else:
    sys.exit(2)