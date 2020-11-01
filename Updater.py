import psutil
import requests
import time
import datetime
PROC_NAME = "pythonw.exe"

def make_struct_time(http_header_time):

    '''Input HTML header-type time string and output struct_time'''
    return time.strptime(http_header_time,
            '%a, %d %b %Y %H:%M:%S GMT')

def make_http_time_string(time_struct):

    '''Input struct_time and output HTTP header-type time string'''
    return time.strftime('%a, %d %b %Y %H:%M:%S GMT',
            time_struct)

def make_iso8601_time_string(time_struct):

    '''Input struct_time and output an ISO 8601 time string'''
    return time.strftime('%Y-%m-%dT%H:%M:%S',
            time_struct)

def make_sortable_time_string(time_struct):

    '''Input struct_time and output a "compact sortable" time string'''
    return time.strftime('%Y%m%d_%H%M%S',
            time_struct)


if __name__ == "__main__":

    for proc in psutil.process_iter():
        # check whether the process to kill name matches
        cmdline = "";
        try:
            cmdline = str(proc.cmdline())
        except Exception as ex:
            print("no access to cmdline")

        #print(proc.name() + " " + cmdline)
        if 'Updater.py' in cmdline:
            print(proc.name())

    response = requests.request("GET", "http://192.168.0.58:8080/updater", headers={'If-Modified-Since': 'Sat, 24 Oct 2020 01:07:48 GMT'})
    print(str(response.status_code) + " " + str(response.headers))
