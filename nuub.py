#!/usr/bin/python3
import os
from core.banner import logo
from core.help import help


if __name__ == "__main__":
	os.system('tput setaf 5')
	logo()
	os.system('tput setaf 2')
	help()


