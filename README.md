# FIFA 23 FUT Club Analyzer

Get quick insight into your fut club and transfer list prices. Track profits and losses. Export the csv files into your favorite program for more analysis

## Getting Started

### Dependencies

* Requires Python3
-requests
-PYyaml

Install with 
```py -m pip install requests``` and
```py -m pip install pyyaml```


## Authenticating Yourself
* To avoid any security issues or problems with EA, I have chosen not to implement email/password login. In order to authenticate yourself, you will need to put your session ID header value into the config file in /auth/config.yml after signing into the official EA web app or mobile app.
* The sesion ID header is listed as `X-UT-SID` on requests made to the web app. Just copy and paste the value into the auth config.
* The session ID seems to be valid for at least an hour, which is more than enough time to pull your club stats

* To get your sesion ID header, open chrome, sign into the EA web app, then hit ```CTRL+SHIFT+i```. The web app screen might pause and say "paused in debugger". To get around it, click back on the web app and press ```ctrl+F8```. 
![Click the network tab](https://i.imgur.com/aB3JhDZ.png)
* Now just navigate around the web app and you will see the Network tab populate with requests. 
![Click on a request](https://i.imgur.com/lBX0ymF.png)
*Find a request with the X-UT-SID header
![Copy it](https://i.imgur.com/VyE9htH.png)

### Executing program

* Start the program with `py main.py`, `python3 main.py` or whatever else your picky system might be asking for

## Version History
* 0.1
    * Initial Release

## Acknowledgments

* This project would not be possible without the use of [futbin](https://www.futbin.com/) pricing. All futbin integration is done responsibly and poses no danger to the internal systems used to serve their users. A big thank you to the futbin team.
