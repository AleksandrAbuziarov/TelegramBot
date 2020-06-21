#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import requests
from requests.exceptions import Timeout
import telebot
from telebot import apihelper
from opcua import Client
import threading
from threading import Thread
import logging
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from pyngrok import ngrok

app = Flask(__name__)

# Paramms OPC
url = "opc.tcp://10.4.37.2:4840"
client = Client(url)
# Paramms Telegram
# https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/setWebhook?url=https://cf10c57a.ngrok.io/
CHANNEL_NAME1 = '@MILKOMTEST'
apihelper.proxy = {'https': 'https://NsY4C3:ZPYqX7@186.179.51.64:8000'}
CHANNEL_NAME_PET1 = '@Milkom_PET1'
CHANNEL_NAME_PET2 = '@Milkom_PET2'
CHANNEL_NAME_PET3 = '@Alarm_PET'
token = '1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo'
bot = telebot.TeleBot('1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo')

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=["POST", "GET"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http = requests.Session()
http.mount("https://", adapter)
http.mount("http://", adapter)
# logger
if __name__ == '__main__':
    # Get rid of spam in the logs from the requests library
    logging.getLogger('requests').setLevel(logging.CRITICAL)
    # Logger setup
    logging.basicConfig(format='[%(asctime)s] %(filename)s:%(lineno)d %(levelname)s - %(message)s', level=logging.ERROR,
                        filename='Error_TelegramBotV1_4.log', datefmt='%d.%m.   %Y %H:%M:%S')

def send_message():
    try:
        method = "sendMessage"
        url = "https://api.telegram.org/bot{bot}/{sendMessage}"
        data = bot.send_message(chat_id=CHANNEL_NAME1, text="Тест связи")
        requests.post(url, timeout=0.4, proxies=apihelper.proxy)
    except requests.Timeout:
        pass
    except requests.ConnectionError:
        pass
    except Exception as e:
        print(e)
        pass


# Send Message
@bot.message_handler(content_types=['text'])
def get_text_messages_line1(OEE, Performance, Quality, Availability, DateStart, DateEnd, ValueChange, User_Line1):
    try:
        if ValueChange:
            method = "sendMessage"
            url = "https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage"
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1, text="ПЭТ 1:"'''
"Оператор:''' + " " + str(User_Line1) + '''
"Начало смены:''' + " " + str(DateStart) + ''' 
Окончание смены:''' + " " + str(DateEnd) + '''      
OEE''' + " " + "=" + " " + str(OEE) + '''
Performance''' + " " + "=" + " " + str(Performance) + '''
Quality''' + " " + "=" + " " + str(Quality) + '''
Availability''' + " " + "=" + " " + str(Availability))
            requests.post(url, timeout=1, proxies=apihelper.proxy)

    except requests.Timeout:
        pass
       # return get_text_messages_line1(OEE, Performance, Quality, Availability, DateStart, DateEnd, 1, User_Line1)
    except requests.ConnectionError:
        logging.error("Error send")
        print ("Error")
        pass
        #return get_text_messages_line1(OEE, Performance, Quality, Availability, DateStart, DateEnd, 1, User_Line1)
    except Exception as e:
        logging.error(e)
        print(e)
        pass
        #return get_text_messages_line1(OEE, Performance, Quality, Availability, DateStart, DateEnd, 1, User_Line1)


