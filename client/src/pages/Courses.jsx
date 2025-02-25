import { useCourses } from "../features/courses/useCourses";

export default function Courses() {
    const { data: courses, isLoading, error } = useCourses();

    console.log("Courses:", courses);
    
    if (isLoading) return <main><h1>Loading courses...</h1></main>;
    if (error) return <main><h1>Error loading courses</h1></main>;

    return (
        <main>
            <h1>Courses</h1>
            <ul>
                {courses && courses.length > 0 ? (
                    courses.map((course) => <li key={course.id}><a href={`/courses/${course.id}`}>{course.name}</a></li>)
                ) : (
                    <p>No courses available</p>
                )}
            </ul>
        </main>
    );
}
