#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const todos = JSON.parse(body);
  const completedTasks = {};

  for (const todo of todos) {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasks[userId]) {
        completedTasks[userId]++;
      } else {
        completedTasks[userId] = 1;
      }
    }
  }

  console.log(completedTasks);
});
