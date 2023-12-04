from EventCounter import EventCounter
import datetime
import time
import math

small_window = 10
med_window = 150
large_window = 300

def test1(EC):        # fill 10 item buffer, non rotated
    time.sleep(1)

    events = [5, 9, 17, 23, 30, 4, 5, 7, 6, 7]
    waits  = [1, 3, 5,  4,  3,  1, 1, 3, 6, 3]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 1: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 1 data:", file=f)
    EC.print_data("Test 1: ")

def test2(EC):         # partially filled 10 item buffer, even number of items
    time.sleep(1)

    events = [5, 9, 17, 23, 30, 4, 5, 7]
    waits =  [1, 3, 5,  4,  3,  6, 2, 4]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 2: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 2 data:", file=f)
    EC.print_data("Test 2: ")

def test3(EC):        # rotated 10 item buffer, pivot before midpoint
    time.sleep(1)

    events = [5, 9, 17, 23, 30, 4, 5, 7, 6, 7, 2, 3]
    waits  = [1, 3, 5,  4,  3,  1, 1, 3, 6, 3, 1, 5]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 3: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 3 data:", file=f)
    EC.print_data("Test 3: ")

def test4(EC):        # rotated 10 item buffer, pivot = midpoint
    time.sleep(1)

    events = [3, 5, 1, 4, 8, 6, 7, 9, 1, 3, 6, 4, 7, 1, 5]
    waits  = [1, 2, 5, 4, 2, 3, 8, 1, 3, 6, 2, 4, 1, 4, 5]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 4: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 4 data:", file=f)
    EC.print_data("Test 4: ")

def test5(EC):        # rotated 10 item buffer, pivot after midpoint
    time.sleep(1)

    events = [1, 6, 3, 4, 9, 6, 2, 8, 12, 15, 3, 7, 4, 2, 1, 5, 1]
    waits  = [2, 3, 1, 6, 4, 2, 8, 3, 4,  5,  1, 4, 3, 7, 2, 5, 1]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 5: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 5 data:", file=f)
    EC.print_data("Test 5: ")

def test7(EC):         # partially filled 10 item buffer, odd
    time.sleep(1)

    events = [5, 9, 17, 23, 30, 4, 5]
    waits =  [1, 3, 5,  4,  3,  6, 2]

    for i in range(len(events)):
        for j in range(events[i]):
            EC.event("Test 7: ")
        time.sleep(waits[i])

    with open("debug_log.txt", "a") as f:
        print("Test 7 data:", file=f)
    EC.print_data("Test 7: ")

def test8(EC):        # fill 300 item buffer, non rotated
    time.sleep(1)
    for i in range(300):
        EC.event("Test 8: ")
        time.sleep(1)

    EC.print_data("Test 8: ")


def test9(EC):        # half filled 300 item buffer, non rotated
    time.sleep(1)
    for i in range(150):
        EC.event("Test 9: ")
        time.sleep(1)
    
    EC.print_data("Test 9: ")


