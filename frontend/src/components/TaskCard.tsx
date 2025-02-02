interface TaskCardProps {
  taskName: string;
  storyPoints: number;
}

export default function TaskCard({ taskName, storyPoints }: TaskCardProps) {
  return (
    <div className="w-[400px] bg-gradient-to-r from-teal-700 to-teal-900 text-white rounded-lg shadow-lg mx-auto p-4">
      <div className="flex justify-between items-center">
        {/* Task Name - Bold */}
        <span className="font-bold text-lg">{taskName}</span>

        {/* Deadline */}
        <span className="text-gray-300">{storyPoints} story points</span>
      </div>
    </div>
  );
}
