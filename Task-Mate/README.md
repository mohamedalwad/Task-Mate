# TaskMate
#### Video Demo:  https://youtu.be/rnRDjYLgvgE 
#### Description:
Introduction:
In today’s fast-paced world, effective task management is essential for productivity and organization. The Task Manager web application is designed to help users efficiently create, manage, and track their tasks and to-dos in a user-friendly interface. This application not only streamlines task organization but also promotes better time management and accountability. Built with Flask, SQLAlchemy, and modern front-end technologies, this application offers a robust and interactive experience for users.
User Registration and Authentication:
The Task Manager application features a user registration and authentication system, allowing each user to create their own account securely. Users can register by providing a unique username and a password, which is securely hashed for protection against unauthorized access. Once registered, users can log in to their accounts, where their tasks and data are personalized and stored.
The application ensures that each user’s tasks are kept private and only accessible to them, enhancing the security of their personal information. If a user attempts to log in with incorrect credentials, the application provides immediate feedback through a popup message, informing them that the username or password is incorrect. This feedback mechanism is designed to enhance user experience by ensuring that users are aware of any login issues without needing to refresh the page.
Dashboard Overview:
Upon successful login, users are directed to a dashboard that serves as the central hub for managing tasks. The layout is clean and intuitive, designed to minimize clutter and maximize productivity. The dashboard consists of two main sections: the task addition section and the task management section.
Task Addition Section:
In the left half of the dashboard, users can add new tasks. The task creation form prompts users to enter the following details:
•	Task Name: A brief description of the task.
•	Category: Users can specify the category of the task, such as Work, Personal, Shopping, or Health, which helps in organizing tasks effectively.
•	Due Date: A date picker allows users to set a deadline for the task, ensuring timely completion.
•	Priority Level: Users can select a priority level for each task (Low, Medium, High), which aids in prioritizing their workload.
•	Notes: An optional text area for any additional details or reminders related to the task.
After filling out the form, users can click the “Add Task” button to save their task. Upon successful addition, a confirmation message appears, assuring users that their task has been saved. This section is designed to facilitate quick task entry, ensuring users can easily add their tasks without navigating away from the dashboard.
Task Management Section
In the right half of the dashboard, users can manage their tasks efficiently. This section includes several features that enhance the organization and tracking of tasks:
•	Task List: A dynamically updated list displays all tasks associated with the logged-in user. Each task entry includes the task name, category, priority level, and status (Pending or Complete).
•	Filters and Search: Users can filter tasks by category or status, allowing them to quickly view tasks that meet specific criteria. A search bar is also available to enable users to find tasks by keywords.
•	Sorting Options: Tasks can be sorted by due date, priority, or category, giving users flexibility in how they view their tasks.
•	Completion and Deletion: Each task entry has options to mark the task as complete or delete it. When a task is marked complete, it updates the status, helping users visualize their progress.
Progress Tracking
The application includes a progress tracking feature that helps users stay motivated and accountable. A progress bar visually represents the percentage of tasks completed, allowing users to see how much they have achieved. This feature encourages users to maintain productivity by providing a clear visual representation of their workload.
Responsive Design:
The Task Manager application is built with a responsive design, ensuring it works seamlessly on various devices, including desktops, tablets, and smartphones. The layout adjusts automatically based on the screen size, allowing users to manage their tasks on the go without losing functionality or ease of use.
User Experience:
User experience is a critical aspect of the Task Manager application. The interface is designed to be user-friendly, with intuitive navigation and clear call-to-action buttons. Feedback mechanisms, such as flash messages and alerts, enhance user interaction by providing immediate responses to user actions. The application emphasizes simplicity, making it accessible for users of all technical backgrounds.
