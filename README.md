# chrome-remote

## Summery

Simple remote for chrome / chromium browser. It opens/changes the url chromium is displaying at the moment. Useful for kiosk systems.

## Synopse

I tried to find a program which allows me to change the url of a running chrome instance, or simply to refresh the current web site. After a lot of research I found some code snippets mainly done from-for developers. But nothing useable in a simple ssh command or usable in a webhook. 

So I wrote my own programm.

## Basic Usage

Start a chrome or a chromium browser with the option _remote-debugging-port_

```
chromium --remote-debugging-port=12345
```

Afterwards take call the python script:

```
./chrome-remote https://www.heise.de 
```

## Advanced Usage

Start chromium on the remote system with the option <i>remote-debugging-port</i>. Afterwards clone this repo to a directory of your choise on the remote system (I prefer /opt). 

```
chromium --remote-debugging-port=12345
cd /opt
git clone <this-repo>
```

Ensure you have ssh access to the remote system. Call the script from you local system by using the following ssh command:

```
ssh <remote-user>@<remote-system> '/opt/chrome-remote/chrome-remote.py http://www.heise.de'
```
if your kiosk needs to refresh 

```
ssh <remote-user>@<remote-system> '/opt/chrome-remote/chrome-remote.py refresh'
```

## Installation

### Dependencies

* Arch Linux ```community/python-websocket-client```
* Debian/Ubuntu ```python3-websocket```

### Install to /opt

```
cd /opt
git clone <this-repo>
chown -R <your-username>:<your-username> chrome-remote
chmod 755 chrome-remote/chrome-remote.py
```

### Testing

Tested on the following distributions:

- Arch Linux
- Debian Buster
- Raspbian 

## Help

```
./chrome-remote.py 
Usage: ./chrome-remote.py [ -h ] | [ -p <chrome-remote-port>] <url_to_open> | refresh 

 This programm requires chrome/chromium browser. Start this with the following argument: 
 chromium -remote-debugging-port=12345

 -p remote debugging port (default is 12345)
 
 <url_to_open> e.g. https://www.heise.de
 OR
 refresh
 ```

## Sources

Websocket command for refresh
* https://sakthipriyan.com/2016/02/15/auto-refresh-chrome-when-files-modified.html

Remote open url
* https://stackoverflow.com/questions/52783655/use-curl-with-chrome-remote-debugging

Websocat
* https://github.com/vi/websocat


Misc
* https://github.com/lvancrayelynghe/chrome-remote-reload
* https://stackoverflow.com/questions/31340063/how-to-change-url-on-chromium-kiosk-mode-via-ssh












