"use client";

import SignOut from "@/components/SignOut";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";

export default function FileUpload () {
    const [file, setFile] = useState<File | null>(null);

    const router = useRouter();
    
    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = e.target.files ? e.target.files[0] : null;
        if (selectedFile) {
          setFile(selectedFile);
        }
    }

    const handleUpload = () => {
        if (!file) {
            alert("Please select a file first!");
            return;
          }
          // TODO: send the file to a server
          console.log(file.name);
          router.push("/dashboard");
    }

    return (
        <div>
             {/* SignOut and Back Button on top */}
        <div className="flex justify-between items-center p-4">
            <Link href={"/dashboard"}>
                <button className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                    Dashboard
                </button>
            </Link>
            <SignOut />
        </div>
        {/* Upload Form */}
        <div className="flex flex-col items-center justify-center min-h-screen">
          <h1 className="text-2xl mb-4">Upload MP4/MP3 File</h1>
          <input
            type="file"
            accept=".mp4, .mp3"
            onChange={handleFileChange}
            className="mb-4 p-2 border border-gray-300 rounded"
          />
          <button
            onClick={handleUpload}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Upload File
          </button>
        </div>
        </div>
    );
}