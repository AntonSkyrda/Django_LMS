import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

async function getCourse(id) {

    try {
        const res = await fetch(`http://127.0.0.1:8000/api/courses/${id}`);
        console.log(res)
        const data = await res.json();
        
        return data;
    } catch(r) {
        console.error(r)
    }
}

export function useCourse() {
    const {courseId} = useParams();
    console.log(courseId)
    const queryClient = useQueryClient();
    const {isLoading, data} = useQuery(
        {
            queryKey: ["Course", courseId],
            queryFn: () => getCourse(courseId),
        }
    );

    return {isLoading, data};
}
