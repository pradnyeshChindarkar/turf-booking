from django.test import TestCase
from btbookturf.models import Ground,Booking,Slot
# Create your tests here.
class MyModelTestCase(TestCase):
    def available_slots(self):
        allSlots=Slot()
        for slots in allSlots:
            print(allSlots.start_time)