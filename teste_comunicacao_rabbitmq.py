# -*- coding: utf-8 -*-
import os
import re
import sys
import cv2
import json
import time
import argparse
import numpy as np
import math
import statistics
import pika
import io
from utils import load_options
from utils import to_labels_array, to_labels_dict
from video_loader import MultipleVideoLoader
from is_wire.core import Logger
from collections import defaultdict, OrderedDict
from utils import get_np_image
#from PIL import ImageGrab
from is_msgs.image_pb2 import ObjectAnnotations
from is_msgs.image_pb2 import HumanKeypoints as HKP
from google.protobuf.json_format import ParseDict
from itertools import permutations
import pandas as pd
import sys

sys.argv += 'arg1 arg2'.split()
data = sys.argv 

def send_information(message):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='Receive_information')
    channel.basic_publish(exchange='', routing_key='Receive_information', body =json.dumps({'dict': message}).encode('utf-8'))
    #channel.basic_consume(queue='Receive_information', on_message_callback=callback, auto_ack=True)
    #channel.start_consuming()
    print("Enviado")
    connection.close()

options = load_options(print_options=False)

if not os.path.exists(options.folder):
    log.critical("Folder '{}' doesn't exist", options.folder)

while True:
    with io.open(options.folder+'PARTICIPANTE_{}/{}/p001g01_3d.json'.format(data[0],data[1])) as json_file:
        message = json.load(json_file)
    print(message)
    send_information(message)
    response=input("Desejada enviar novamente? S ou N ")
    if response=="N":
        break
