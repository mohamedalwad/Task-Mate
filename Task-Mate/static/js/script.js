const taskForm = document.getElementById('new-task-form');
const taskList = document.getElementById('task-list');
const categoryFilter = document.getElementById('category-filter');
const statusFilter = document.getElementById('status-filter');
const taskSearch = document.getElementById('task-search');
const sortBy = document.getElementById('sort-by');
const progressText = document.getElementById('progress-text');
const taskProgress = document.getElementById('task-progress');

let tasks = [];

function updateProgress() {
    const totalTasks = tasks.length;
    const completedTasks = tasks.filter(task => task.completed).length;
    taskProgress.value = totalTasks > 0 ? (completedTasks / totalTasks) * 100 : 0;
    progressText.textContent = `${completedTasks} of ${totalTasks} tasks completed`;
}

function addTask(task) {
    tasks.push(task);
    renderTasks();
    updateProgress();
    updateCategoryOptions();
}

function renderTasks() {
    taskList.innerHTML = '';
    const filteredTasks = filterTasks(tasks);

    filteredTasks.forEach(task => {
        const li = document.createElement('li');
        li.className = `priority-${task.priority}`;
        li.innerHTML = `
            <input type="checkbox" class="complete-checkbox" ${task.completed ? 'checked' : ''} onchange="toggleTaskCompletion(${tasks.indexOf(task)})">
            <div>
                <div class="task-name">${task.name}</div>
                <div class="task-category">${task.category}</div>
                <div class="task-date">${task.date}</div>
                <div class="task-priority">Priority: ${task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}</div>
                <div class="task-notes">${task.notes}</div>
            </div>
            <button class="delete-btn" onclick="deleteTask(${tasks.indexOf(task)})">Delete</button>
        `;
        taskList.appendChild(li);
    });

    updateProgress();
}

function toggleTaskCompletion(index) {
    tasks[index].completed = !tasks[index].completed;
    renderTasks();
}

function deleteTask(index) {
    tasks.splice(index, 1);
    renderTasks();
    updateCategoryOptions();
}

function filterTasks(tasks) {
    let filteredTasks = tasks;

    const status = statusFilter.value;
    if (status === 'complete') {
        filteredTasks = filteredTasks.filter(task => task.completed);
    } else if (status === 'incomplete') {
        filteredTasks = filteredTasks.filter(task => !task.completed);
    }

    const searchTerm = taskSearch.value.toLowerCase();
    if (searchTerm) {
        filteredTasks = filteredTasks.filter(task => task.name.toLowerCase().includes(searchTerm));
    }

    const category = categoryFilter.value;
    if (category !== 'all') {
        filteredTasks = filteredTasks.filter(task => task.category === category);
    }

    return filteredTasks;
}

function updateCategoryOptions() {
    const categories = [...new Set(tasks.map(task => task.category))];
    categoryFilter.innerHTML = '<option value="all">All Categories</option>';
    categories.forEach(category => {
        categoryFilter.innerHTML += `<option value="${category}">${category}</option>`;
    });
}

taskForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const newTask = {
        name: document.getElementById('task-name').value,
        category: document.getElementById('task-category').value,
        date: document.getElementById('task-date').value,
        priority: document.getElementById('task-priority').value,
        notes: document.getElementById('task-notes').value,
        completed: false,
    };

    addTask(newTask);
    taskForm.reset();
});

categoryFilter.addEventListener('change', renderTasks);
statusFilter.addEventListener('change', renderTasks);
taskSearch.addEventListener('input', renderTasks);

sortBy.addEventListener('change', () => {
    const sortValue = sortBy.value;
    if (sortValue === 'date') {
        tasks.sort((a, b) => new Date(a.date) - new Date(b.date));
    } else if (sortValue === 'priority') {
        const priorityOrder = { 'high': 3, 'medium': 2, 'low': 1 };
        tasks.sort((a, b) => priorityOrder[b.priority] - priorityOrder[a.priority]); 
    } else if (sortValue === 'category') {
        tasks.sort((a, b) => a.category.localeCompare(b.category));
    }
    renderTasks();
});