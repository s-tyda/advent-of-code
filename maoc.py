#!/usr/bin/env python3
from datetime import datetime
import colorama
import getpass
import mechanize
import time
from bs4 import BeautifulSoup
import sys
import os.path
import subprocess
from termcolor import colored
from configparser import ConfigParser
from pathlib import Path
from cryptography.fernet import Fernet
from shutil import copyfile
import fire
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException


# def help_f(test):
#     if test == "zero":
#         print('Usage: maoc <command> [options] [<args>]\n')
#         print("\nCommands:")
#         print(
#             '   {:<56} {:<s}'.format(
#                 "dir, d [options] [<args>]", "Makes directory of a year"
#             )
#         )
#         print(
#             '   {:<56} {:<s}'.format(
#                 "check, c [options] [<args>]", "Checks for missing inputs and download them"
#             )
#         )
#         print("\nOptions:")
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-h, --help", "Shows usage information"
#             )
#         )
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-l, --list", "Lists all opened years"
#             )
#         )
#         return 1
#     elif test == "init":
#         print('Usage: maoc <init, i> [options] [<args>]\n')
#         print("Description:")
#         print("This command initialize directory of a year.")
#         print("\nOptions:")
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-h, --help, --pomoc", "Shows usage information"
#             )
#         )
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-y, --year", "Sets a year, default is current year"
#             )
#         )
#         return 1
#     elif test == "check":
#         print('Usage: maoc <check, c> [options] [<args>]\n')
#         print("Description:")
#         print("This command checks for missing inputs and download them.")
#         print("\nOptions:")
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-d, --day", "Sets a day, default is all days of a choosen year"
#             )
#         )
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-h, --help, --pomoc", "Shows usage information"
#             )
#         )
#         print(
#             '   {:<56} {:<s}'.format(
#                 "-y, --year", "Sets a year, default is current year"
#             )
#         )
#         return 1


# Sprawdzanie liczby argumentów
# def check_for_args(min_number, max_number, help_string):
#     if len(args) == (min_number - 1) or args[min_number - 1] in ('--help', '-h', '--pomoc'):
#         help_f(help_string)
#         sys.exit(1)
#     elif len(args) < min_number:
#         print(colored("Too few arguments.\n", 'red', attrs=['bold']))
#         help_f(help_string)
#         sys.exit(1)
#     elif len(args) > max_number:
#         print(colored("Too many arguments.\n", 'red', attrs=['bold']))
#         help_f(help_string)
#         sys.exit(1)


def get_current_year():
    year = datetime.now().year
    month = datetime.now().month
    if month < 12:
        return year-1
    else:
        return year


def get_current_day():
    return datetime.now().day


def check_day(year, day):
    if day < 10 and not os.path.exists(data := f"{year}/Day_0{day}/data.txt"):
        # os.makedirs(f"{year}/Day_0{day}", exist_ok=True)
        make_missing_directories(f"{year}/Day_0{day}")
        open_input_page(year, day)
        with open(data, "w") as file:
            file.write(get_text_input())
    elif 10 <= day and not os.path.exists(data := f"{year}/Day_{day}/data.txt"):
        # os.makedirs(f"{year}/Day_{day}", exist_ok=True)
        make_missing_directories(f"{year}/Day_{day}")
        open_input_page(year, day)
        with open(data, "w") as file:
            file.write(get_text_input())


def check_year(year, day):
    login(cookie)
    if day == 0:
        for i in range(1, 26):
            check_day(year, i)
    else:
        check_day(year, day)


def initialize(year):
    os.makedirs(f"{year}", exist_ok=True)
    for i in range(1, 26):
        if i < 10:
            os.makedirs(f"{year}/Day_0{i}", exist_ok=True)
            copyfile("day_template.py", f"{year}/Day_0{i}/day{i}.py")
        else:
            os.makedirs(f"{year}/Day_{i}",  exist_ok=True)
            copyfile("day_template.py", f"{year}/Day_{i}/day{i}.py")
    check_year(year, 0)


def read_f(year, day):
    return "Checking year " + str(year) + " and day " + str(day)


def test_f(file, part, year, day):
    return "File: " + str(file) + " part: " + str(part) + " year " + str(year) + " and day " + str(day)


def send_f(file, part, year, day):
    return "File: " + str(file) + " part: " + str(part) + " year " + str(year) + " and day " + str(day)


