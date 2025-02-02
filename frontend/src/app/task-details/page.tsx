"use client";

import { useEffect, useState } from "react";
import axios from "axios";
import { useUser } from "@/context/UserContext"; // Import the useUser hook
import PrivateRoute from "@/components/PrivateRoute";
import SignOut from "@/components/SignOut";
import TaskCard from "@/components/TaskCard";

interface Task {
    task_id: number;
    task_desc: string;
    story_points: number;
  }

const TaskDetailsPage = () => {
  const { user } = useUser(); // Get the user data from UserContext
  const [tasks, setTasks] = useState<Task[]>([]);
  const [fetchingError, setFetchingError] = useState<string | null>(null);

  useEffect(() => {
    if (user && user.id && user.role == "manager") {
      // Fetch tasks for the user based on user.id
      axios
        .get(`http://localhost:4050/user/get-task?userId=1`) // Pass user.id in the request
        .then((response) => {
          setTasks(response.data); // Assuming response data contains the tasks
        //   console.log(response.data);
        })
        .catch((err) => {
          setFetchingError("Failed to fetch tasks");
        });
    }else if (user && user.id && user.role == "member") {
      // Fetch tasks for the user based on user.id
      axios
        .get(`http://localhost:4050/user/get-task?userId=${user.id}`) // Pass user.id in the request
        .then((response) => {
          setTasks(response.data); // Assuming response data contains the tasks
        //   console.log(response.data);
        })
        .catch((err) => {
          setFetchingError("Failed to fetch tasks");
        });
    } else {
      setFetchingError("User not found in context");
    }
  }, [user]);

  // Loading and error handling
  if (!user) {
    return <p>User not logged in</p>;
  }

  if (fetchingError) {
    return <p>{fetchingError}</p>;
  }

  return (
    <PrivateRoute>
      <div>
      <SignOut />
      <div className="flex flex-col items-center justify-center min-h-screen">
      <h1 className="text-3xl font-semibold text-teal-800 mb-6 text-center">
  Your Tasks
</h1>


  {tasks.length > 0 ? (
    <div className="flex flex-col items-center justify-center gap-4">
      {tasks.map((task) => (
        <TaskCard
          key={task.task_id}
          taskName={task.task_desc}
          storyPoints={task.story_points}
        />
      ))}
    </div>
  ) : (
    <p className="text-center text-lg text-gray-600">No tasks available</p>
  )}
</div>
    </div>
    </PrivateRoute>
  );
};

export default TaskDetailsPage;
