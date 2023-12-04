''' 
use a circular buffer to track event counts
track total count
track current oldest = counter % 10 + 1
track available - number of readings in 
memory

'''
import datetime
import time

class EventCounter:
    def __init__(self, bufSize):
        now = datetime.datetime.now()
        self.curr = -1                      # Current bucket index
        self.oldest = -1                    # Oldest bucket index
        self.prev = 0                       # prev is used for whole window event total calculation, needed when using cumulative event counts
        self.used = 0                       # track used buckets for partially filled buffer case, for use with binary search
        self.wrap = False                   # used to update oldest and prev when buffer is overwriting oldest with newest entries
        self.buffer = []                    # circular buffer data structure, list/array for fast access with binary search
        self.capacity = bufSize             # buffer capacity
        self.totalEvents = 0                # Cumulative total event count
        for i in range(bufSize):
            self.buffer.append([now, 0])    

    # reset buffer to initial values
    def reset(self):
        now = datetime.datetime.now()
        for i in range(self.capacity):
            self.buffer[i] = [now, 0]

    # Run binary search, include handling for rotated and not rotated cases
    def binary_search(self, target_delta, now):

        left, right = 0, self.used - 1
        left_time = self.buffer[left][0]
        right_time = self.buffer[right][0]
        left_delta = (now - left_time).total_seconds()
        right_delta = (now - right_time).total_seconds()

        is_rotated = bool(left_time > right_time)

        if is_rotated == False:
            # standard binary search, unrotated list
            while left <= right:
                mid = (left + right) // 2
                mid_time = self.buffer[mid][0]
                mid_delta = (now - mid_time).total_seconds()
                with open("debug_log.txt", "a") as f:
                    print(f"Unrotated - left = {left}, mid = {mid}, right = {right}",file=f)
                    print(f"Unrotated - mid_delta = {mid_delta}, target_delta = {target_delta}", file=f)

                if mid_delta <= target_delta:
                    right = mid - 1
                else:  
                    left = mid + 1
            
            return right
        else:
            # Modified binary search to handle rotated list
            while left <= right:
                mid = (left + right) // 2
                mid_time = self.buffer[mid][0]
                mid_delta = (now - mid_time).total_seconds()
                left_delta = (now - left_time).total_seconds()
                right_delta = (now - right_time).total_seconds()
                with open("debug_log.txt", "a") as f:
                    print(f"Rotated - left = {left}, mid = {mid}, right = {right}",file=f)
                    print(f"Rotated - left_delta = {left_delta}, mid_delta = {mid_delta}, \
                          right_delta = {right_delta}, target_delta = {target_delta}", file=f)

                if right_delta > target_delta:
                    if left_delta <= target_delta:
                        return right
                    else:
                        # choose which half to search based on mid_delta
                        if mid_delta > target_delta:
                            if mid_delta > left_delta:
                                right = mid - 1
                            else:
                                left = mid + 1
                        else:
                            right = mid - 1
                else:
                    # choose which half to search based on mid_delta
                    if mid_delta > target_delta:
                        left = mid + 1
                    else:
                        right = mid - 1
            # overshoot, return left
            if right < 0:
                return left
            # if this point is reached, right has the correct index value
            return right
            


                        
    # return number of events by calculating difference in cumulative event counts
    def get_num_events(self, interval, now, caller=""):        
        
        first = self.buffer[self.oldest][0]
        last = self.buffer[self.curr][0]
        delta = (now - last).total_seconds()

        # log debug output
        with open ("debug_log.txt", "a") as f:
            print(f"{caller} oldest is {self.oldest}, current is {self.curr}", file=f)
            print(f"{caller} Last Delta is {delta}", file=f)
            print(f"{caller}Requested timestamp {interval} at time {now}", file=f)
        if delta > interval: # no recent data
            return -1
        
        with open ("debug_log.txt", "a") as f:
            delta = (now - first).total_seconds()
            print(f"{caller} First Delta is {delta}", file=f)

        if delta <= interval: # interval covers all data
            return (self.buffer[self.curr][1] - self.prev)

        # run binary search to find latest bucket just outside interval
        index = self.binary_search(interval, now)
        retval = (self.buffer[self.curr][1] - self.buffer[index][1])
        return retval

    # Signal that an event has occurred
    def event(self, name=""):
        self.totalEvents += 1
        now = datetime.datetime.now()
        with open("Event_log.txt", "a") as f:
            if self.totalEvents == 1:
                print("\n", file=f)
                print("=======================================", file=f)
            print(f"{name} Event {self.totalEvents} signalled at {now}", file=f)
        curr_time = self.buffer[self.curr][0]
        delta = now - curr_time
                        
        if(delta.total_seconds() >= 1):
            # Update oldest if this is very first event or wraparound 
            if self.curr == (self.capacity - 1):
                self.wrap = True

            if self.wrap or self.oldest == -1:
                # save the oldest value self.prev which we will lose
                # use it to get event total for whole buffer
                self.prev = self.buffer[self.oldest][1]
                self.oldest = (self.oldest + 1) % self.capacity
                with open("debug_log.txt", "a") as f:
                    print(f"{name} self.prev changed to {self.prev}, self.oldest changed to {self.oldest}", file=f)
                

            if not self.wrap:
                self.used += 1
            # Since delta is >= 1, use next available time slot
            self.curr = (self.curr + 1) % self.capacity
            self.buffer[self.curr] = [now, self.totalEvents]
        else: # still within 1 second, update current time slot
            self.buffer[self.curr][1] = self.totalEvents

    # print the current buffer
    def print_data(self, test):
        with open ("debug_log.txt", "a") as f:
            print(f"{test} buf size is {self.capacity}", file=f)
            print("========================================", file=f)
            for i in range(self.capacity):
                print("Index = ", i, file=f)
                print("Timestamp - ", self.buffer[i][0], file=f)
                print("Events - ", self.buffer[i][1], file=f)

