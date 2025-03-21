import axios from "axios";

import { coursesSchema } from "../../schemas/coursesSchema";

export async function getCourses(authHeader: string) {
  const res = await axios.get(`${import.meta.env.VITE_BASE_URL}/api/courses`, {
    headers: { Authorization: authHeader },
  });
  const { success, data: courses } = coursesSchema.safeParse(res.data);
  if (!success) throw new Error("There is Error with loading Courses data");
  return courses;
}
