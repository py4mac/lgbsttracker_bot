<H1>Lgbsttracker Bot Assistant</H1>
<p align="center">
<img src="https://img.shields.io/github/last-commit/py4mac/lgbsttracker-bot.svg">
<a href="https://github.com/py4mac/" target="_blank">
    <img src="https://github.com/py4mac/lgbsttracker-bot/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://codecov.io/gh/py4mac/lgbsttracker-bot" target="_blank">
    <img src="https://codecov.io/gh/py4mac/lgbsttracker-bot/branch/master/graph/badge.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/lgbsttracker-bot" target="_blank">
    <img src="https://badge.fury.io/py/lgbsttracker-bot.svg" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://py4mac.github.io/lgbsttracker-bot" target="_blank">https://py4mac.github.io/lgbsttracker-bot</a>

**Source Code**: <a href="https://github.com/py4mac/lgbsttracker-bot" target="_blank">https://github.com/py4mac/lgbsttracker-bot</a>

---

## Requirements

Python 3.6+


## How to use it?

To train your API bot, execute
```
rasa train
```
This will store a zipped model file in `models/`.

Run an instance of duckling on port 8001
```
docker run -p 8001:8000 rasa/duckling
```

To chat with the bot on the command line, run
```
rasa run actions
rasa shell
```

## Environment variables

| Variable Name |  Description | Default value |
| --- | --- | --- |
| LGBSTTRACKER_API_URI | Lgbsttracker API URI | Mandatory: to be set by the user before using library |

## Credits

* https://github.com/RasaHQ/rasa

## License

This project is licensed under the terms of the MIT license.