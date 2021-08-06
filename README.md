# FOSSil 
---
(if someone can add more of those badge things that would be nice)
![https://img.shields.io/matrix/null:kde.org](matrix://#null:kde.org)

## About
FOSSil automatically uses GET requests to download and compress websites.

### Directories used:

`~/.config/fossil/config.toml`: This is the configuration file, the only way to control Fossil. It is discussed more in the config section.

`~/FOSSil`: This is where FOSSil stores archived websites

`~/fossil`: Where the source code is often downloaded. This a development only directory.

### How websites are downloaded
A simple GET request is used to download the HTML source of sites and then archives them into tar.gz files with the site name and UNIX time.

### Editing the configuration file

``title = "fossil config file"``: I don't know what this does, but I'm scared to remove it. I advise letting it be.

`links = "example.org", "subdomian.example.org"`: This is what sites you want to download. Put URLs into double quotes `""` and separate them with commas. Currently only up to ten sites can be added.

`action = "archive"`: This is useless. It will be fixed in a new update. 

`time = "30"`: How many seconds between archives

Best practices: Put quotes around all values (example.org, archive, 30, etc...). Don't put http:// before website names.

### Installation

```
git pull https://github.com/Changeme-NUL/fossil
cd fossil
./install.sh -l #use -g to install for all users
```

### Troubleshooting
Contact me via matrix or start a discussion on Github