def leaderboard_f(update=False, all=False, list=False):
    if update:
        return "Updating"
    elif all:
        return "all"
    elif list:
        return "Listing"
    else:
        return "Empty"


class CLI(object):

    @staticmethod
    def init(year=get_current_year()):
        # return "Initializaing year " + str(year)
        return initialize(year)

    @staticmethod
    def i(year=get_current_year()):
        return initialize(year)

    @staticmethod
    def check(year=get_current_year(), day=0):
        return check_year(year, day)

    @staticmethod
    def c(year=get_current_year(), day=0):
        return check_year(year, day)

    @staticmethod
    def test(file, part, year=get_current_year(), day=get_current_day()):
        return test_f(file, part, year, day)

    @staticmethod
    def t(file, part, year=get_current_year(), day=get_current_day()):
        return test_f(file, part, year, day)

    @staticmethod
    def send(file, part, year=get_current_year(), day=get_current_day()):
        return send_f(file, part, year, day)

    @staticmethod
    def s(file, part, year=get_current_year(), day=get_current_day()):
        return send_f(file, part, year, day)

    @staticmethod
    def read(year=get_current_year(), day=get_current_day()):
        return read_f(year, day)

    @staticmethod
    def r(year=get_current_year(), day=get_current_day()):
        return read_f(year, day)

    @staticmethod
    def leaderboard(update=False, all=False, list=False):
        return leaderboard_f(update, all, list)

    @staticmethod
    def l(update=False, all=False, list=False):
        return leaderboard_f(update, all, list)


def file_encrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        original = file.read()

    encrypted = f.encrypt(original)

    with open(file_path, 'wb') as file:
        file.write(encrypted)


def file_decrypt(key, file_path):
    f = Fernet(key)

    with open(file_path, 'rb') as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    with open(file_path, 'wb') as file:
        file.write(decrypted)


# Otworzenie strony głównej
def open_main_page(driver):
    driver.get("https://adventofcode.com")


def open_event_page(year):
    driver.get(f"https://adventofcode.com/{year}")


def open_day_page(year, day):
    driver.get(f"https://adventofcode.com/{year}/day/{day}")


def open_input_page(year, day):
    driver.get(f"https://adventofcode.com/{year}/day/{day}/input")


def make_missing_directories(path):
    os.makedirs(path, exist_ok=True)


def login(session_cookie):
    # options = Options()
    # options.headless = True
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(options=options)
    driver = initalize_driver()
    open_main_page(driver)
    driver.add_cookie({"name": "session",
                       "value": f"{session_cookie}"})
    driver.refresh()
    if driver.title.startswith("Advent of Code"):
        print("Gitara")
    else:
        print("Error")
    return driver


def get_text_input():
    return driver.find_element_by_tag_name("pre").text


def print_config(key, user_config):
    file_decrypt(key, user_config)
    f = open(user_config, 'r')
    for p in f:
        if p.startswith('[') or p.endswith(']'):
            print(colored(p, 'red', attrs=['bold']), end="")
        else:
            print(p, end="")
    file_encrypt(key, user_config)


def write_config(key, user_config, userinfo, option, new):
    userinfo[option] = new
    file_decrypt(key, user_config)
    with open(user_config, 'w') as conf:
        config_object.write(conf)
    file_encrypt(key, user_config)


def clear_leaderboards(userinfo):
    write_config(key, user_config, userinfo, "private_leaderboards", "")


def add_leaderboard(leaderboard_id, userinfo):
    result = userinfo["private_leaderboards"] + f",{leaderboard_id}"
    result = result.strip(",")
    write_config(key, user_config, userinfo, "private_leaderboards", result)


def update_day(year, day, userinfo):
    result = userinfo[f"{year}"]
    idx = (day - 1) * 2
    result = result[:idx] + str(int(result[idx]) + 1) + result[(idx + 1):]
    write_config(key, user_config, userinfo, str(year), result)


def update_year(year):
    result = ""
    for i in range(1, 26):
        open_day_page(year, i)
        try:
            x = str(driver.find_element_by_class_name("day-success").text)
            if x.endswith("**"):
                result += "2,"
            elif x.endswith("*"):
                result += "1,"
        except NoSuchElementException:
            result += "0,"
    return result.strip(",")


