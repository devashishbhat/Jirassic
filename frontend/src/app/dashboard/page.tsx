"use client";

import SignOut from "@/components/SignOut";
import Link from "next/link";
import { useUser } from "@/context/UserContext";
import PrivateRoute from "@/components/PrivateRoute";

export default function Dashboard() {
  const { user } = useUser();
  
  return (
    <PrivateRoute>
      <div>
      <SignOut />
      <div className="flex flex-col items-center justify-center min-h-screen">
        

        {/* Upload button at the end of the task list */}
        {user?.role === "manager" && (
          <Link href="/file-upload">
            <button className="bg-gradient-to-r from-blue-500 to-indigo-600 text-white font-semibold px-6 py-3 rounded-lg shadow-lg hover:from-blue-600 hover:to-indigo-700 hover:scale-105 transform transition duration-300 ease-in-out absolute bottom-0 right-0 mb-6 mr-6">
              📤 Upload
            </button>
          </Link>
        )}
      </div>
    </div>
    </PrivateRoute>
  );
}
