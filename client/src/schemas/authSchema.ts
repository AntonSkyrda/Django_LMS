import { z } from "zod";

export const authSchema = z.object({
  access: z.string().jwt(),
  refresh: z.string().jwt(),
});
