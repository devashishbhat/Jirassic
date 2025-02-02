"use client";

import { useRouter } from "next/navigation";
import { useUser } from "@/context/UserContext";

export default function SignOut() {
  const router = useRouter();
  const { setUser } = useUser();

  function signOut() {
    setUser(null);
    router.push("/login");
  }
  return (
    <div
      onClick={signOut}
      className="absolute top-4 right-4 flex items-center space-x-2 cursor-pointer border border-gray-300 rounded-lg px-4 py-2 hover:bg-gray-100"
    >
      <div>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          fill="currentColor"
          className="size-6"
        >
          <path
            fillRule="evenodd"
            d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z"
            clipRule="evenodd"
          />
        </svg>
      </div>
      <span>SignOut</span>
    </div>
  );
}
