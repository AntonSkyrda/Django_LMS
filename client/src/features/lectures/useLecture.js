import { useQuery, useQueryClient } from "@tanstack/react-query";
import { useParams } from "react-router-dom";

async function getLecture(id) {

    try {
        const res = await fetch(`http://127.0.0.1:8000/api/lecture/${id}`);
        console.log(res)
        const data = await res.json();
        
        return data;
    } catch(r) {
        console.error(r)
    }
}

export function useLecture() {
    const {lectureId} = useParams();
    console.log(lectureId)
    const queryClient = useQueryClient();
    const {isLoading, data} = useQuery(
        {
            queryKey: ["Course", lectureId],
            queryFn: () => getLecture(lectureId),
        }
    );

    return {isLoading, data};
}
