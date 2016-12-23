#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, json

KEY1 = "Key1"
KEY2 = "Key2"
KEY3 = "Key3"

# Basic template of configuration
DEFAULT_CONF = {'mailbox0':{'username':'',
                            'password':'',
                            'imap_server':'',
                            'imap_port':'993',
                            'smtp_server':'',
                            'smtp_port':'587',
                            'auto_check_freq':60 # in second
                            },
                'settings':{'num_of_mailbox':0, # be supported more than 1 email
                            'auto_check':False,
                            'startup':True
                          }
                }
conf = {} # configurations
dirs = {} # important directories of project
tmp = {} # tmp variables

def init():
    global conf, dirs

    # Initialize dirs
    dirs["console"] = os.getcwd()
    dirs["src"] = os.path.dirname(__file__)
    dirs["config"] = os.path.join(dirs["src"], "config.json")
    dirs["project"] = dirs["src"]
    dirs["res"] = os.path.join(dirs["project"], "res")
    dirs["app_icon"] = os.path.join(dirs["res"], "app_icon.png")
    dirs["tray_icon"] = os.path.join(dirs["res"], "tray_icon.png")
    dirs["mail_icon"] = os.path.join(dirs["res"], "mail_icon.png")

    # Initialize conf
    if os.path.isfile(dirs["config"]):
        try:
            conf = json.load(open('config.json'))
        except:
            print("[!] Config file is not valid. Loading default configurations.")
            set_default_conf()
    else:
        print("[!] There is no config file. I am creating one for you :)")
        set_default_conf()


def set_default_conf():
    global conf
    conf = DEFAULT_CONF.copy()
    save_conf()


def save_conf():
    json.dump(conf, open(dirs["config"], 'w'))


def encrypt(value, k=KEY1):
    if value=="":
        return ""
    return xor(value, k)


def decrypt(value, k=KEY1):
    if value=="":
        return ""
    value = "".join(map(chr, value))
    value = xor(value, k)
    value = "".join(map(chr, value))
    return value


def xor(s, k=KEY1):
    k = k*(int(len(s)/len(k))+1)
    return [ord(s[i]) ^ ord(k[i]) for i in range(len(s))]

init()
