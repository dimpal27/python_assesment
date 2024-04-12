
Calendar Program Debugging
Issue Description:
The provided calendar program is not functioning as expected. It should allow users to add events to the calendar without causing double bookings. Double bookings occur when two events overlap in time.

Steps to Reproduce:
Create a new instance of the Calendar class.
Attempt to add events using the book method.

Expected Behavior:
The book method should return True if the event can be added without causing a double booking.
The book method should return False if the event would cause a double booking.

Actual Behavior:
The book method does not correctly detect double bookings and sometimes returns incorrect results.

Debugging Steps:
Review the Node class implementation, which handles event insertion.
Identify any logic errors in the insert method of the Node class.
Check if events are being correctly inserted into the binary tree structure.
Verify that overlapping events are detected and handled properly.
Test the book method with various input scenarios to ensure correct behavior.
Resolution:
To resolve the issue, the insert method in the Node class should be modified to correctly handle event insertion and detection of overlapping events.

Updated Implementation:
Adjust the logic in the insert method to properly detect overlapping events and insert events into the binary tree structure.
Ensure that the book method in the Calendar class correctly calls the insert method and returns the expected results.

Testing:
After updating the implementation, test the Calendar class with different input scenarios to verify that double bookings are detected and prevented.