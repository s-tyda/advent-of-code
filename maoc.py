#!/usr/bin/env python3
from datetime import datetime
import time
import sys
import os.path
import subprocess
from configparser import ConfigParser
from pathlib import Path
from cryptography.fernet import Fernet
from shutil import copyfile
import fire
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from rich.console import Console
from rich.table import Table
from rich import print
from rich.panel import Panel
from rich.text import Text
import textwrap
from tkinter import Tk


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


def get_childs(element):
    return element.find_elements_by_xpath("./child::*")


def read_day(year, day):
    open_day_page(year, day)
    text = driver.find_elements_by_class_name("day-desc")
    for part in text:
        childs = get_childs(part)
        for child in childs:
            desc = str(child.text)
            if child.tag_name == "pre":
                print(desc)
                print()
            elif child.tag_name == "ul":
                rows = get_childs(child)
                for row in rows:
                    row = textwrap.wrap(row.text, width=75, initial_indent="  - ", subsequent_indent="    ")
                    for i in row:
                        print(Text(i))
                print()
            else:
                if desc.startswith("---"):
                    print(Text(desc, style="red"))
                else:
                    desc = textwrap.wrap(desc, width=75)
                    for i in desc:
                        print(Text(i))
                print()


def get_test(year, day, n, part, mode):
    n = add_zero(n)
    driver.get(f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_{day}/Part_{part}/test{n}_{mode}.txt")
    test = str(driver.find_element_by_tag_name("body").text)
    if test == "404: Not Found":
        return False
    else:
        return test


def add_zero(n):
    if n < 10:
        return "0" + str(n)
    else:
        return n


# def get_test_day(year, day):
#     day = add_zero(day)
#     make_missing_directories(f"Test_Inputs/{year}/Day_{day}/Part_1")
#     make_missing_directories(f"Test_Inputs/{year}/Day_{day}/Part_2")
#     i = 1
#     check = get_test(year, day, i, 1, "i")
#     while check:
#         if i < 10:
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_1/test0{i}_i.txt")
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_1/test0{i}_o.txt")
#         else:
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_1/test{i}_i.txt")
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_1/test{i}_o.txt")
#     i = 1
#     check = get_test(year, day, i, 2, "i")
#     while check:
#         if i < 10:
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_2/test0{i}_i.txt")
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_2/test0{i}_o.txt")
#         else:
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_2/test{i}_i.txt")
#             driver.get(
#                 f"https://raw.githubusercontent.com/s-tyda/Advent-of-Code/master/Test_Inputs/{year}/Day_0{day}/Part_2/test{i}_o.txt")
#     with open(data, "w") as file:
#         file.write(get_text_input())


# def get_test_data(year, day):
#     if day == 0:
#         for i in range(1, 26):
#             get_test_day(year, i)
#     else:
#         get_test_day(year, day)


def send_answer(year, day, answer):
    open_day_page(year, day)
    inputs = driver.find_elements_by_tag_name("input")
    form = inputs[1]
    form.click()
    form.send_keys(answer)
    form.submit()
    output = driver.find_element_by_tag_name("article")
    output = str(get_childs(output)[0].text)
    output = textwrap.wrap(output, width=75)
    for i in output:
        words = i.split()
        if words[1] == "not":
            print(Text.assemble((i[:28], "bright_red"), i[28:]))
        elif words[1] == "the":
            print(Text.assemble((i[:24], "bright_green"), i[24:]))
            update_day(year, day, userinfo)
        else:
            print(i)


def test_f(file, part, year, day):
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
    def test(file, part, year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return test_f(file, part, year, day)

    @staticmethod
    def t(file, part, year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return test_f(file, part, year, day)

    @staticmethod
    def send(answer, year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return send_answer(year, day, answer)

    @staticmethod
    def s(answer, year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return send_answer(year, day, answer)

    @staticmethod
    def read(year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return read_day(year, day)

    @staticmethod
    def r(year=get_current_year(), day=0):
        if day == 0:
            day = get_next_day(year, userinfo)
        return read_day(year, day)

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
            print(f"[bold red]{p}[/bold red]", end="")
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
    for idx, i in enumerate(stats):
        if i != "2":
            return idx+1
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
            "It seems it's your first time using maoc script. You have"
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
    fire.Fire(CLI)
    # print_config(key, user_config)
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
