import { useLecture } from "./useLecture.js";

export default function LectureDetail() {
    const {isLoading, data: lecture, error} = useLecture();
    console.log(lecture)
    if (isLoading) {
        return <p>Loading</p>
    }
    return <div>
        <h3>Name</h3>
        <p>{lecture.name}</p>
        <h3>Description</h3>
        <p>{lecture.description}</p>
    </div>
}