def get_text_messages_line2(OEE_Line2, Performance_OPC_Line2, Quality_OPC_Line2, Availability_Line2, DateStart_Line2,
                            DateEnd_Line2, ValueChange_Line2, User_Line2):
    try:
        if ValueChange_Line2:
            method = "sendMessage"
            url = "https://api.telegram.org/bot{bot}/{sendMessage}"
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2, text="ПЭТ 2:"'''
"Оператор:''' + " " + str(User_Line2) + '''
"Начало смены:''' + " " + str(DateStart_Line2) + ''' 
Окончание смены:''' + " " + str(DateEnd_Line2) + '''      
OEE''' + " " + "=" + " " + str(OEE_Line2) + '''
Performance''' + " " + "=" + " " + str(Performance_OPC_Line2) + '''
Quality''' + " " + "=" + " " + str(Quality_OPC_Line2) + '''
Availability''' + " " + "=" + " " + str(Availability_Line2))
            requests.post(url, timeout=1, proxies=apihelper.proxy)
    except requests.Timeout:
        pass
  #      return get_text_messages_line1(OEE_Line2, Performance_OPC_Line2, Quality_OPC_Line2, Availability_Line2,
     #                                  DateStart_Line2, DateEnd_Line2, 1, User_Line2)
    except requests.ConnectionError:
        logging.error("Error send")
        pass
   #     return get_text_messages_line1(OEE_Line2, Performance_OPC_Line2, Quality_OPC_Line2, Availability_Line2,
      #                                 DateStart_Line2, DateEnd_Line2, 1, User_Line2)
    except Exception as e:
        logging.error(e)
        print(e)
        pass
    #    return get_text_messages_line1(OEE_Line2, Performance_OPC_Line2, Quality_OPC_Line2, Availability_Line2,
       #                                DateStart_Line2, DateEnd_Line2, 1, User_Line2)


def help_line1(Help_OPC_Line1):
    try:
        if Help_OPC_Line1:
            method = "sendMessage"
            url = "https://api.telegram.org/bot{bot}/{sendMessage}"
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1,
                                    text="На ПЭТ 1 произошла АВАРИЯ! Оператору требуется помощь инженера!")
            requests.post(url, timeout=1, proxies=apihelper.proxy)
    # except requests.Timeout:
    # print("Timeout")
    # pass
    #  return help_line1(1)
    except requests.ConnectionError:
        logging.error("Error send")
        print("Error")
        pass
        #return help_line1(1)
    except requests.Timeout:
        print("Timeout")
        pass
        #return help_line1(1)
    except Exception as e:
        logging.error(e)
        print("Except")
        print(e)
        pass
        #return help_line1(1)



def help_line2(Help_OPC_Line2):
    try:
        if Help_OPC_Line2:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2,
                                    text="На ПЭТ 2 произошла АВАРИЯ! Оператору требуется помощь инженера!")
            requests.post(url, timeout=1, proxies=apihelper.proxy)
    except requests.Timeout:
        print("Timeout")
        pass
       # return help_line2(1)
    except requests.ConnectionError:
        logging.error("Error send")
        print("Error")
        pass
       # return help_line2(1)
    except Exception as e:
        logging.error(e)
        print("Except")
        print(e)
        pass
       # return help_line2(1)


def downtime_line1(Downtime_OPC_Line1, IndexDowntimeMachine_OPC_Line1, count_line1):
    switcher_line1 = {
        1: "Выдувной машины 1",
        2: "Машины розлива",
        3: "Этикеровочной машины",
        4: "Упаковочной машины",
        5: "Выдувной машины 2",
    }
    machine = switcher_line1.get(IndexDowntimeMachine_OPC_Line1)
    try:
        if Downtime_OPC_Line1 and count_line1 == 1:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET3,
                                    text="На ПЭТ 1 произошла авария" + " " + str(
                                        machine) + " " + "(длительность аварии 1 минута)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

        elif Downtime_OPC_Line1 and count_line1 == 15:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1,
                                    text="На ПЭТ 1 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии 15 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

        elif Downtime_OPC_Line1 and count_line1 == 30:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1,
                                    text="На ПЭТ 1 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии 30 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)
        elif Downtime_OPC_Line1 and count_line1 == 60:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1,
                                    text="На ПЭТ 1 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительсноть аварии 60 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

        elif Downtime_OPC_Line1 and count_line1 > 60:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET1,
                                    text="На ПЭТ 1 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии более 60 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)


    except requests.Timeout:
        print("Timeout")
        pass
     #   return downtime_line1(1, IndexDowntimeMachine_OPC_Line1, count_line1)
    except requests.ConnectionError:
        logging.error("Error send")
        print("Error")
        pass
      #  return downtime_line1(1, IndexDowntimeMachine_OPC_Line1, count_line1)
    except Exception as e:
        logging.error(e)
        print("Except")
        print(e)
        pass
       # return downtime_line1(1, IndexDowntimeMachine_OPC_Line1, count_line1)


