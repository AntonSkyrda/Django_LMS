import { z } from "zod";

export const courseSchema = z.object({
  id: z.number().int().optional(),
  name: z.string().max(255),
  description: z.string(),
  teacher: z.number().int().optional(),
  groups: z.array(z.number()).optional(),
});

export const coursesSchema = z.array(courseSchema);
