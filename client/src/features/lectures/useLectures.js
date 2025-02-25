import { useQuery, useQueryClient } from "@tanstack/react-query";

async function getLectures() {
    const res = await fetch("http://127.0.0.1:8000/api/lectures");
    const data = await res.json();

    return data
}

export function useLectures() {
    const queryClient = useQueryClient();
    const {isLoading, data} = useQuery(
        {
            queryKey: ["Courses"],
            queryFn: () => getLectures(),
        }
    )

    return {isLoading, data};
}