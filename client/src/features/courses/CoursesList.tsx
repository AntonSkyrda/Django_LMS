import { useCourses } from "./useCourses";
import Spinner from "../../ui/Spinner";
import Empty from "../../ui/Empty";
import CourseCard from "./CourseCard";

function CoursesList() {
  const { isLoading, courses } = useCourses();
  if (isLoading) return <Spinner />;
  if (!courses) return <Empty resourceName="Курси" />;
  return (
    <ul className="grid grid-cols-4">
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </ul>
  );
}

export default CoursesList;
