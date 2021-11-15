# Домашнее задание №5: Backend Linux

## Python скрипт

Для запуска скрипта на Python необходимо ввести следующую команду:

```
python path_to_access_log
```

где:

```path_to_access_log``` - путь к файлу ```access.log```

Результат выполнения скрипта отобразится в файле ```answer.txt```, который появится в папке с файлом скрипта.

Данный скрипт позволяет выводить данные в формате ```json```. Для этого необходимо при запуске скрипта указать
ключ ```--json```.

```python path_to_access_log --json```

Результат выполнения скрипта отобразится в файле ```answer.json```, который появится в папке с файлом скрипта.

## Bash скрипт

Для запуска скрипта на Bash необходимо ввести следующую команду:

```
chmod +x path_to_script
path_to_script path_to_access_log
```

где:

```path_to_script``` - путь к файлу ```script.sh```
```path_to_access_log``` - путь к файлу ```access.log```

Результат выполнения скрипта отобразится в файле ```result.txt```, который появится в папке с файлом скрипта.

## Вывод

При выводе общего количества запросов по типу была найдена битая строка:

```
g369g=%40eval%01%28base64_decode%28%24_POST%5Bz0%5D%29%29%3B&z0=QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0%2bfCIpOztlY2hvKCJlNTBiNWYyYjRmNjc1NGFmMDljYzg0NWI4YjU4ZTA3NiIpOztlY2hvKCJ8PC0iKTs7ZGllKCk7GET 1
```

Сравнение скриптов на Python и Bash:

### Python

* Подходит для написания больших скриптов
* Более читабельный код

### Bash

* Подходит для написания небольших скриптов
* Меньшее количество кода