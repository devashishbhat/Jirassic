import SignOut from "@/components/SignOut";
import TaskCard from "@/components/TaskCard";

export default function Dashboard() {
  return (
    <div>
      <SignOut />
      <div className="flex items-center justify-center min-h-screen">
        <TaskCard />
      </div>
    </div>
  );
}
