import logging
import os
from datetime import datetime
from random import randint

import yaml
from cryptography.fernet import Fernet

from test_cases import test_data

used_numbers = []


def initialize_logger():
    """Initialize logger here"""
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    log.addHandler(console_handler)
    return log


def read_yaml(fpath):
    """Read yaml file and return dictionary/list"""
    if os.path.isfile(fpath):
        with open(fpath) as filein:
            try:
                data = yaml.safe_load(filein)
            except yaml.YAMLError as exc:
                error_msg = "Failed to parse: {}\n{}".format(fpath, str(exc))
                raise Exception(error_msg) from exc
    else:
        error_msg = f"Specified file doesn't exist: {fpath}"
        raise Exception(error_msg)
    return data


def decrypt_file(
    files_to_decrypt=("config/credentials.yaml.encrypted",),
    overwrite=True,
):
    """This method will decrypt files"""
    # Get the key from the file
    file = open("key.key", "rb")
    key = file.read()  # The key will be type bytes
    file.close()

    # Open encrypted files
    for encrypted_file_path in files_to_decrypt:
        decrypted_file_path = os.path.splitext(encrypted_file_path)[0]
        if not overwrite:
            # check if files are already decrypted
            if os.path.exists(decrypted_file_path):
                continue
        with open(encrypted_file_path, "rb") as f:
            data = f.read()

        fernet1 = Fernet(key)
        decrypted = fernet1.decrypt(data)

        # Write the decrypted file
        with open(decrypted_file_path, "wb") as f:
            f.write(decrypted)
        assert os.path.exists(
            decrypted_file_path
        ), "file {} not decrypted".format(encrypted_file_path)


def encrypt_file(
    files_to_encrypt=("config/credentials.yaml",),
):
    """This method will encrypt files"""
    file = open("key.key", "rb")
    key = file.read()  # The key will be type bytes
    file.close()

    # Open the files to encrypt
    for file in files_to_encrypt:
        encrypted_file_path = file + ".encrypted"
        with open(file, "rb") as f:
            data = f.read()

        fernet2 = Fernet(key)
        encrypted = fernet2.encrypt(data)

        # Write the encrypted file
        with open(encrypted_file_path, "wb") as f:
            f.write(encrypted)
        assert os.path.exists(
            encrypted_file_path
        ), "file {} not encrypted".format(file)


def get_random_number():
    """This method generate random number"""
    global used_numbers
    r_num = -1
    while (r_num in used_numbers) or (r_num == -1):
        r_num = randint(1000, 9000)
    return r_num


def generate_random_string(prefix):
    """This method generate random staring"""
    return prefix + str(get_random_number())


def generate_random_watchlist_name():
    """This method generate random watchlist name"""
    data = test_data.WATCHLIST_NAME
    return generate_random_string(data)


def generate_random_portfolio_name():
    """This method generate random portfolio name"""
    data = test_data.PORTFOLIO_NAME
    return generate_random_string(data)


def sanitize_price(input_price_str):
    val = input_price_str.strip("+")
    val = val.strip("-")
    val = val.strip("$")
    val = val.strip("%")
    val = val.replace(",", "")
    return val


def date_formatter(input_date):
    date_obj = datetime.strptime(input_date, "%m/%d/%y")
    return date_obj.strftime("%b %-d, %Y")