def downtime_line2(Downtime_OPC_Line2, IndexDowntimeMachine_OPC_Line2, count_line2):
    switcher_line2 = {
        1: "Выдувной машины",
        2: "Машины розлива",
        3: "Этикеровочной машины",
        4: "Упаковочной машины",
        5: "Машины установки ручек",
    }
    machine = switcher_line2.get(IndexDowntimeMachine_OPC_Line2)
    try:
        if Downtime_OPC_Line2 and count_line2 == 1:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET3,
                                    text="На ПЭТ 2 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии 1 минута)")
            requests.post(url, timeout=1, proxies=apihelper.proxy )

        elif Downtime_OPC_Line2 and count_line2 == 15:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2,
                                    text="На ПЭТ 2 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии 15 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

        elif Downtime_OPC_Line2 and count_line2 == 30:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2,
                                    text="На ПЭТ 2 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительсноть аварии 30 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)
        elif Downtime_OPC_Line2 and count_line2 == 60:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2,
                                    text="На ПЭТ 2 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии 60 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

        elif Downtime_OPC_Line2 and count_line2 > 60:
            method = "sendMessage"
            url = 'https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/sendMessage'
            data = bot.send_message(chat_id=CHANNEL_NAME_PET2,
                                    text="На ПЭТ 2 поизошла авария" + " " + str(
                                        machine) + " " + "(Длительность аварии более 60 минут)")
            requests.post(url, timeout=1, proxies=apihelper.proxy)

    except requests.Timeout:
        print("Timeout")
        pass
      #  return downtime_line2(1, IndexDowntimeMachine_OPC_Line2, count_line2)
    except requests.ConnectionError:
        logging.error("Error send")
        print("Error")
        pass
       # return downtime_line2(1, IndexDowntimeMachine_OPC_Line2, count_line2)
    except Exception as e:
        logging.error(e)
        print("Except")
        print(e)
        pass
        #return downtime_line2(1, IndexDowntimeMachine_OPC_Line2, count_line2)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        # chat_id = request.json["message"]["chat"]["id"]
        # weather = 25
        send_message()
    return {"ok": True}

