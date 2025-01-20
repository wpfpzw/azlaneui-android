from packaging.version import Version
import requests,sys

res=requests.get("https://api.github.com/repos/MetaCubeX/metacubexd/tags").json()
res=[
  {
    "name": "v1.176.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.176.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.176.1",
    "commit": {
      "sha": "d0f2ec2855ee262bb66a461b2bca58cf78d36d4a",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/d0f2ec2855ee262bb66a461b2bca58cf78d36d4a"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc2LjE"
  },
  {
    "name": "v1.176.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.176.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.176.0",
    "commit": {
      "sha": "4bf631590ccb82106c30532f9c6a8cbf932ca369",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/4bf631590ccb82106c30532f9c6a8cbf932ca369"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc2LjA"
  },
  {
    "name": "v1.175.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.175.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.175.0",
    "commit": {
      "sha": "bb5824bb35c7e443c96339a3ec94daa76bba5e2d",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/bb5824bb35c7e443c96339a3ec94daa76bba5e2d"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc1LjA"
  },
  {
    "name": "v1.174.3",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.174.3",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.174.3",
    "commit": {
      "sha": "adae52c69e8363c9dd022ed8be6b9f69cd935881",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/adae52c69e8363c9dd022ed8be6b9f69cd935881"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc0LjM"
  },
  {
    "name": "v1.174.2",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.174.2",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.174.2",
    "commit": {
      "sha": "c2f51c604bf2f638cc93fc0de16dd3d5fa25ff9c",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/c2f51c604bf2f638cc93fc0de16dd3d5fa25ff9c"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc0LjI"
  },
  {
    "name": "v1.174.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.174.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.174.1",
    "commit": {
      "sha": "d906c4a7f2db52526b7b1102357f6428b15b7491",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/d906c4a7f2db52526b7b1102357f6428b15b7491"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc0LjE"
  },
  {
    "name": "v1.174.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.174.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.174.0",
    "commit": {
      "sha": "d5193d0015391c8c7e8101e259eb65cba89d7230",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/d5193d0015391c8c7e8101e259eb65cba89d7230"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTc0LjA"
  },
  {
    "name": "v1.173.3",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.173.3",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.173.3",
    "commit": {
      "sha": "e9025734a93afb58ebf9bb3da436e75623eb17d4",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/e9025734a93afb58ebf9bb3da436e75623eb17d4"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTczLjM"
  },
  {
    "name": "v1.173.2",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.173.2",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.173.2",
    "commit": {
      "sha": "ecb43c7c90c8d26da1882fbe0fbe698f61d8d9fc",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/ecb43c7c90c8d26da1882fbe0fbe698f61d8d9fc"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTczLjI"
  },
  {
    "name": "v1.173.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.173.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.173.1",
    "commit": {
      "sha": "ad3a83a53fd2295dafa76f4d8cb09fb728f0afac",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/ad3a83a53fd2295dafa76f4d8cb09fb728f0afac"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTczLjE"
  },
  {
    "name": "v1.173.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.173.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.173.0",
    "commit": {
      "sha": "f6103337175fa28fa7334cf4937a9f1daf85c542",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/f6103337175fa28fa7334cf4937a9f1daf85c542"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTczLjA"
  },
  {
    "name": "v1.172.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.172.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.172.0",
    "commit": {
      "sha": "8c615f231e0ce73804968db368a167bbfef8c7d3",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/8c615f231e0ce73804968db368a167bbfef8c7d3"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTcyLjA"
  },
  {
    "name": "v1.171.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.171.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.171.0",
    "commit": {
      "sha": "a75cb03818d62ffd6bf04f0e03bb6ea8a63e2ee1",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/a75cb03818d62ffd6bf04f0e03bb6ea8a63e2ee1"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTcxLjA"
  },
  {
    "name": "v1.170.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.170.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.170.0",
    "commit": {
      "sha": "26f9a6dbaee85ca334793a07e33d083ea1e0c407",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/26f9a6dbaee85ca334793a07e33d083ea1e0c407"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTcwLjA"
  },
  {
    "name": "v1.169.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.169.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.169.0",
    "commit": {
      "sha": "72efdd3c5a1a4a56a7ec8fce9f9abe1ad98966ad",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/72efdd3c5a1a4a56a7ec8fce9f9abe1ad98966ad"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY5LjA"
  },
  {
    "name": "v1.168.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.168.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.168.0",
    "commit": {
      "sha": "fd45c2e970a73e645398fa540f51a82bcc0b3754",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/fd45c2e970a73e645398fa540f51a82bcc0b3754"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY4LjA"
  },
  {
    "name": "v1.167.4",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.167.4",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.167.4",
    "commit": {
      "sha": "fe472fe0ea1c459b43d9bb7108684e7eecd9f73a",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/fe472fe0ea1c459b43d9bb7108684e7eecd9f73a"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY3LjQ"
  },
  {
    "name": "v1.167.3",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.167.3",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.167.3",
    "commit": {
      "sha": "fc96dc995a9151db5e25ccd926f74e0dad3c52c3",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/fc96dc995a9151db5e25ccd926f74e0dad3c52c3"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY3LjM"
  },
  {
    "name": "v1.167.2",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.167.2",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.167.2",
    "commit": {
      "sha": "e1cbbd8a0e62f4d82b7cd4ddd9d662ca06e3e38b",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/e1cbbd8a0e62f4d82b7cd4ddd9d662ca06e3e38b"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY3LjI"
  },
  {
    "name": "v1.167.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.167.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.167.1",
    "commit": {
      "sha": "b0e374127cd7ec26b28899748107c8ff00bdf40e",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/b0e374127cd7ec26b28899748107c8ff00bdf40e"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY3LjE"
  },
  {
    "name": "v1.167.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.167.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.167.0",
    "commit": {
      "sha": "f4cfdc93983bd05b21edd792beff532b43af0a97",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/f4cfdc93983bd05b21edd792beff532b43af0a97"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY3LjA"
  },
  {
    "name": "v1.166.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.166.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.166.0",
    "commit": {
      "sha": "b533020849e78403282db6434295560ffc3fab03",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/b533020849e78403282db6434295560ffc3fab03"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY2LjA"
  },
  {
    "name": "v1.165.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.165.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.165.0",
    "commit": {
      "sha": "7001f78e669b9617ac21a2f5e6e6165698645afd",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/7001f78e669b9617ac21a2f5e6e6165698645afd"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY1LjA"
  },
  {
    "name": "v1.164.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.164.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.164.0",
    "commit": {
      "sha": "9621001b4235a09a3a3fd8e53dc6332861a9b8b9",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/9621001b4235a09a3a3fd8e53dc6332861a9b8b9"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTY0LjA"
  },
  {
    "name": "v1.163.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.163.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.163.0",
    "commit": {
      "sha": "251adb4e0ed0f59bb93da313257b4a9bd140e01f",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/251adb4e0ed0f59bb93da313257b4a9bd140e01f"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYzLjA"
  },
  {
    "name": "v1.162.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.162.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.162.1",
    "commit": {
      "sha": "2bc5c78d91ee2200ddc37a2135237f11042d6929",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/2bc5c78d91ee2200ddc37a2135237f11042d6929"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYyLjE"
  },
  {
    "name": "v1.162.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.162.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.162.0",
    "commit": {
      "sha": "f2578c958db24d02087005e9fd88e40e2a10f17c",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/f2578c958db24d02087005e9fd88e40e2a10f17c"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYyLjA"
  },
  {
    "name": "v1.161.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.161.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.161.0",
    "commit": {
      "sha": "9916d14adb79a278cc3a3ac96bc166b89bf65184",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/9916d14adb79a278cc3a3ac96bc166b89bf65184"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYxLjA"
  },
  {
    "name": "v1.160.1",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.160.1",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.160.1",
    "commit": {
      "sha": "68c71e1c20866bcde5d10f4eef23c95d4feee5fd",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/68c71e1c20866bcde5d10f4eef23c95d4feee5fd"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYwLjE"
  },
  {
    "name": "v1.160.0",
    "zipball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/zipball/refs/tags/v1.160.0",
    "tarball_url": "https://api.github.com/repos/MetaCubeX/metacubexd/tarball/refs/tags/v1.160.0",
    "commit": {
      "sha": "e38786ce980e385ae61dcc2af6c48186757d1987",
      "url": "https://api.github.com/repos/MetaCubeX/metacubexd/commits/e38786ce980e385ae61dcc2af6c48186757d1987"
    },
    "node_id": "REF_kwDOJ6H0kLJyZWZzL3RhZ3MvdjEuMTYwLjA"
  }
]
# print(res)
version_list=[Version(i["name"]) for i in res]
with open("version","r") as f:
    now_version=Version(f.read())
latest_version=max(version_list)
if latest_version>now_version:
    with open("version","w") as f:
        f.write(str(latest_version))
else:
    sys.exit(2)