# Follow-Unfollow Notification

## Overview

A script for listing users who followed and unfollowed the account

## Installation
```
pip install git+https://github.com/takanori-pskq/follow-unfollow-notification.git
```

## Usage
First execute `fun_initialize --consumer-key=<consumer key> --consumer-secret=<consumer secret>` to initialize. Then run `fun_notify <twitter screenname> | mail <mail address>` routinely.

## Requirement
This script requires `twurl` command on your system. You can install `twurl` by:
```
gem install twurl
```
You can install required python packages by:
```
pip install docopt xdg
```

## License
This software is released under the MIT License, see `LICENSE.md`.


