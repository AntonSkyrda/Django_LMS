import CoursesList from "../features/courses/CoursesList";
import usePageTitle from "../hooks/usePageTitle";
import Heading from "../ui/Heading";

function Courses() {
  usePageTitle("Курси");
  return (
    <div className="flex flex-col gap-10 px-10 py-4">
      <Heading as="h2">Курси</Heading>
      <CoursesList />
    </div>
  );
}

export default Courses;
