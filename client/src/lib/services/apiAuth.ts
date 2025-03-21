import axios from "axios";

import { authSchema } from "../../schemas/authSchema";

export async function login({
  username,
  password,
}: {
  username: string;
  password: string;
}) {
  const res = await axios
    .post(`${import.meta.env.VITE_BASE_URL}/api/token/`, {
      username,
      password,
    })
    .catch(() => {
      throw new Error(`Невірний Username чи Пароль.`);
    });

  const { success, data: auth } = authSchema.safeParse(res.data);
  if (!success)
    throw new Error(
      " There is an error with authentication service. Please contact administrator.",
    );
  return auth;
}
