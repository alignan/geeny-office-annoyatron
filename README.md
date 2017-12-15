# Geeny's Hackathon

This is the log of our hacking adventures at Geeny's.
TL;DR: we made an application which actually works

The solution we developed (rather a set of problems we came up with) is called the `Geeny's office annoyatron`, a.k.a. How to make friends in the office.

The `annoyatron` consists of two incredible helpful features:

* A friendly reminder over the `team's slack channel` every time a window is opened and closed, lovely isn't?
* Turn a light ON everytime someone is assigned to a new issue, fun! never miss out a Project Manager's ticket!


## The implementation

The implementation is a joint effort from [Geeny](https://www.geeny.io) and [IFTTT](https://www.ifttt.com) to bring happiness over [Slack](https://geenyhackathon.slack.com) and [Github](https://github.com/alignan).

A `Formula` has been deployed to Geeny's Docker registry, based on the [Geeny's Hackathon 2018 repository](https://github.com/geeny/Hackathon2018), with minor modifications:

* Added a `last-msg` endpoint to retrieve the last message only (instead of the whole history at the `/msgs` endpoint)
* Publish to `IFTTT's Webhook` trigger (see: https://ifttt.com/maker_webhooks) 

Overall this is what our architecture looks like:

![img/arch.png](img/arch.png)


### The window friend

Whenever the `Develco's window sensor` detects a window/door has been opened or closed, our `Formula` will publish 

![img/window.png](img/window.png)


### The Issue companion

Whenever there is a new issue assigned by our lovely Project Managers, the light will go ON, quite handy to work those extra overtime hours at night!

![img/github.png](img/github_on.png)

And when it is closed, you can rest assured as the light will go OFF, it is time to go home and enjoy a good few hours of sleep.

![img/github.png](img/github_on.png)

Command example to turn a light ON:
````bash
http://1ffbd1bc-5530-40f4-b7b7-6d1ead22f915-v-22.formula.geeny.io/send-message?thing=bulb&cmd=cmd_on
````