def run_10sec_buffer_tests_partially_filled_odd():
    passed, failed = 0, 0
    EvC = EventCounter(small_window)
    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 7 : Partially filled, odd", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)
    test7(EvC)

    EvC.print_data()


    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print("Partially filled, odd - Total events is ", EvC.totalEvents, file=f)


    interval = str(2.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #1: Partially filled, single time slot after midpoint...", end="")
    if(retval == 5):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(8.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #2: Partially filled, multiple time slots after midpoint...", end="")
    if(retval == 9):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(15.2)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #3: Partially filled, multiple time slots starting at midpoint...", end="")
    if(retval == 62):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(20.2)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #4: Partially filled, multiple time slots before midpoint...", end="")
    if(retval == 79):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(1.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #5: Partially filled, short time window, no data...", end="")
    if(retval == -1):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(24.31)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #6: Partially filled, long time window, all data...", end="")
    if(retval == 93):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    return [passed, failed]

def run_10sec_buffer_tests_partially_filled_even():
    passed, failed = 0, 0
    EvC = EventCounter(small_window)
    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 2 : Partially filled, even   ", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)

    test2(EvC)

    EvC.print_data("run_10sec_buffer_tests_partially_filled_even: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print("Partially filled, even - Total events is ", EvC.totalEvents, file=f)


    interval = str(4.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #1: Partially filled, single time slot after midpoint...", end="")
    if(retval == 7):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(6.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #2: Partially filled, multiple time slots after midpoint...", end="")
    if(retval == 12):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(19.2)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #3: Partially filled, multiple time slots starting at midpoint...", end="")
    if(retval == 69):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(24.2)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #4: Partially filled, multiple time slots before midpoint...", end="")
    if(retval == 86):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(1.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #5: Partially filled, short time window, no data...", end="")
    if(retval == -1):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(30.31)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_partially_filled_odd: ")

    print("\nRunning 10 second buffer test #6: Partially filled, long time window, all data...", end="")
    if(retval == 100):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    return [passed, failed]

def run_10sec_buffer_tests_rotated():
    passed, failed = 0, 0    
    EvC = EventCounter(small_window)
    
    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 3 : Rotated  ", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)
    test3(EvC)
    EvC.print_data("run_10sec_buffer_tests_rotated: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Rotated - Total events is ", EvC.totalEvents, file=f)
    interval = str(5.23)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #1: Rotated, single time slot before midpoint...", end="")
    if(retval == 3):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(6.21)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #2: Rotated, multiple time slots before midpoint...", end="")
    if(retval == 5):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    EvC.reset()

    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 4 : Rotated  ", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)
    test4(EvC)
    EvC.print_data("run_10sec_buffer_tests_rotated: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print("Rotated - Total events is ", EvC.totalEvents, file=f)

    interval = str(5.23)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #3: Rotated, single time slot at midpoint...", end="")
    if(retval == 5):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(9.23)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #4: Rotated, multiple time slots starting at midpoint...", end="")
    if(retval == 6):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    EvC.reset()

    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 5 : Rotated  ", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)
    test5(EvC)
    EvC.print_data("run_10sec_buffer_tests_rotated: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print("Rotated - Total events is ", EvC.totalEvents, file=f)

    interval = str(1.22)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #5: Rotated, single time slot after midpoint...", end="")
    if(retval == 1):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(6.21)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #6: Rotated, multiple time slots after midpoint...", end="")
    if(retval == 6):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(0.5)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #7: Rotated, short time window, no data...", end="")
    if(retval == -1):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    with open ("debug_log.txt", "a") as f:
        print("\n----------TEST 8------------\n",file=f)


    interval = str(36)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_rotated: ")

    print("\nRunning 10 second buffer test #8: Rotated, window covers all data...", end="")
    if(retval == 58): 
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    return [passed, failed]


def run_10sec_buffer_tests_unrotated():
    passed, failed = 0, 0
    EvC = EventCounter(small_window)
    print("\nPlease wait while events are generated...")
    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print(" Test 1 : Unrotated  ", EvC.totalEvents, file=f)
        print("--------------------------------------", file=f)

    test1(EvC)
    EvC.print_data("run_10sec_buffer_tests_unrotated: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        print("Unrotated - Total events is ", EvC.totalEvents, file=f)
    interval = str(3.1)
    curr_time = datetime.datetime.now()
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #1: Not rotated, single time slot after midpoint...", end="")
    if(retval == 7):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1

    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(9.1)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #2: Not rotated, multiple time slots after midpoint...", end="")
    if(retval == 13):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1


    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(17.2)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #3: Not rotated, multiple time slots starting at midpoint...", end="")
    if(retval == 59):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1


    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(21.2)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #4: Not rotated, multiple time slots starting before midpoint...", end="")
    if(retval == 82):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1


    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")


    interval = str(1)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #5: Not rotated, no data due to short time window...", end="")
    if(retval == -1):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1


    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    interval = str(31)
    retval = EvC.get_num_events(float(interval), curr_time, "run_10sec_buffer_tests_unrotated: ")

    print("\nRunning 10 second buffer test #6: Not rotated, window covers entire data set...", end="")
    if(retval == 113):
        print("PASSED")
        passed += 1
    else:
        print("FAILED")
        failed += 1


    if retval == -1:
        print(f"0 events occurred in the last {interval} seconds")
    else:
        print(f"{retval} events occurred in the last {interval} seconds")

    return [passed, failed]

# run 300 second buffer tests, filled and half filled based on parameter
def run_300sec_buffer_tests(fill_pct):
    passed, failed = 0, 0
    EvC = EventCounter(large_window)
    print("Please wait while events are generated...")
    # use test data as needed based on fill_pct
    if fill_pct == 100:
        test8(EvC)
    else:
        test9(EvC)
    curr_time = datetime.datetime.now()

    EvC.print_data("run_300sec_buffer_tests: ")

    with open ("debug_log.txt", "a") as f:
        print("--------------------------------------", file=f)
        if fill_pct == 100:
            print("Unrotated, 300 items, filled - Total events is ", EvC.totalEvents, file=f)
        else:
            print("Unrotated, 300 items, half filled - Total events is ", EvC.totalEvents, file=f)


    print("Total events is ", EvC.totalEvents)
    print(f"Last data collection time {EvC.buffer[EvC.curr][0]}")

    while(True):
        if fill_pct == 100:
            print(f"Event count data available for {large_window} seconds")
        else:
            print(f"Event count data available for {med_window} seconds")

        interval = input("Enter an interval (Enter 0 to quit): ")
        # exit if blank input or 0
        if len(interval) == 0 or int(interval) == 0:
            break
        retval = EvC.get_num_events(float(interval), EvC.buffer[EvC.curr][0], "run_10sec_buffer_tests_unrotated: ")
        if fill_pct == 100:
            print("Running 300 second buffer test #1: Filled...", end="")
        else:
            print("Running 300 second buffer test #2: Half filled...", end="")

        if retval == math.floor(float(interval)):
            print("PASSED")
            passed += 1
        elif fill_pct == 100 and float(interval) > 300 and retval == 300:
            print("PASSED")
            passed += 1
        elif fill_pct == 50 and float(interval) > 150 and retval == 150:
            print("PASSED")
            passed += 1
        else:
            print("FAILED")
            failed += 1

        if retval == -1:
            print(f"0 events occurred in the last {float(interval)} seconds\n")
        else:
            print(f"{retval} events occurred in the last {float(interval)} seconds\n")

    return [passed, failed]

def main():
    total_pass, total_fail= 0, 0
    result = []
    test_option = 0


    while(True):
        print("Test options : ")
        print("1. Automated tests. Testing a variety of scenarios (see README for details). buffer size = 10 seconds")
        print("2. Manual test. User input queries. buffer size = 300 seconds, filled 100% with 1 event per second")
        print("3. Manual test. User input queries. buffer size = 300 seconds, filled 50% with 1 event per second")

        test_option = input("Enter a testing choice (1-3), 0 or none to quit : ")
        if len(test_option) == 0 or test_option == '0':
            break

        if test_option == "1":
            result = run_10sec_buffer_tests_unrotated()
            total_pass += result[0]
            total_fail += result[1]
            result = run_10sec_buffer_tests_rotated()
            total_pass += result[0]
            total_fail += result[1]
            result = run_10sec_buffer_tests_partially_filled_even()
            total_pass += result[0]
            total_fail += result[1]
            result = run_10sec_buffer_tests_partially_filled_odd()
            total_pass += result[0]
            total_fail += result[1]
        
        elif test_option == "2":
            result = run_300sec_buffer_tests(100)
            total_pass += result[0]
            total_fail += result[1]

        elif test_option == "3":
            result = run_300sec_buffer_tests(50)
            total_pass += result[0]
            total_fail += result[1]

        else:
            break


    print(f"\nTotal passed {total_pass}\nTotal failed {total_fail}") 

if __name__ == "__main__":
    main()

