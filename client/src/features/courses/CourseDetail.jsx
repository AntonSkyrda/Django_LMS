import { useCourse } from "./useCourse";

export default function CourseDetail() {
    const {isLoading, data: course, error} = useCourse();
    console.log(course)
    if (isLoading) {
        return <p>Loading</p>
    }
    return <div>
        <h3>Name</h3>
        <p>{course.name}</p>
        <h3>Description</h3>
        <p>{course.description}</p>
    </div>
}