"use client";

// components/PrivateRoute.tsx
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { useUser } from '../context/UserContext'; // Your custom hook to access the context

const PrivateRoute = ({ children }) => {
  const { user } = useUser(); // Accessing the current user from context
  const router = useRouter();

  useEffect(() => {
    if (!user) {
      // Redirect to login page if no user is logged in
      router.push('/login');
    }
  }, [user, router]); // Dependencies: when 'user' changes, this effect runs

  // Optionally, you can show a loading state while checking for user context
  if (!user) {
    return <div>Loading...</div>; // Or a loading spinner
  }

  return <>{children}</>; // Render protected content when the user exists
};

export default PrivateRoute;
