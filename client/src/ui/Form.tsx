import { ComponentPropsWithoutRef, ReactNode } from "react";
import { cn } from "../lib/utils/cn";

interface FormProps extends ComponentPropsWithoutRef<"form"> {
  type?: "modal" | "regular";
  aditionalStyles?: string;
  children: ReactNode;
}

export default function Form({
  children,
  type = "regular",
  aditionalStyles,
  ...props
}: FormProps) {
  const styles = {
    regular: "rounded-md border border-gray-100 px-16 py-10",
    modal: "w-[80rem]",
  };

  return (
    <form className={cn(styles[type], aditionalStyles)} {...props}>
      {children}
    </form>
  );
}
