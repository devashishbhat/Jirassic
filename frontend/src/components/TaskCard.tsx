export default function TaskCard() {
  return (
    <div className="w-[400px] bg-gradient-to-r from-teal-700 to-teal-900 text-white rounded-lg shadow-lg mx-auto p-4">
      <div className="flex justify-between items-center">
        {/* Task Name - Bold */}
        <span className="font-bold text-lg">Task Name</span>

        {/* Deadline */}
        <span className="text-gray-300">Deadline Date</span>

        {/* Down Arrow Icon */}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="size-6"
        >
          <path
            fillRule="evenodd"
            d="M12.53 16.28a.75.75 0 0 1-1.06 0l-7.5-7.5a.75.75 0 0 1 1.06-1.06L12 14.69l6.97-6.97a.75.75 0 1 1 1.06 1.06l-7.5 7.5Z"
            clipRule="evenodd"
          />
        </svg>
      </div>
    </div>
  );
}
