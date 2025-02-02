import SignOut from "@/components/SignOut";
import TaskCard from "@/components/TaskCard";

export default function Dashboard() {
  
  return (
    <div>
      <SignOut />
      <div className="flex flex-col items-center justify-center min-h-screen">
        {/* Map through tasks and render TaskCard for each */}
        <TaskCard />

        {/* Upload button at the end of the task list */}
        <button className="bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-semibold px-6 py-3 rounded-lg shadow-lg hover:from-blue-600 hover:to-indigo-700 hover:scale-105 transform transition duration-300 ease-in-out absolute bottom-0 right-0 mb-6 mr-6">
          📤 Upload
        </button>
      </div>
    </div>
  );
}
