<h1 align = center> System Action Scheduler</h1>

<div style="height: 300px; width: 900px; margin: 0 auto; text-align: center;">
  <img src="https://github.com/user-attachments/assets/e3309d4a-f7b8-49a6-8f4e-e1022935b0e1" alt="System Action Scheduler" >

</div>

 ## Working of System Action Scheduler 
<p align="center">
<img src="https://github.com/user-attachments/assets/79a77a29-5c2e-4f00-b6ae-b04b79663363"></img>
</p>


## 📝Overview
System Action Scheduler is a simple yet powerful desktop application that allows users to schedule system actions such as shutdown, restart, sleep, or open a URL after a specified delay. The application is designed for Windows users and comes as a standalone executable file, making it easy to run without any installation or Python setup.

## ✨Features
- Schedule system actions: shutdown, restart, sleep, or open a URL.
- Set a timer for each action with a delay in seconds, minutes, or hours.
- User-friendly graphical interface with a clean, intuitive design.
- No installation required – just download and run the executable. <a href = "https://github.com/usmanbvp/system-action-scheduler/blob/main/dist/scheduler.exe">Link </a>

## 📋Requirements

- Windows Operating System.
- No installation required – just the executable file.

## 🛠️Installation

### Download the Executable File:
- Download the Scheduler.exe file from the provided link.
-  👉 [Download Scheduler.exe](https://github.com/usmanbvp/system-action-scheduler/blob/main/dist/scheduler.exe)

### Run the Application:
- Simply double-click the Scheduler.exe file to launch the app. There's no need for installation or setting up dependencies.

## How to Use the App?

#### 1.Choose an Action:
    Select one of the following actions:
        Shutdown: Shuts down the system.
        Restart: Restarts the system.
        Sleep: Puts the system to sleep.
        Open URL: Opens a URL in the web browser.

#### 2.Enter Time Delay:
    For the selected action, input the delay time in the text field. You can choose the delay in seconds, minutes, or hours.

#### 3.Select Time Unit:
    Use the dropdown menu to select the unit for the time (seconds, minutes, or hours).

#### 4.Start the Timer:
    Click on the "Start Timer" button to initiate the countdown for the selected action. A confirmation dialog will appear asking you to confirm the scheduled action.

#### 5.Action Execution:
    Once the time is up, the selected action will be performed automatically (e.g., shutdown, restart, sleep, or open the URL).


## 🎨UI Plan
#### Layout Overview

The app's graphical user interface (GUI) is structured to provide a clean, user-friendly experience where each action has its own section for input and controls. The layout is designed to be intuitive, allowing users to easily select and configure system actions.
##### UI Components
- Heading: At the top of the window, the title "System Action Scheduler" is displayed in bold and large font, providing a clear indication of the app's purpose.

- Action Sections: Each action (Shutdown, Restart, Sleep, Open URL) is represented by a section containing:

    Icon: A small icon visually representing the selected action (e.g., a restart icon for restarting, a power icon for shutting down, etc.). The icon updates dynamically when the user selects a new action from the dropdown menu. <br>
    Time Input: A text field where users can enter the delay time for the selected action. This allows users to specify how long they want to wait before the action is executed.<br>
    Time Unit Selector: A dropdown menu that allows users to choose the time unit for the delay, such as seconds, minutes, or hours.<br>
    URL Input: For the "Open URL" action, an additional input field is shown, allowing users to specify the URL they want to open in their default web browser.<br>
- Start Timer Button: A large button labeled "Start Timer" that, when clicked, initiates the countdown for the selected action. This button triggers the scheduling of the chosen action, using the time and unit specified by the user.<br>

##### UI Layout
The layout of the app consists of a single main window, containing the action selection dropdown, the icon for the action, the time input and unit selection, and the "Start Timer" button. The components are arranged logically to make it easy for the user to follow:<br>
1.Header at the top displays the app title.<br>
2.Action selection section allows the user to choose between Restart, Shutdown, Sleep, or Open URL from a dropdown.<br>
3.Icon display shows a corresponding icon for the selected action.<br>
4.Time input fields (text field and dropdown) for entering the delay.<br>
5.Start Timer button at the bottom to trigger the scheduled action.<br>

<div style="height: 1200px; width: 900px; margin: 0 auto; text-align: center;">
  <img src="https://github.com/user-attachments/assets/6bc207ea-3e03-4e2b-a130-6c8157a039c6" alt="System Action Scheduler UI Layout" >
  
</div>


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

The MIT License is a permissive open source license that allows you to use, modify, and distribute this project for both commercial and non-commercial purposes.

## 📝Feedback and Support
If you have any feedback, suggestions, or questions regarding the project, please create an issue in the repository or contact me at usman.bvp@gmail.com.

### If you find this repository helpful, don't forget to show your support by giving it a star! ⭐
Your star is a great way to let us know you appreciate our work and find value in this project. Thank you! ⭐