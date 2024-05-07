#include <stdio.h>
#include <time.h>

// Define cleaning schedule data structure
typedef struct {
  int hour;
  int minute;
  int weekday; // 0-6 (Sunday-Saturday)
} CleaningSchedule;

// Function to send cleaning command to Eco Clint (replace with actual communication method)
void sendCleaningCommand() {
  printf("Sending cleaning command to Eco Clint...\n");
}

int main() {
  // Define cleaning schedule
  CleaningSchedule schedule = {10, 0, 2}; // Tuesday at 10:00 AM

  time_t currentTime;
  struct tm *localTime;

  while (1) {
    // Get current time
    currentTime = time(NULL);
    localTime = localtime(&currentTime);

    // Check if current time matches schedule
    if (localTime->tm_wday == schedule.weekday && 
        localTime->tm_hour == schedule.hour && 
        localTime->tm_min == schedule.minute) {
      sendCleaningCommand();
    }

    sleep(60); // Sleep for 1 minute
  }

  return 0;
}
