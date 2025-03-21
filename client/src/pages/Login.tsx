import LoginForm from "../features/authentication/LoginForm";
import Heading from "../ui/Heading";

export default function Login() {
  return (
    <div className="grid min-h-[100dvh] grid-cols-[48rem] content-center justify-center gap-12">
      <Heading as="h2" additionalStyles="text-center">
        Виконайте авторизацію
      </Heading>
      <LoginForm />
    </div>
  );
}
