# SabriShiraz_EventCounter
Sabri Shiraz solution for Event Counter library

Event Counter

Overview
This EventCounter module allows tracking the number of events that occur over a rolling time window. It uses a circular buffer to efficiently store timestamped event counts.

Key capabilities:

Log that an event has occurred
Query number of events within a time range in seconds
Handles high volume events without leak or overflow

Usage

Import EventCounter class: 
from EventCounter import EventCounter

Create instance (sets buffer size): 
event_counter = EventCounter(100)

Log an event: 
event_counter.event("pageview")
Events are logged to Event_log.txt

Get event count over time window (number of seconds, current time): 
count = event_counter.get_num_events(60, datetime.now()) 
print(count)

Implementation
The EventCounter uses a circular buffer to store timestamped counts for each second. As new events come in, it tracks the current and oldest index.

Binary search is used to efficiently find the index for a time interval. Since each bucket has cumulative total event counts, finding the latest timetamp outside the queried window allows fast calculation of the total events from that timestamp umtil the latest event count. This is much faster than summing all the counts in each bucket. 

Testing
Testing covers various test cases as follows:

Automated testing (10 second buffer)

1a. Not rotated, boundary after mid, single bucket
1b. Not rotated, boundary after mid, multiple buckets
2. Not Rotated, boundary = mid, multiple buckets
3a. Not Rotated, boundary before mid, multiple buckets
4a. Rotated, boundary after mid, single bucket
4b. Rotated, boundary after mid, multiple buckets
5a. Rotated, boundary = mid, multiple buckets
5a. Rotated, boundary = mid, single bucket
6a. Rotated, boundary before mid, single bucket
6b. Rotated, boundary before mid, multiple buckets
7. Not rotated, short window
8. Rotated, short window
9. Not Rotated, whole window
10. Rotated, whole window
11a. Partially filled, boundary after mid, single buckets
11b. Partially filled, boundary after mid, multiple buckets
12. Partially filled, boundary = mid, multiple buckets
13. Partially filled, boundary before mid, multiple buckets
14. Partially filled, short window
15. Partially filled, whole window


Run tests using:
python test_event_counter.py

Features
1. Fast find and retrieval using binary search and cumulative event counts.
2. Separate debug log (debug_log.txt) and events log (Event_log.txt)
3. Robust testing with a combination of an automated test suite and manual tests
   with user input queries. Pass / Fail summary printout.


Limitations
1. Only supports single event type
2. Triggering events during get_num_events query could result in unexpected behavior and invalid results
3. No support for multi-threading
4. No log archiving
