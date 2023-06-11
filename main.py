from rabbit_handler.rabbit_sender import produce


def set_alarm_settings_single():
    body = {
        "action": "single",
        "channelid": 1,
        "settings": {
            "alarmsethigh": 1,
            "alarmtemphigh": 50.0,
            "alarmsetlow": 1,
            "alarmtemplow": -20.0
        }
    }
    produce("core-alarm", body)


def set_alarm_settings_multiple():
    body = {
        "action": "multiple",
        "settings": {
            "2": {"alarmsethigh": 1,
                  "alarmtemphigh": 20.0,
                  "alarmsetlow": 1,
                  "alarmtemplow": -20.0
                  },
            "3": {"alarmsethigh": 1,
                  "alarmtemphigh": 30.0,
                  "alarmsetlow": 1,
                  "alarmtemplow": -30.0

                  },
            "24": {"alarmsethigh": 1,
                   "alarmtemphigh": 240.0,
                   "alarmsetlow": 1,
                   "alarmtemplow": -240.0

                   }
        }
    }
    produce("core-alarm", body)


def set_dwellsettings_single():
    body = {
        "action": "single",
        "channelid": 1,
        "settings": {
            "upperdwelltemp": 10.0,
            "upperdwelllimithigh": 13.0,
            "upperdwelllimitlow": 7.0,
            "lowerdwelltemp": -10.0,
            "lowerdwelllimithigh": -7.0,
            "lowerdwelllimitlow": -13.0,
        }
    }
    produce("core-dwell", body)


def set_dwell_settings_multiple():
    body = {
        "action": "multiple",
        "settings": {
            "2": {"upperdwelltemp": 10.0,
                  "upperdwelllimithigh": 13.0,
                  "upperdwelllimitlow": 7.0,
                  "lowerdwelltemp": -10.0,
                  "lowerdwelllimithigh": -7.0,
                  "lowerdwelllimitlow": -13.0,
                  },
            "3": {"upperdwelltemp": 10.0,
                  "upperdwelllimithigh": 13.0,
                  "upperdwelllimitlow": 7.0,
                  "lowerdwelltemp": -10.0,
                  "lowerdwelllimithigh": -7.0,
                  "lowerdwelllimitlow": -13.0,

                  },
            "24": {"upperdwelltemp": 10.0,
                   "upperdwelllimithigh": 13.0,
                   "upperdwelllimitlow": 7.0,
                   "lowerdwelltemp": -10.0,
                   "lowerdwelllimithigh": -7.0,
                   "lowerdwelllimitlow": -13.0,

                   }
        }
    }
    produce("core-dwell", body)


def change_name():
    body = {
        "action": "single",
        "channelid": 24,
        "channelname": "MMX_TEST"
    }
    produce("core-channelname", body)


def change_names():
    body = {
        "action": "multiple",
        "names": {
            "1": "NEW_1",
            "2": "NEW_2",
            "3": "NEW_3",
            "4": "NEW_4",
            "5": "NEW_5",
            "6": "NEW_6",
            "7": "NEW_7",
            "8": "NEW_8",
            "9": "NEW_9",
            "10": "NEW_10",
            "11": "NEW_11",
            "12": "NEW_12",
            "13": "NEW_13",
            "14": "NEW_14",
            "15": "NEW_15",
            "16": "NEW_16",
            "17": "NEW_17",
            "18": "NEW_18",
            "19": "NEW_19",
        }
    }
    produce("core-channelname", body)


def start_idle():
    body = {
        "action": "idle"
    }
    produce("core-test-control", body)


def start_test():
    body = {
        "action": "start",
        "usedctr": 1023,
        "usedpsu": 32636927,
        "testname": "Test_19_22"
    }
    produce("core-test-control", body)


def stop_test():
    body = {
        "action": "stop"
    }
    produce("core-test-control", body)


def restart_controller():
    body = {"action": "multiple",
            "channelid": 20,
            "channels":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]}
    produce("activity-restart", body)


def change_psu_val():
    body = {
        "type": "psu",
        "channelid": 25,
        "property": "voltage",
        "value": 8.0
    }
    produce("core-set-device-prop", body)


if __name__ == '__main__':
    start_test()
