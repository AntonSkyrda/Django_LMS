import Form from "../../ui/Form";
import FormRow from "../../ui/FormRow";
import Input from "../../ui/Input";

import { FieldValues, useForm } from "react-hook-form";
import { useLogin } from "./useLogin";

export default function LoginForm() {
  const { register, handleSubmit, formState } = useForm();

  const { errors } = formState;

  const { login, isPending, loginError } = useLogin();

  function onSubmit(data: FieldValues) {
    const { username, password } = data;
    login({ username, password });
  }

  return (
    <Form type="regular" onSubmit={handleSubmit(onSubmit)}>
      <FormRow
        label="Username"
        orientation="vertical"
        error={errors.username?.message?.toString()}
      >
        <Input
          type="username"
          id="username"
          autoComplete="username"
          disabled={isPending}
          {...register("username", {
            required: "Це поле обовʼязкове",
            minLength: {
              value: 5,
              message: "Username має містити більше 10 символів",
            },
          })}
        />
      </FormRow>

      <FormRow
        label="Пароль"
        orientation="vertical"
        error={errors.password?.message?.toString()}
      >
        <Input
          type="password"
          id="password"
          autoComplete="password"
          disabled={isPending}
          {...register("password", {
            required: "Це поле обовʼязкове",
            minLength: {
              value: 5,
              message: "Пароль має містити більше 10 символів",
            },
          })}
        />
      </FormRow>
      <FormRow orientation="vertical" error={loginError?.message}>
        <button className="cursor-pointer">
          {isPending ? "Вхід..." : "Увійти"}
        </button>
      </FormRow>
    </Form>
  );
}
