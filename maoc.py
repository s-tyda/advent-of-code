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

def help_f(test):
    if test == "zero":
        print('Usage: maoc <command> [options] [<args>]\n')
        print("\nCommands:")
        print(
            '   {:<56} {:<s}'.format(
                "dir, d [options] [<args>]", "Makes directory of a year"
            )
        )
        print(
            '   {:<56} {:<s}'.format(
                "check, c [options] [<args>]", "Checks for missing inputs and download them"
            )
        )
        print("\nOptions:")
        print(
            '   {:<56} {:<s}'.format(
                "-h, --help", "Shows usage information"
            )
        )
        print(
            '   {:<56} {:<s}'.format(
                "-l, --list", "Lists all opened years"
            )
        )
        return 1
    elif test == "dir":
        print('Usage: maoc <dir, d> [options] [<args>]\n')
        print("Description:")
        print("This command makes directory of a year.")
        print("\nOptions:")
        print(
            '   {:<56} {:<s}'.format(
                "-h, --help, --pomoc", "Shows usage information"
            )
        )
        print(
            '   {:<56} {:<s}'.format(
                "-y, --year", "Sets a year, default is current year"
            )
        )
        return 1
    elif test == "check":
        print('Usage: maoc <check, c> [options] [<args>]\n')
        print("Description:")
        print("This command checks for missing inputs and download them.")
        print("\nOptions:")
        print(
            '   {:<56} {:<s}'.format(
                "-d, --day", "Sets a day, default is all days of a choosen year"
            )
        )
        print(
            '   {:<56} {:<s}'.format(
                "-h, --help, --pomoc", "Shows usage information"
            )
        )
        print(
            '   {:<56} {:<s}'.format(
                "-y, --year", "Sets a year, default is current year"
            )
        )
        return 1


# Sprawdzanie liczby argumentów
def check_for_args(min_number, max_number, help_string):
    if len(args) == (min_number - 1) or args[min_number - 1] in ('--help', '-h', '--pomoc'):
        help_f(help_string)
        sys.exit(1)
    elif len(args) < min_number:
        print(colored("Too few arguments.\n", 'red', attrs=['bold']))
        help_f(help_string)
        sys.exit(1)
    elif len(args) > max_number:
        print(colored("Too many arguments.\n", 'red', attrs=['bold']))
        help_f(help_string)
        sys.exit(1)


def get_current_year():
    return datetime.now().year


if __name__ == '__main__':
    colorama.init(strip=False)
    global OK
    OK = colored("OK", 'green', attrs=['bold'])
    global args
    args = sys.argv

    # Rozpatrywanie argumentów skryptu
    check_for_args(2, 5, "zero")
    if args[1].startswith("-"):
        if args[1] in ('--list', '-l'):
            check_for_args(2, 2, "zero")
        else:
            help_f("zero")

    elif args[1] in ('dir', 'd'):
        check_for_args(2, 4, "dir")
        if args[2] in ('--year', '-y'):
            check_for_args(4, 4, "dir")
        elif args[2] in ('--help', '-h'):
            help_f("dir")
        # default case - current year
        elif len(args) == 2:
            print("default")
        else:
            help_f("dir")

    elif args[1] in ('check', 'c'):
        check_for_args(2, 6, "check")
        if args[2] in ('--year', '-y'):
            check_for_args(4, 6, "check")
            # Only years passed
            if len(args) == 4:
                print("4")
            # Year and day passed
            else:
                check_for_args(6, 6, "check")
                if args[4] in ('--day', '-d'):
                    print("6")
                else:
                    help_f("check")
        elif args[2] in ('--day', '-d'):
            check_for_args(4, 4, "check")
        elif args[2] in ('--help', '-h'):
            help_f("check")
        # default case - current year
        elif len(args) == 2:
            print("default")
        else:
            help_f("check")
