"use client";

import SignOut from "@/components/SignOut";
import axios from "axios";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useState } from "react";

interface RequestBody {
  content: string
}

export default function FileUpload () {
    const [file, setFile] = useState<File | null>(null);
    const [transcription, setTranscription] = useState("");
    const [loading, setLoading] = useState(false);

    const router = useRouter();
    
    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = e.target.files ? e.target.files[0] : null;
        if (selectedFile) {
          setFile(selectedFile);
        }
    }

    const handleUpload = async () => {
        if (!file) {
            alert("Please select a file first!");
            return;
          }
          // TODO: send the file to a server
          console.log(file.name);

          setLoading(true);
          const formData = new FormData();
          formData.append("file", file);
          try {
            const response = await axios.post('http://127.0.0.1:5000/transcribe', formData, {
              headers: {
                'Content-Type': 'multipart/form-data'
              }
            });

            const generated_transcript = response.data.transcription;
            console.log("generated-transcript: ", generated_transcript);
            setTranscription(generated_transcript);

            const dataBody: RequestBody = {
              content: transcription
            }
            
            const response_task = await axios.post("http://0.0.0.0:4050/user/generate-task", dataBody);
            console.log(response_task.data);
          } catch (error) {
            alert("Failed to connect to server.");
          } finally {
            setLoading(false);
          }
          router.push("/task-details");
          // router.push("/dashboard");
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
            disabled={loading}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Submit
          </button>
        </div>
        </div>
    );
}