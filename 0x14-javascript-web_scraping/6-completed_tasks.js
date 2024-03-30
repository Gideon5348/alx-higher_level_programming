#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch data. Status code:', response.statusCode);
    return;
  }

  const todos = JSON.parse(body);

  // Filter completed tasks
  const completedTodos = todos.filter(todo => todo.completed);

  // Create a map to store the count of completed tasks for each user
  const completedTasksByUser = {};

  // Count completed tasks for each user
  completedTodos.forEach(todo => {
    if (!completedTasksByUser[todo.userId]) {
      completedTasksByUser[todo.userId] = 1;
    } else {
      completedTasksByUser[todo.userId]++;
    }
  });

  console.log(completedTasksByUser);
});
