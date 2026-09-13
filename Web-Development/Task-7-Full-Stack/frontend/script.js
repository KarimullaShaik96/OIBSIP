const API_URL = "http://127.0.0.1:5000/api/tasks";

const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const message = document.getElementById("message");


// Load all tasks
async function loadTasks() {
    try {
        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const tasks = await response.json();

        taskList.innerHTML = "";

        tasks.forEach(task => {
            displayTask(task);
        });

    } catch (error) {
        message.textContent = "Unable to connect to the backend.";
        console.error("Load error:", error);
    }
}


// Add a new task
async function addTask() {

    const title = taskInput.value.trim();

    if (!title) {
        message.textContent = "Please enter a task.";
        return;
    }

    try {

        const response = await fetch(API_URL, {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title: title
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Failed to add task");
        }

        taskInput.value = "";
        message.textContent = "";

        await loadTasks();

    } catch (error) {

        message.textContent = "Unable to add task.";
        console.error("Add task error:", error);

    }
}


// Display task
function displayTask(task) {

    const li = document.createElement("li");

    li.className = "task-item";

    li.innerHTML = `
        <input
            type="checkbox"
            ${task.completed ? "checked" : ""}
            onchange="toggleTask(${task.id}, this.checked)"
        >

        <span class="task-title ${task.completed ? "completed" : ""}">
            ${task.title}
        </span>

        <button
            class="delete-btn"
            onclick="deleteTask(${task.id})"
        >
            Delete
        </button>
    `;

    taskList.appendChild(li);
}


// Complete / uncomplete task
async function toggleTask(id, completed) {

    try {

        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                completed: completed
            })
        });

        if (!response.ok) {
            throw new Error("Failed to update task");
        }

        await loadTasks();

    } catch (error) {

        console.error("Update error:", error);

    }
}


// Delete task
async function deleteTask(id) {

    try {

        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        if (!response.ok) {
            throw new Error("Failed to delete task");
        }

        await loadTasks();

    } catch (error) {

        console.error("Delete error:", error);

    }
}


// Enter key support
taskInput.addEventListener("keypress", function(event) {

    if (event.key === "Enter") {
        addTask();
    }

});


// Load tasks when page opens
loadTasks();