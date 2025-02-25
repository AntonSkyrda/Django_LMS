import { useQuery, useQueryClient } from "@tanstack/react-query";

async function getCourses() {
    const res = await fetch("http://127.0.0.1:8000/api/courses");
    const data = await res.json();

    return data
}

export function useCourses() {
    const queryClient = useQueryClient();
    const {isLoading, data} = useQuery(
        {
            queryKey: ["Courses"],
            queryFn: () => getCourses(),
        }
    )

    return {isLoading, data};
}