class new_value():

    def __init__(self):
        # OPC
        self.dateprev = ()
        self.user_OPC = ()
        self.OEE_OPC = ()
        self.Date_OPC = ()
        self.Date_OPCEnd = ()
        self.Availability_OPC = ()
        self.Performance_OPC = ()
        self.Quality_OPC = ()
        self.Help_OPC_Line1 = ()
        self.Downtime_OPC_Line1 = ()
        self.IndexDowntimeMachine_OPC_Line1 = ()
        self.dateprev_Line2 = ()
        self.user_OPC_Line2 = ()
        self.OEE_OPC_Line2 = ()
        self.Date_OPC_Line2 = ()
        self.Date_OPCEnd_Line2 = ()
        self.Availability_OPC_Line2 = ()
        self.Performance_OPC_Line2 = ()
        self.Quality_OPC_Line2 = ()
        self.Help_OPC_Line2 = ()
        self.Downtime_OPC_Line2 = ()
        self.IndexDowntimeMachine_OPC_Line2 = ()

        # Time
        self.start_time_line1 = time.time()
        self.count_line1 = 0
        self.one_line1 = ()
        self.two_line1 = ()
        self.three_line1 = ()
        self.four_line1 = ()
        self.five_line1 = ()
        self.start_time_line2 = time.time()
        self.count_line2 = 0
        self.one_line2 = ()
        self.two_line2 = ()
        self.three_line2 = ()
        self.four_line2 = ()
        self.five_line2 = ()
        self.get_json_ =()
        self.get_json_two_try = 0

        #Start Thread
        self.t1 = Thread(target=self.opc, args=(), name='opc')
        self.t1.start()
        self.t2 = Thread(target=self.check_new_value, args=(), name='check_value')
        self.t2.start()
        self.t3 = Thread(target=self.check_new_value_line_2, args=(), name='check_value_line2')
        self.t3.start()
        t4 = Thread(target=app.run, name='app')
        t4.start()
        t5 = Thread(target=self.th, args=(), name='restart')
        t5.start()


    def opc(self):
        while True:
            try:
                client.connect()
                # Shift OEE(Line1)
                Date = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.StartTime")
                self.Date_OPC = Date.get_value()
                # Date_OPC = input()
                DateEnd = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.EndTime")
                self.Date_OPCEnd = DateEnd.get_value()
                UserLine1 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.AssetInt.User")
                self.user_OPC = UserLine1.get_value()
                OEE = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.OEE")
                self.OEE_OPC = OEE.get_value()
                Availability = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.Availability")
                self.Availability_OPC = Availability.get_value()
                Performance = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.Performance")
                self.Performance_OPC = Performance.get_value()
                Quality = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.LINE.MpOEE.ListUI.Quality")
                self.Quality_OPC = Quality.get_value()
                # Help
                Help_Line1 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.EnginHelp")
                self.Help_OPC_Line1 = Help_Line1.get_value()
                # Downtime
                DowntimeLine1 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.Down_Time")
                self.Downtime_OPC_Line1 = DowntimeLine1.get_value()
                DowntimeIndexMachineLine1 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_1.IndexDownTimeMachine")
                self.IndexDowntimeMachine_OPC_Line1 = DowntimeIndexMachineLine1.get_value()

                # Shift OEE(Line 2)
                Date_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.StartTime")
                self.Date_OPC_Line2 = Date_Line2.get_value()
                DateEnd_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.EndTime")
                self.Date_OPCEnd_Line2 = DateEnd_Line2.get_value()
                UserLine2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.AssetInt.User")
                self.user_OPC_Line2 = UserLine2.get_value()
                OEE_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.OEE")
                self.OEE_OPC_Line2 = OEE_Line2.get_value()
                Availability_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.Availability")
                self.Availability_OPC_Line2 = Availability_Line2.get_value()
                Performance_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.Performance")
                self.Performance_OPC_Line2 = Performance_Line2.get_value()
                Quality_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.LINE.MpOEE.ListUI.Quality")
                self.Quality_OPC_Line2 = Quality_Line2.get_value()
                # Help
                Help_Line2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.EnginHelp")
                self.Help_OPC_Line2 = Help_Line2.get_value()
                # Downtime
                DowntimeLine2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.Down_Time")
                self.Downtime_OPC_Line2 = DowntimeLine2.get_value()
                DowntimeIndexMachineLine2 = client.get_node("ns=6; s=::AsGlobalPV:PDA_Line_2.IndexDownTimeMachine")
                self.IndexDowntimeMachine_OPC_Line2 = DowntimeIndexMachineLine2.get_value()
                time.sleep(1)

            except Exception as error:
                print (error)
                logging.error(error)
                logging.error("Error connect to opc server")
                # repeat after 5 seconds if the OPC server is unavailable
                client.disconnect()
                time.sleep(60)

            except:
                logging.error('Error connecting to OPC server (Check connection)')
                print("Error connecting to OPC server (Check connection)")
                # repeat after 5 seconds if the OPC server is unavailable
                client.disconnect()
                time.sleep(60)

            finally:
                client.disconnect()


    def check_new_value(self):
        while True:
            time.sleep(1)
            # Var
            # Line1
            date = self.Date_OPC
            dateEnd = self.Date_OPCEnd
            # ValueChange Line1
            # ValueChange Line1
            if self.dateprev != date:
                ValueChange = 1
                self.dateprev = date
                print(self.dateprev)
                print(date)
            else:
                ValueChange = 0

                # Update Value Line 1
            if ValueChange:
                OEE = float('{:.2f}'.format(self.OEE_OPC))
                Availability = float('{:.2f}'.format(self.Availability_OPC))
                Performance = float('{:.2f}'.format(self.Performance_OPC))
                Quality = float('{:.2f}'.format(self.Quality_OPC))
                DateStart = date
                DateEnd = dateEnd
                User_line1 = self.user_OPC
                print(float('{:.2f}'.format(OEE)))
                print(Availability)
                print(Performance)
                print(Quality)
                print (User_line1)
                time.sleep(15)
                get_text_messages_line1(OEE, Performance, Quality, Availability, DateStart, DateEnd, ValueChange, User_line1)

            # Help Line1
            if self.Help_OPC_Line1:
                print(self.Help_OPC_Line1)
                #time.sleep(15)
                help_line1(self.Help_OPC_Line1)

            # Downtime Line1
            if self.Downtime_OPC_Line1 and self.IndexDowntimeMachine_OPC_Line1 != 0:
                if time.time() - self.start_time_line1 > 60.0:
                    self.count_line1 += 1
                    print(self.count_line1)
                    self.start_time_line1 = time.time()

                if self.count_line1 == 1 and not self.one_line1:
                    downtime_line1(self.Downtime_OPC_Line1, self.IndexDowntimeMachine_OPC_Line1, self.count_line1)
                    print ("1")
                    self.one_line1 = 1
                elif self.count_line1 == 15 and not self.two_line1:
                    downtime_line1(self.Downtime_OPC_Line1, self.IndexDowntimeMachine_OPC_Line1, self.count_line1)
                    print ("15")
                    self.two_line1 = 1
                elif self.count_line1 == 30 and not self.three_line1:
                    downtime_line1(self.Downtime_OPC_Line1, self.IndexDowntimeMachine_OPC_Line1, self.count_line1)
                    print ("30")
                    self.three_line1 = 1
                elif self.count_line1 == 60 and not self.four_line1:
                    downtime_line1(self.Downtime_OPC_Line1, self.IndexDowntimeMachine_OPC_Line1, self.count_line1)
                    print ("60")
                    self.four_line1 = 1
                elif self.count_line1 > 60 and not self.five_line1:
                    downtime_line1(self.Downtime_OPC_Line1, self.IndexDowntimeMachine_OPC_Line1, self.count_line1)
                    print (">60")
                    self.five_line1 = 1
            else:
                self.count_line1 = 0
                self.one_line1 = 0
                self.two_line1 = 0
                self.three_line1 = 0
                self.four_line1 = 0
                self.five_line1 = 0

            # get json + setebhook
            if not self.get_json_ and self.get_json_two_try < 2:
                self.get_json_two_try += 1
                print (self.get_json_two_try)
                ngrok.connect(5000)
                try:
                    api_result = requests.get('http://127.0.0.1:4040/api/tunnels')
                    api_response = api_result.json()
                    print (api_response)
                    if api_response['tunnels'][0]['proto'] == "https":
                        setebhook_https = "https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/setWebhook?url=" + (
                        api_response['tunnels'][0]['public_url'])
                        print(api_response['tunnels'][0]['proto'])
                        requests.post(setebhook_https, timeout=5, proxies=apihelper.proxy)
                        print (setebhook_https)
                    else:
                        setebhook_http = "https://api.telegram.org/bot1068384211:AAHWnsTAtDL90H7vU6CW_CryuZRaqIqgfPo/setWebhook?url=" + (
                            api_response['tunnels'][1]['public_url'])
                        print(api_response['tunnels'][0]['proto'])
                        requests.post(setebhook_http, timeout=5, proxies=apihelper.proxy)
                        print (setebhook_http)
                    self.get_json_ = 1
                    time.sleep(60)
                    # return api_response['tunnels'][0]['public_url']
                except Exception  as json:
                    ngrok.kill()
                    self.get_json_ = 0
                    logging.error(json)
                    logging.error("Ngrok don't work")
                    print (json)
                    time.sleep(60)
                    pass


    # Check change value OPC line2
    def check_new_value_line_2(self):
        while True:
            time.sleep(1)
            # Line2
            date_Line2 = self.Date_OPC_Line2
            dateEnd_Line2 = self.Date_OPCEnd_Line2
            # ValueChange Line2
            if self.dateprev_Line2 != date_Line2:
                ValueChange_Line2 = 1
                self.dateprev_Line2 = date_Line2
                print(self.dateprev_Line2)
                print(date_Line2)
            else:
                ValueChange_Line2 = 0

            # Update Value Line 2
            if ValueChange_Line2:
                OEE_Line2 = float('{:.2f}'.format(self.OEE_OPC))
                Availability_Line2 = float('{:.2f}'.format(self.Availability_OPC))
                Performance_Line2 = float('{:.2f}'.format(self.Performance_OPC))
                Quality_Line2 = float('{:.2f}'.format(self.Quality_OPC))
                DateStart_Line2 = date_Line2
                DateEnd_Line2 = dateEnd_Line2
                User_line2 = self.user_OPC_Line2
                print(float('{:.2f}'.format(OEE_Line2)))
                print(Availability_Line2)
                print(self.Performance_OPC_Line2)
                print(self.Quality_OPC_Line2)
                print (User_line2)
                time.sleep(15)
                get_text_messages_line2(OEE_Line2, Performance_Line2, Quality_Line2, Availability_Line2, DateStart_Line2,
                                    DateEnd_Line2, ValueChange_Line2, User_line2)

            # Help Line2
            if self.Help_OPC_Line2:
                print(self.Help_OPC_Line2)
                #time.sleep(15)
                help_line2(self.Help_OPC_Line2)

            # Downtime Line2
            if self.Downtime_OPC_Line2 and self.IndexDowntimeMachine_OPC_Line2 != 0:
                if time.time() - self.start_time_line2 > 60.0:
                    self.count_line2 += 1
                    print(self.count_line2)
                    self.start_time_line2 = time.time()

                if self.count_line2 == 1 and not self.one_line2:
                    downtime_line2(self.Downtime_OPC_Line2, self.IndexDowntimeMachine_OPC_Line2, self.count_line2)
                    print ("1")
                    self.one_line2 = 1
                elif self.count_line2 == 15 and not self.two_line2:
                    downtime_line2(self.Downtime_OPC_Line2, self.IndexDowntimeMachine_OPC_Line2, self.count_line2)
                    print ("15")
                    self.two_line2 = 1
                elif self.count_line2 == 30 and not self.three_line2:
                    downtime_line2(self.Downtime_OPC_Line2, self.IndexDowntimeMachine_OPC_Line2, self.count_line2)
                    print ("30")
                    self.three_line2 = 1
                elif self.count_line2 == 60 and not self.four_line2:
                    downtime_line2(self.Downtime_OPC_Line2, self.IndexDowntimeMachine_OPC_Line2, self.count_line2)
                    print ("60")
                    self.four_line2 = 1
                elif self.count_line2 > 60 and not self.five_line2:
                    downtime_line2(self.Downtime_OPC_Line2, self.IndexDowntimeMachine_OPC_Line2, self.count_line2)
                    print (">60")
                    self.five_line2 = 1
            else:
                self.count_line2 = 0
                self.one_line2 = 0
                self.two_line2 = 0
                self.three_line2 = 0
                self.four_line2 = 0
                self.five_line2 = 0

    #Restart Tread
    def th(self):
        while True:
            time.sleep(1)
            try:
                if not self.t1.is_alive():
                    self.t1 = Thread(target=self.opc, args=(), name='opc')
                    self.t1.start()
                    logging.error("New Thread")
                    print ("New Thread")
                    time.sleep(60)

            except Exception as th_opc:
                logging.error(th_opc)
                logging.error("Error_OPC")
                print (th_opc)
                print ("System_opc")
                time.sleep(60)
            except:
                print ("Error_opc")

            try:
                if not self.t2.is_alive():
                    t2 = Thread(target=self.check_new_value, args=(), name='check_value')
                    t2.start()
                    print ("New Thread")
                    time.sleep(60)
            except Exception as th_line1:
                logging.error(th_line1)
                logging.error("Error Check line1")
                print (th_line1)
                print ("System_Line1")
                time.sleep(60)
            except:
                print ("Error_Line1")

            try:
                if not self.t3.is_alive():
                    t3 = Thread(target=self.check_new_value_line_2, args=(), name='check_value_line2')
                    t3.start()
                    print ("New Thread")
                    time.sleep(60)
            except Exception as th_line2:
                logging.error("Error Check line2")
                logging.error(th_line2)
                print (th_line2)
                print ("System_line2")
                time.sleep(60)
            except:
                print ("Error_line2")
new_value()
