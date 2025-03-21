import { useCourses } from "../features/courses/useCourses";
// import { getCourses } from "../lib/services/courses";
// import useAuthHeader from "react-auth-kit/hooks/useAuthHeader";

export default function Dashboard() {
  const { courses } = useCourses();
  console.log(courses);
  if (!courses) return <div>no courses</div>;
  return (
    <div>
      <ul>
        {courses.map((course) => (
          <li key={course.id}>{course.name}</li>
        ))}
      </ul>
    </div>
  );
}
