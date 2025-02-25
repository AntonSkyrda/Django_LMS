import { BrowserRouter, Route, Routes } from "react-router-dom";
import { lazy, Suspense } from "react";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import AppLayout from "./ui/AppLayout";
import { AuthProvider } from "./context/AuthContext.jsx";
import ProtectedRoute from "./components/ProtectedRoute";

const Homepage = lazy(() => import("./pages/Homepage"));
const Courses = lazy(() => import("./pages/Courses"));
const Course = lazy(() => import("./pages/Course"));
const Lectures = lazy(() => import("./pages/Lectures.jsx"));
const Lecture = lazy(() => import("./pages/Lecture.jsx"));
const LoginPage = lazy(() => import("./pages/LoginPage"));

const queryClient = new QueryClient();

function App() {
  return (
    <AuthProvider>
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <Suspense fallback={<div>Loading...</div>}>
            <Routes>
              <Route path="/login" element={<LoginPage />} />
              <Route element={<ProtectedRoute />}>
                <Route element={<AppLayout />}>
                  <Route index element={<Homepage />} />
                  <Route path="courses" element={<Courses />} />
                  <Route path="courses/:courseId" element={<Course />} />
                  <Route path="lectures" element={<Lectures />} />
                  <Route path="lecture/:lectureId" element={<Lecture />} />
                </Route>
              </Route>
            </Routes>
          </Suspense>
        </BrowserRouter>
      </QueryClientProvider>
    </AuthProvider>
  );
}

export default App;
