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

## Environment variables

| Variable Name |  Description | Default value |
| --- | --- | --- |
| LGBSTTRACKER_API_URI | Lgbsttracker API URI | Mandatory: to be set by the user before using library |

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

## Example dialog flow

```
Your input ->  Hi                                                                                  
Hello! I am API search assistant! How can I help?
Your input ->  Can I get table values                                                              
what table?
Your input ->  experiments                                                                         
how many entries?
Your input ->  2                                                                                   
/usr/local/lib/python3.7/site-packages/rasa/utils/common.py:351: UserWarning: Interpreter parsed an entity 'number' which is not defined in the domain. Please make sure all entities are listed in the domain.
  More info at https://rasa.com/docs/rasa/core/domains/
{'experiment_uuid': 'experiment1', 'ts': '2020-04-01T16:53:09.444218', 'action': 'none', 'vision_sensor': None, 'speed': None, 'state': 'stopped', 'id': 1}
I've made a request using the following parameters:
 - table: experiments
 - num_entries: 2
```

## Credits

* https://github.com/RasaHQ/rasa

## License

This project is licensed under the terms of the MIT license.