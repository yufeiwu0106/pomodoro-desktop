# Pomodoro Timer Project

## Introduction

Welcome to the Pomodoro Timer project! This project is a simple implementation of a Pomodoro timer using Python and Pygame.

## Features

- **Pomodoro Timer:** Set a timer for 25 minutes of focused work.
- **Short Break Timer:** Take a short break of 5 minutes.
- **Long Break Timer:** Enjoy a longer break of 15 minutes.
- **User Input:** Enter your user ID to track work times.
- **Database Integration:** Store and retrieve user work times in a SQLite database.
- **Audio Notifications:** Receive notifications for timer completion.

## Getting Started

### Prerequisites

- Python (3.7 or higher)
- Pygame library

## Limitations

- Timer State Preservation: The current program does not save the state of the timer (e.g., whether it is in work or rest mode) when the program is closed or restarted. Consider adding state saving and restoration functionality.
- More Unit Customization Options: Provide users with more customization options, such as adjusting the length of work and break periods, customizing notification sounds, etc.
- User Switching Within Program Execution: Lacks the functionality to facilitate user switching without restarting the program 
- Richer Statistics and Reports: While basic work time statistics are implemented, there is room for expansion to generate detailed work time reports, providing users with more information and insights.
