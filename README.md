# Test.Bash-Online AutomationWeek - mobile automation challenge 

This repo shows the solution to the Test.bash('Online') AutomationWeek mobile beginner challenge:

```
Beginner:
Open the Swaglabs App, login to the application, and assert you are logged in.
```
Challenge is based on [Swaglabs App](https://github.com/saucelabs/sample-app-mobile/releases) please download the application before running the project.


## Dependencies

Python 2.7.16\
Pytest 6.1.1\
XCODE + Command Line Tools\
Carthage (iOS dependency manager, install using homebrew)\
Appium 1.18.3


## Installation

Once we have XCODE installed let's open the simulator and check for device name and udid variables using this command:

```
instruments -s devices
```
The above command should pull a list of iOS devices similar to this one: `iPhone 11 (14.1) [5638C6BD-76B0-475D-8E7B-3C178FA4F447] (Simulator)`
where `iPhone 11` is the device name and `5638C6BD-76B0-475D-8E7B-3C178FA4F447` is the udid, let's grab those two parameters and change them within the `config.py` file as follows:

```
"deviceName": "iPhone 11",
"udid": "5638C6BD-76B0-475D-8E7B-3C178FA4F447",
```
Once done that let's replace the `app` parameter with the current location of the Swaglabs App that we downloaded at the beggining of this repo, change should look like this:

```
"app": "/current-app-directory/iOS.Simulator.SauceLabs.Mobile.Sample.app.2.5.0.app",
```

After te previous steps are completed let's start the appium server executing the following command in the terminal:

```
appium
```

Now we should be able to run our tests in our root folder of our project by typing the following command in the terminal:
```
pytest -v -s login_test.py
```



## Contributing
Pull requests are welcome.

Please make sure to update tests and README as appropriate.
