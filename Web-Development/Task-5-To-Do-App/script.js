const taskInput = document.getElementById("taskInput");
const taskList = document.getElementById("taskList");
const taskCount = document.getElementById("taskCount");

function addTask() {

    const taskText = taskInput.value.trim();

    if (taskText === "") {
        alert("Please enter a task.");
        return;
    }

    const li = document.createElement("li");
    li.className = "task";

    const taskSpan = document.createElement("span");
    taskSpan.textContent = taskText;

    const completeButton = document.createElement("button");
    completeButton.textContent = "✓";
    completeButton.className = "complete-btn";

    completeButton.onclick = function () {
        li.classList.toggle("completed");
        updateTaskCount();
    };

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.className = "delete-btn";

    deleteButton.onclick = function () {
        li.remove();
        updateTaskCount();
    };

    li.appendChild(taskSpan);
    li.appendChild(completeButton);
    li.appendChild(deleteButton);

    taskList.appendChild(li);

    taskInput.value = "";

    updateTaskCount();
}

function clearCompleted() {

    const completedTasks = document.querySelectorAll(".completed");

    completedTasks.forEach(function (task) {
        task.remove();
    });

    updateTaskCount();
}

function updateTaskCount() {

    const totalTasks = taskList.children.length;

    if (totalTasks === 1) {
        taskCount.textContent = "1 task";
    } else {
        taskCount.textContent = totalTasks + " tasks";
    }
}

taskInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        addTask();
    }
});