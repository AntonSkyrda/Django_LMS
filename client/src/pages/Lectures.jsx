import { useLectures } from "../features/lectures/useLectures.js";

export default function Lectures() {
    const { data: lecture, isLoading, error } = useLectures();

    console.log("Lectures:", lecture);

    if (isLoading) return <main><h1>Loading courses...</h1></main>;
    if (error) return <main><h1>Error loading courses</h1></main>;

    return (
        <main>
            <h1>Courses</h1>
            <ul>
                {lecture && lecture.length > 0 ? (
                    lecture.map((lecture) => <li key={lecture.id}><a href={`/lectures/${lecture.id}`}>{lecture.name}</a></li>)
                ) : (
                    <p>No lectures available</p>
                )}
            </ul>
        </main>
    );
}
