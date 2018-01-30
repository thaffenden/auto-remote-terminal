# Auto Remote Terminal
Send auto remote commands from your terminal to your phone.

This allows you to control anything you usually would using auto remote without even having to reach for your phone.

## Configuration
Clone this repo.

Follow the guide here to get your key: https://joaoapps.com/autoremote/personal and add it to the `config.cfg` file.

Register your device by calling the script with the command 'register'.
e.g.:
> python auto_remote.py register

You should see the device you created showing in auto remote.

Set your message prefix in the config file.

## Sending messages
> python auto_remote.py send --message=<MY_MESSAGE>

Create a test Tasker profile, triggered by an AutoRemote event, with the message filter which matches your message prefix and a command you want to send.

e.g.:

> python auto_remote.py send --message=lights

This sends the command linux=:=lights

I have a profile created in Tasker, which will call an existing task to turn my lights on when it receives this message.


## Bonus points
Make your life even easier by setting up shell aliases for these commands so you can control anything you like with a few keystrokes.
