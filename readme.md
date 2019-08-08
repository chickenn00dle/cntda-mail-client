# Simple Mail Client implementation for Computer Networking: A Top Down Approach

A mail client built with python (Chapter 2 assignment for Computer Networking: A Top Down Approach). The client will only send text and has only been tested with Gmails smtp.gmail.com mail server.

## Getting Started

### Prerequisites

The project runs on Python 3+ so you'll need to make sure this is installed.

```
python3 --version
```

Should result in something like:

```
Python 3.7.4
```

If not, you can get set up with the latest version of Python here: https://www.python.org/downloads/

### Installing

Clone the project and give it a name

```
git clone phttps://github.com/chickenn00dle/cntda-udp-pinger.git [project-name]
cd [project-name]
```

And that's it. You have everything you need to get started.

## Running the tests

To send an email using gmail, you'll want to set up a development email account following these steps:

- Create a new Gmail account: [#](https://accounts.google.com/signup/v2)
- Allow less secure apps to access this account: [#](https://devanswers.co/allow-less-secure-apps-access-gmail-account/)

Once you've done the above, you run the app with the following command:

```
./mail-client.py [_email address from above_] [_mail server_]
```

So for example:

```
./mail-client.py example@test.com smtp.gmail.com
```

The client will then prompt you for the password for your development email address, a recipient, subject, and message content.

Go ahead and send an email to yourself to test things out!

## Authors

* **Rasmy Nguyen** - [@chickenn00dle](https://twitter.com/ChickenN00dle)

## License

This project is licensed under the MIT License - see the [Open Source Initiative](https://opensource.org/licenses/MIT) for details

## Acknowledgments

Big shout out to @davidshepherd7 for providing some templates for the Computer Networking: A Top Down Approach projects here: https://github.com/davidshepherd7/Kurose-and-Ross-socket-programming-exercises