def update_stats(year=0):
    if year == 0:
        for i in range(2015, get_current_year()+1):
            result = update_year(i)
            write_config(key, user_config, userinfo, str(i), result)
    else:
        result = update_year(year)
        write_config(key, user_config, userinfo, str(year), result)


def get_pic(year):
    open_event_page(year)
    for i in [i.text for i in driver.find_element_by_tag_name("main").find_elements_by_tag_name("a")]:
        print(i[-2])


def get_next_day(year, userinfo):
    stats = userinfo[f"{year}"].split(",")
    for i in stats:
        if i != "2":
            return i
    print(f"All days in year {year} are completed!")
    sys.exit(0)


def initalize_driver():
    options = Options()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(options=options)


if __name__ == '__main__':
    user_config_dir = str(Path.home()) + "/.config/maoc"
    user_config = user_config_dir + "/config.ini"
    key_path = user_config_dir + "/.key"

    if not os.path.exists(user_config):
        print(
            "It seems it's your first time using tichy script. You have"
            " to set your config to proceed.\n"
        )
        cookie = input("Your session cookie: ")
        make_missing_directories(user_config_dir)
        key = Fernet.generate_key()
        with open(key_path, 'wb') as mykey:
            mykey.write(key)
        with open(user_config, "w") as f:
            f.write("[CONFIG]\n")
            f.write("session_cookie = " + cookie + '\n')
            f.write("private_leaderboards = \n")
            for year in range(2015, get_current_year() + 1):
                f.write(f"{year} = \n")
        file_encrypt(key, user_config)
        print("Now you can proceed with running a script.")
        sys.exit(0)

    # Odczytanie danych z konfiguracji
    with open(key_path, 'rb') as mykey:
        key = mykey.read()
    file_decrypt(key, user_config)
    config_object = ConfigParser()
    config_object.read(user_config)
    file_encrypt(key, user_config)

    # Dane
    userinfo = config_object["CONFIG"]
    cookie = userinfo["session_cookie"]
    leaderboards_ids = userinfo["private_leaderboards"].split(",")
    stats = userinfo["2020"].split(",")

    driver = login(cookie)
    # fire.Fire(CLI)
    # colorama.init(strip=False)
    # global OK
    # OK = colored("OK", 'green', attrs=['bold'])
    # global args
    # args = sys.argv
    #
    # check_for_args(2, 7, "zero")
    # if args[1].startswith("-"):
    #     if args[1] in ('--list', '-l'):
    #         check_for_args(2, 2, "zero")
    #     else:
    #         help_f("zero")
    #
    # elif args[1] in ('init', 'i'):
    #     check_for_args(2, 4, "init")
    #     if args[2] in ('--year', '-y'):
    #         check_for_args(4, 4, "init")
    #     elif args[2] in ('--help', '-h'):
    #         help_f("init")
    #     # default case - current year
    #     elif len(args) == 2:
    #         print("default")
    #     else:
    #         help_f("init")
    #
    # elif args[1] in ('check', 'c'):
    #     check_for_args(2, 6, "check")
    #     if args[2] in ('--year', '-y'):
    #         check_for_args(4, 6, "check")
    #         # Only years passed
    #         if len(args) == 4:
    #             print("4")
    #         # Year and day passed
    #         else:
    #             check_for_args(6, 6, "check")
    #             if args[4] in ('--day', '-d'):
    #                 print("6")
    #             else:
    #                 help_f("check")
    #     elif args[2] in ('--day', '-d'):
    #         check_for_args(4, 4, "check")
    #     elif args[2] in ('--help', '-h'):
    #         help_f("check")
    #     # default case - current year
    #     elif len(args) == 2:
    #         print("default")
    #     else:
    #         help_f("check")
    #
    # elif args[1] in ('check', 'c'):
    #     check_for_args(2, 6, "check")
    #     if args[2] in ('--year', '-y'):
    #         check_for_args(4, 6, "check")
    #         # Only years passed
    #         if len(args) == 4:
    #             print("4")
    #         # Year and day passed
    #         else:
    #             check_for_args(6, 6, "check")
    #             if args[4] in ('--day', '-d'):
    #                 print("6")
    #             else:
    #                 help_f("check")
    #     elif args[2] in ('--day', '-d'):
    #         check_for_args(4, 4, "check")
    #     elif args[2] in ('--help', '-h'):
    #         help_f("check")
    #     # default case - current year
    #     elif len(args) == 2:
    #         print("default")
    #     else:
    #         help_f("check")
